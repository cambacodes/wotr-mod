param([int]$X=-1,[int]$Y=-1,[string]$Keys='')
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System.Runtime.InteropServices;
public static class UiInput {
 [DllImport("user32.dll")] public static extern bool ShowWindow(System.IntPtr window, int command);
 [DllImport("user32.dll")] public static extern bool SetForegroundWindow(System.IntPtr window);
 [DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);
 [DllImport("user32.dll")] public static extern void mouse_event(uint flags,uint x,uint y,uint data, System.UIntPtr extra);
}
"@
[UiInput]::ShowWindow((Get-Process Wrath).MainWindowHandle,9) | Out-Null
[UiInput]::SetForegroundWindow((Get-Process Wrath).MainWindowHandle) | Out-Null
Start-Sleep -Milliseconds 300
if($X -ge 0) { [UiInput]::SetCursorPos($X,$Y) | Out-Null; [UiInput]::mouse_event(2,0,0,0,[UIntPtr]::Zero); [UiInput]::mouse_event(4,0,0,0,[UIntPtr]::Zero) }
if($Keys) { [Windows.Forms.SendKeys]::SendWait($Keys) }
Start-Sleep -Milliseconds 700
$screen = [Windows.Forms.SystemInformation]::VirtualScreen
$bitmap = New-Object Drawing.Bitmap $screen.Width,$screen.Height
$graphics = [Drawing.Graphics]::FromImage($bitmap)
$graphics.CopyFromScreen($screen.Location,[Drawing.Point]::Empty,$screen.Size)
$bitmap.Save((Join-Path $PSScriptRoot 'runtime-screen.png'))
$graphics.Dispose()
$bitmap.Dispose()


