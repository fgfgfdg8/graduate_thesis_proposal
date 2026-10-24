# Regenerate figures/fig_rag_conceptions.pdf from figures/rag_conceptions.svg
#
# Why a browser engine is required:
#   The draw.io SVG stores its text as <switch>(<foreignObject> + base64 <image>),
#   not as <text>. Only Chromium renders foreignObject as real vector text;
#   Inkscape / cairosvg fall back to the embedded base64 raster, which produces
#   blurry text and a PDF with NO embedded fonts.
#
# Three gotchas:
#   1. The SVG must be INLINED into the HTML. Loading it via <img src> skips
#      foreignObject and yields a blank page.
#   2. The working path must be pure ASCII. A non-ASCII (e.g. Chinese) path makes
#      the file:// URL invalid and the browser silently renders nothing.
#   3. @page size must come from the SVG root width/height, with zero margin.
#
# Usage:
#   powershell -NoProfile -ExecutionPolicy Bypass -File figures\render_rag_conceptions.ps1
#
# NOTE: keep this file ASCII-only. Windows PowerShell 5.1 reads .ps1 as ANSI/GBK
# when there is no BOM, which corrupts non-ASCII comments and breaks parsing.

$ErrorActionPreference = "Stop"

# $PSScriptRoot is <repo>\figures, so ".." is the repo root
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$src  = Join-Path $repo "figures\rag_conceptions.svg"
$out  = Join-Path $repo "figures\fig_rag_conceptions.pdf"

if (-not (Test-Path $src)) { throw "source SVG not found: $src" }

# ---------- locate Edge ----------
$edgeCandidates = @(
    "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
)
$edge = $edgeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw "msedge.exe not found; set the path manually" }
Write-Host "Edge: $edge"

# ---------- read SVG and parse its size ----------
$raw = [System.IO.File]::ReadAllText($src, (New-Object System.Text.UTF8Encoding($false)))
$m = [regex]::Match($raw, '<svg[^>]*width="([0-9.]+)px"[^>]*height="([0-9.]+)px"')
if (-not $m.Success) { throw "cannot parse width/height from the SVG root element" }
$w = [double]$m.Groups[1].Value
$h = [double]$m.Groups[2].Value
Write-Host ("SVG size: {0}px x {1}px" -f $w, $h)

# drop the XML declaration so the markup can be inlined
$svg = $raw.Substring($raw.IndexOf("<svg"))

# ---------- build wrapper HTML ----------
$work = Join-Path $env:TEMP "svgwork"
New-Item -ItemType Directory -Force -Path $work | Out-Null

$head = '<!doctype html>' + "`n" +
        '<html><head><meta charset="utf-8"><style>' + "`n" +
        "@page { size: ${w}px ${h}px; margin: 0; }" + "`n" +
        'html, body { margin:0; padding:0; background:#ffffff; }' + "`n" +
        "svg { display:block; width:${w}px; height:${h}px; }" + "`n" +
        '</style></head><body>' + "`n"
$tail = "`n" + '</body></html>' + "`n"

$htmlPath = Join-Path $work "wrap.html"
[System.IO.File]::WriteAllText($htmlPath, $head + $svg + $tail, (New-Object System.Text.UTF8Encoding($false)))
Write-Host "HTML: $htmlPath"

# ---------- headless print to PDF ----------
$pdfTmp = Join-Path $work "wrap.pdf"
if (Test-Path $pdfTmp) { Remove-Item $pdfTmp -Force }

$url = "file:///" + ($work -replace '\\', '/') + "/wrap.html"
$edgeArgs = @(
    "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
    "--virtual-time-budget=10000", "--no-pdf-header-footer",
    "--print-to-pdf=$pdfTmp", $url
)

# Edge writes unrelated warnings to stderr (e.g. the QQBrowser importer warning).
# With $ErrorActionPreference='Stop', PowerShell would treat those as terminating
# errors, so relax it for this native call and discard stderr.
$prevEap = $ErrorActionPreference
$ErrorActionPreference = "Continue"
& $edge @edgeArgs 2>$null | Out-Null
$edgeExit = $LASTEXITCODE
$ErrorActionPreference = $prevEap
Write-Host "Edge exit code: $edgeExit"

if (-not (Test-Path $pdfTmp)) { throw "Edge produced no PDF at $pdfTmp" }

# ---------- verify BEFORE overwriting the tracked PDF ----------
$info  = (& pdfinfo  $pdfTmp 2>&1 | Out-String)
$fonts = (& pdffonts $pdfTmp 2>&1 | Out-String)
Write-Host $info
Write-Host $fonts

if ($fonts -notmatch "YaHei|Noto|SimSun|Hei") {
    throw "no CJK font embedded -- text likely degraded to a bitmap; aborting"
}
if ($info -notmatch "Pages:\s+1\b") {
    throw "expected exactly 1 page; aborting"
}

Copy-Item $pdfTmp $out -Force
Write-Host ("Wrote: {0} ({1} bytes)" -f $out, (Get-Item $out).Length)
