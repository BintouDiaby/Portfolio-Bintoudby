# Export frontend and backend into separate folders for independent git repos
# Run from repo root: PowerShell -ExecutionPolicy Bypass -File .\scripts\export_separate_repos.ps1

$root = Resolve-Path -Path (Join-Path $PSScriptRoot '..')
Set-Location $root.Path

$frontendDst = Join-Path $root 'frontend-repo'
$backendDst = Join-Path $root 'backend-repo'

Write-Host "Creating destinations..."
New-Item -ItemType Directory -Force -Path $frontendDst | Out-Null
New-Item -ItemType Directory -Force -Path $backendDst | Out-Null

Write-Host "Copying frontend files..."
# Files/dirs to copy for frontend (adjust if you want more/less)
$frontendItems = @(
  'package.json',
  'angular.json',
  'tsconfig.json',
  'tsconfig.app.json',
  'tsconfig.spec.json',
  'src',
  'README.md'
)
foreach ($item in $frontendItems) {
  if (Test-Path $item) {
    $dst = Join-Path $frontendDst (Split-Path $item -Leaf)
    Write-Host "Copying $item -> $dst"
    Copy-Item -Path $item -Destination $dst -Recurse -Force -ErrorAction SilentlyContinue
  } else {
    Write-Host "Warning: skipped missing frontend item: $item"
  }
}

Write-Host "Copying backend files..."
if (Test-Path 'backend') {
  Copy-Item -Path 'backend\*' -Destination $backendDst -Recurse -Force -ErrorAction SilentlyContinue
} else {
  Write-Host "Warning: 'backend' folder not found in repo root."
}

# Create small .gitignore files
$gitignoreFrontend = @'
node_modules/
dist/
.vscode/
.env
'@

$gitignoreBackend = @'
node_modules/
data.sqlite
.env
.vscode/
'@

Set-Content -Path (Join-Path $frontendDst '.gitignore') -Value $gitignoreFrontend -Encoding UTF8
Set-Content -Path (Join-Path $backendDst '.gitignore') -Value $gitignoreBackend -Encoding UTF8

Write-Host "Export complete."
Write-Host "Next steps:"
Write-Host " - Inspect frontend-repo and backend-repo directories."
Write-Host " - Initialize separate git repos and push them:" 
Write-Host "     cd frontend-repo; git init; git add .; git commit -m 'initial frontend'; git remote add origin <FRONTEND_REMOTE>; git push -u origin main"
Write-Host "     cd backend-repo; git init; git add .; git commit -m 'initial backend'; git remote add origin <BACKEND_REMOTE>; git push -u origin main"

Write-Host "If you want, I can run the script now."
