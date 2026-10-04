using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using Tirabade;

var story = JsonSerializer.Deserialize<Story>(File.ReadAllText("development/Story.json"),
    new JsonSerializerOptions { IncludeFields = true });
var assembly = typeof(Story).Assembly;
assembly.GetType("Program").GetField("story", BindingFlags.Static | BindingFlags.NonPublic).SetValue(null, story);
int failures = 0;
Action<bool, string> check = (ok, message) => { if (!ok) throw new Exception(message); };
foreach (string name in args)
{
    try
    {
        assembly.GetType(name).GetMethod("Run", BindingFlags.Static | BindingFlags.NonPublic)
            .Invoke(null, new object[] { story, check });
        Console.WriteLine("PASS " + name);
    }
    catch (Exception error)
    {
        failures++;
        Console.WriteLine("FAIL " + name + ": " + (error.InnerException ?? error).Message);
    }
}
return failures == 0 ? 0 : 1;
