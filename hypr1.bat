@echo off

title karansingh-in
prompt hypr$G
echo.
echo If the cursor is blinking, it means the program is actively searching for updates (not frozen).
echo.
echo 🔄 Checking for updates...
winget upgrade --all || pause

