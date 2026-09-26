using System;
using System.Linq;
using System.Speech.Synthesis;
using System.Text;

internal static class Program
{
    private static void Main(string[] args)
    {
        using (var voice = new SpeechSynthesizer())
        {
            var female = voice.GetInstalledVoices().FirstOrDefault(v => v.Enabled && v.VoiceInfo.Gender == VoiceGender.Female && v.VoiceInfo.Culture.TwoLetterISOLanguageName == "en");
            if (female != null) voice.SelectVoice(female.VoiceInfo.Name);
            // A real synthesis check writes audio without speaking over the user's running game.
            if (args.Length == 2 && args[0] == "--check")
            {
                voice.SetOutputToWaveFile(args[1]);
                voice.Speak("Three at the Table. Anevia and Irabeth.");
                return;
            }
            voice.SetOutputToDefaultAudioDevice();
            string line;
            while ((line = Console.ReadLine()) != null)
            {
                voice.SpeakAsyncCancelAll();
                if (line == "STOP") continue;
                int space = line.IndexOf(' ');
                if (space < 1) continue;
                try
                {
                    voice.Rate = Math.Max(-3, Math.Min(3, int.Parse(line.Substring(0, space))));
                    voice.SpeakAsync(Encoding.UTF8.GetString(Convert.FromBase64String(line.Substring(space + 1))));
                }
                catch (FormatException) { /* Ignore a malformed message and continue reading the pipe. */ }
            }
            voice.SpeakAsyncCancelAll();
        }
    }
}
