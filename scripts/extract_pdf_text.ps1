$src = "C:\Users\victu\Downloads\portfolio-angular-main\portfolio-angular-main\src\assets\cv\CV-DIABY-NABINTOU.pdf"
$dest = "extracted_cv.txt"
$bytes = [System.IO.File]::ReadAllBytes($src)
$text = [System.Text.Encoding]::Latin1.GetString($bytes)
Set-Content -Path $dest -Value $text -Encoding UTF8
Write-Output "extraction-complete"