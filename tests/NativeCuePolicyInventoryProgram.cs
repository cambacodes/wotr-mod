#if NATIVE_GAME_POLICY
using System;
internal static class NativeCuePolicyInventoryProgram
{
    private static int Main()
    {
        try
        {
            int count = 0;
            NativeCuePolicyInventoryTests.RunNative((ok, message) => { count++; if (!ok) throw new Exception(message); });
            Console.WriteLine("PASS: eng7-f5 production cue-policy fixtures; " + count + " assertions");
            return 0;
        }
        catch (Exception ex) { Console.Error.WriteLine(ex); return 1; }
    }
}
#endif
