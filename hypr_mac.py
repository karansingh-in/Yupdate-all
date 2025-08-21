import subprocess

command = [
    "brew install mas",
    "mas upgrade",
    "clear",
    "echo    _",
    "echo  | |",
    "echo  | |__  _   _ _ __  _ __",
    "echo  | '_ \\| | | | '_ \\| '__|",
    "echo  | | | | |_| | |_) | |",
    "echo  |_| |_|\\__,_| .__/|_|",
    "echo          __/ | |",
    "echo         |___/|_|",
    "echo"
]

for code in command:
    subprocess.run(code, shell=True)

confirm = input("Enter yay to provide confirmation for auto-update process > ")

done = [
    "echo",
    "echo If the cursor is blinking, it indicates the program is actively searching for updates, not frozen.",
    "echo",
    "echo [Press 'Control + C' to force stop any update.]",
    "echo",
    "brew update",
    "brew upgrade",
    "brew upgrade --cask",
    "brew cleanup",
    "brew autoremove",
    'read -n 1 -s -r -p "Press any key to continue..."'
]

if confirm == "yay":
    for work in done:
        subprocess.run(work, shell=True)
else:
    print("closing the terminal...")
    subprocess.run("exit", shell=True)