@echo off
mkdir output
for %%f in (*.png) do (
    tesseract "%%f" "output\%%~nf" -l eng
)
