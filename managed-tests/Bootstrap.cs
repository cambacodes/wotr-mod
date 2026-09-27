using System;
using System.IO;
using System.Reflection;

internal static class Bootstrap
{
    private static int Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.Error.WriteLine("Usage: ManagedBuildTests.exe <game directory> <story.json>");
            return 2;
        }
        string game = Path.GetFullPath(args[0]);
        string root = Path.GetFullPath(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "../../../.."));
        string mod = Path.Combine(root, "src/bin/Release/net48");
        string managed = Path.Combine(game, "Wrath_Data/Managed");
        AppDomain.CurrentDomain.AssemblyResolve += (_, request) =>
        {
            string filename = new AssemblyName(request.Name).Name + ".dll";
            foreach (string directory in new[] { mod, managed, Path.Combine(managed, "UnityModManager") })
            {
                string file = Path.Combine(directory, filename);
                if (File.Exists(file)) return Assembly.LoadFrom(file);
            }
            return null;
        };
        try
        {
            // RRT_TEST_LOAD=1 runs the real UMM entry point (Main.Load + Harmony PatchAll) instead of the Build suite.
            if (Environment.GetEnvironmentVariable("RRT_TEST_LOAD") == "1")
                return (int)typeof(Bootstrap).Assembly.GetType("LoadSmokeTests").GetMethod("Run").Invoke(null, new object[] { Path.GetFullPath(args[1]), mod });
            return (int)typeof(Bootstrap).Assembly.GetType("Program").GetMethod("Run").Invoke(null, new object[] { game, Path.GetFullPath(args[1]), mod });
        }
        catch (Exception ex) { Console.Error.WriteLine(ex); return 1; }
    }

}
