using System;
using System.IO;
using System.Reflection;

internal static class Bootstrap
{
    internal static string RepositoryRoot => Path.GetFullPath(Environment.GetEnvironmentVariable("RRT_TEST_REPO_ROOT")
        ?? Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "../../../.."));

    private static int Main(string[] args)
    {
        // No Windows crash dialog on a failed check (it piled up dialogs on the desktop): print and exit 1.
        AppDomain.CurrentDomain.UnhandledException += (_, e) => { Console.Error.WriteLine(e.ExceptionObject); Environment.Exit(1); };
        if (args.Length != 2)
        {
            Console.Error.WriteLine("Usage: ManagedBuildTests.exe <game directory> <story.json>");
            return 2;
        }
        string game = Path.GetFullPath(args[0]);
        string root = RepositoryRoot;
        string mod = Path.GetFullPath(Environment.GetEnvironmentVariable("RRT_TEST_MOD_DIR")
            ?? Path.Combine(root, "src/bin/Release/net48"));
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
