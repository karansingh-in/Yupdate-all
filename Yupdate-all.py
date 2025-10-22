import subprocess

command = [
"ipconfig/flushdns",
"del /q/f/s %TEMP%\*",
"cls",
"@echo off",
"color 04",          
"echo( __  __                __      __                   ____",
"echo( \ \/ /_  ______  ____/ /___ _/ /____        ____ _/ / /",
"echo(  \  / / / / __ \/ __  / __ `/ __/ _ \______/ __ `/ / /",
"echo(  / / /_/ / /_/ / /_/ / /_/ / /_/  __/_____/ /_/ / / /",
"echo( /_/\__,_/ .___/\__,_/\__,_/\__/\___/      \__,_/_/_/",
"echo(        /_/",
"title karansingh-in",
"prompt Yupdate-all$G",
]

for code in command :
    subprocess.run(code, shell= True)

confirm = input('''Enter 'setup' if running for the first time, 'help' for troubleshooting common issues >
Enter 'yay' to provide confirmation for auto-update process > ''')

done = [
"color 07",
"echo.",
"echo If the cursor is blinking, it indicates the program is actively searching for updates, not frozen.",
"echo.",
"echo [Press 'Ctrl + C' to force stop any update.]",
"echo.",
"winget upgrade --all --silent --accept-source-agreements --accept-package-agreements",
"pause"
]

help = [
"color 07",
"echo NOTE : Microsoft Edge and a few system apps are updated via windows update only or externally via microsoft store.",
"echo.",
"echo If the terminal shows 'Winget' is not recognised as an internal or external known command, just restart your system and you are good to go",
"echo.",
"echo If while setup it shows any error, run the app as administrator. This is common because it install the windows package manager which may require admin permisions",
"pause"
]

setup = [
    "color 07",
    "echo.",
    "echo Setting up this system with the prerequisites and dependencies.",
    "@echo off",
    "bitsadmin /transfer \"WingetDownload\" /download /priority normal https://github.com/microsoft/winget-cli/releases/latest/download/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle \"%DOWNLOAD_DIR%\winget.msixbundle\"",
    "add-appxpackage C:\Winget\winget.msixbundle",
    "@echo off",
    "winget upgrade Microsoft.AppInstaller",
    "winget source add --name msstore --arg https://storeedgefd.dsx.mp.microsoft.com/v9.0",
    "winget source update",
    "winget upgrade --include-unknown",
    "echo All set! reopen the app and you the good to go...",
    "pause"
]
if(confirm == "yay"):
    for work in done :
        subprocess.run(work, shell= True)
elif(confirm == 'setup'):
    for work in setup :
        subprocess.run(work,shell= True)
elif(confirm == "help"):
    for work in help:
        subprocess.run(work, shell= True)


else:
    print("closing the terminal...")
    subprocess.run("exit", shell= True)        

