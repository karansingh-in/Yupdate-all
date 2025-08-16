@echo off
winget upgrade Microsoft.AppInstaller
winget source add --name msstore --arg https://storeedgefd.dsx.mp.microsoft.com/v9.0
winget source update
winget upgrade --include-unknown
pause