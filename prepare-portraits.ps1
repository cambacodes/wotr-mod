$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$artRoot = Join-Path $PSScriptRoot 'art'
$packRoot = Join-Path $artRoot 'CustomNpcPortraits'

# The authored images stay intact. These are the three PNG formats required by the game.
function Export-GamePortrait([string]$Name, [int]$FaceX, [int]$FaceY, [int]$CropWidth) {
    $inputPath = Join-Path $artRoot "originals/$Name.png"
    $outputDir = Join-Path $packRoot "Portraits - Npc/$Name"
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
    $original = [Drawing.Image]::FromFile($inputPath)
    try {
        foreach ($size in @(@('Fulllength.png', 692, 1024), @('Medium.png', 330, 432), @('Small.png', 185, 242))) {
            $width = [int]$size[1]; $height = [int]$size[2]
            $bitmap = New-Object Drawing.Bitmap $width, $height
            $graphics = [Drawing.Graphics]::FromImage($bitmap)
            try {
                $graphics.InterpolationMode = [Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
                if ($size[0] -eq 'Fulllength.png') {
                    $sourceRect = New-Object Drawing.RectangleF 0, 0, $original.Width, $original.Height
                } else {
                    $cropHeight = [int]($CropWidth * $height / $width)
                    $sourceRect = New-Object Drawing.RectangleF $FaceX, $FaceY, $CropWidth, $cropHeight
                }
                $targetRect = New-Object Drawing.RectangleF 0, 0, $width, $height
                $graphics.DrawImage($original, $targetRect, $sourceRect, [Drawing.GraphicsUnit]::Pixel)
                $bitmap.Save((Join-Path $outputDir $size[0]), [Drawing.Imaging.ImageFormat]::Png)
            } finally { $graphics.Dispose(); $bitmap.Dispose() }
        }
    } finally { $original.Dispose() }
    $sceneDir = Join-Path $packRoot 'RanRomance-Tirabade/Scenes'
    New-Item -ItemType Directory -Force -Path $sceneDir | Out-Null
    Copy-Item -LiteralPath (Join-Path $outputDir 'Medium.png') -Destination (Join-Path $sceneDir "$Name.png")
}

Export-GamePortrait 'Anevia' 258 18 505
Export-GamePortrait 'Irabeth' 263 37 525
Copy-Item -LiteralPath (Join-Path $artRoot 'originals/Together.png') -Destination (Join-Path $packRoot 'RanRomance-Tirabade/Scenes/Together.png')
