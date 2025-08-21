import subprocess

command = [
"ipconfig/flushdns",
"del /q/f/s %TEMP%\*",
"cls",
"@echo off",
"echo(   _",              
"echo(  ^| ^|",
"echo(  ^| ^|__  _   _ _ __  _ __",
"echo(  ^| '_ \^| ^| ^| ^| '_ \^| '__^|",
"echo(  ^| ^| ^| ^| ^|_^| ^| ^|_) ^| ^|",
"echo(  ^|_^| ^|_^|\__, ^| .__/^|_^|",
"echo(          __/ ^| ^|",       
"echo(         ^|___/^|_^|",
"title karansingh-in",
"prompt hypr$G"
]

for code in command :
    subprocess.run(code, shell= True)

confirm = input("Enter yay to provide confirmation for auto-update process > ")

done = [
"echo.",
"echo If the cursor is blinking, it indicates the program is actively searching for updates, not frozen.",
"echo.",
"echo NOTE : Microsoft Edge and a few system apps are updated via windows update only or externally via microsoft store.",
"echo [Press 'Ctrl + C' to force stop any update.]",
"echo.",
"winget upgrade --all --silent --accept-source-agreements --accept-package-agreements",
"pause"
]

if(confirm == "yay"):
    for work in done :
        subprocess.run(work, shell= True)

else:
    print("closing the terminal...")
    subprocess.run("exit", shell= True)        

