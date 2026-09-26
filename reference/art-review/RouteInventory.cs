using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Reflection.Emit;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

internal static class RouteInventory
{
    public static int Main(string[] args)
    {
        string managed = Path.Combine(args[0], "Wrath_Data/Managed");
        AppDomain.CurrentDomain.AssemblyResolve += delegate(object sender, ResolveEventArgs e)
        {
            string name = new AssemblyName(e.Name).Name + ".dll";
            foreach (string dir in new[] { managed, Path.Combine(managed, "UnityModManager"), Path.Combine(args[0], "Mods/RanRomance") })
                if (File.Exists(Path.Combine(dir, name))) return Assembly.LoadFrom(Path.Combine(dir, name));
            return null;
        };
        try { typeof(RouteInventory).Assembly.GetType("InventoryRun").GetMethod("Run").Invoke(null, new object[] { args }); return 0; }
        catch (Exception ex) { Console.Error.WriteLine(ex); return 1; }
    }
}

internal static class InventoryRun
{
    public static void Run(string[] args)
    {
        string folder = Path.Combine(args[0], "Mods/RanRomance");
        var strings = JArray.Parse(File.ReadAllText(Path.Combine(folder, "LocalizedStrings.json")));
        var opcodes = typeof(OpCodes).GetFields(BindingFlags.Public | BindingFlags.Static)
            .Where(f => f.FieldType == typeof(OpCode)).Select(f => (OpCode)f.GetValue(null))
            .ToDictionary(o => unchecked((ushort)o.Value));
        var assembly = Assembly.LoadFrom(Path.Combine(folder, "RanRomance.dll"));
        var records = new List<object>();
        Type[] types;
        string[] loaderErrors = new string[0];
        try { types = assembly.GetTypes(); }
        catch (ReflectionTypeLoadException ex)
        {
            types = ex.Types.Where(t => t != null).ToArray();
            loaderErrors = ex.LoaderExceptions.Select(e => e.Message).Distinct().ToArray();
            foreach (string error in loaderErrors) Console.WriteLine(error);
        }
        foreach (Type type in types.Where(t => t.FullName.StartsWith("RanRomance.") || t.FullName.StartsWith("Epilogue.")))
        {
            var methods = type.GetMethods(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance | BindingFlags.DeclaredOnly).Cast<MethodBase>()
                .Concat(type.GetConstructors(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static | BindingFlags.Instance | BindingFlags.DeclaredOnly));
            foreach (MethodBase method in methods)
            {
                var body = method.GetMethodBody();
                if (body == null) continue;
                var il = body.GetILAsByteArray();
                var literals = new List<object>();
                var calls = new List<object>();
                int pos = 0;
                while (pos < il.Length)
                {
                    int offset = pos;
                    ushort code = il[pos++];
                    if (code == 0xfe) code = (ushort)(0xfe00 | il[pos++]);
                    OpCode op = opcodes[code];
                    int size;
                    switch (op.OperandType)
                    {
                        case OperandType.InlineNone: size = 0; break;
                        case OperandType.ShortInlineBrTarget:
                        case OperandType.ShortInlineI:
                        case OperandType.ShortInlineVar: size = 1; break;
                        case OperandType.InlineVar: size = 2; break;
                        case OperandType.InlineI8:
                        case OperandType.InlineR: size = 8; break;
                        case OperandType.InlineSwitch: size = 4 + 4 * BitConverter.ToInt32(il, pos); break;
                        default: size = 4; break;
                    }
                    if (op.OperandType == OperandType.InlineString)
                        literals.Add(new { Offset = offset, Value = method.Module.ResolveString(BitConverter.ToInt32(il, pos)) });
                    if (op.OperandType == OperandType.InlineMethod)
                    {
                        try
                        {
                            var target = method.Module.ResolveMethod(BitConverter.ToInt32(il, pos), type.GetGenericArguments(), method.IsGenericMethod ? method.GetGenericArguments() : Type.EmptyTypes);
                            calls.Add(new { Offset = offset, Target = target.DeclaringType.FullName + "." + target.Name, Token = target.MetadataToken });
                        }
                        catch (Exception ex) { calls.Add(new { Offset = offset, Error = ex.GetType().Name }); }
                    }
                    pos += size;
                }
                records.Add(new { Type = type.FullName, Method = method.Name, Token = method.MetadataToken, Strings = literals, Calls = calls });
            }
        }
        File.WriteAllText(args[1], JsonConvert.SerializeObject(new { Localization = strings, Methods = records, LoaderErrors = loaderErrors }, Formatting.Indented));
        Console.WriteLine("Extracted " + strings.Count + " localization entries and " + records.Count + " methods without executing mod configuration.");
    }
}
