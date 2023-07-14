# AllanWm
A highly customizable replacement for the windows shell written in python with PySide6.

## Roadmap

⚫ Future
🔴 Not started
🟡 Working on it
🟢 Done

| Feature | Status |
| ----------- | ----------- |
| Bar | 🟢 |
| App launcher | 🟢 |
| App switcher | 🟢 |
| Clock | 🟢 |
| Power menu | 🟢 |
| Theming: Colours | 🟡 |
| Documentation | 🟡 |
| Theming: Fonts | 🔴 |
| Tiling Window manager | ⚫ |
| Workspaces | ⚫ |
| Theming: More | ⚫ |
| Progress bars | ⚫ |

## Setup
(requires windows 10)

1. Make sure the above requirement is met - this (probably) only works on windows 10.
2. Move the taskbar to the top of the screen
3. Enable "Use small taskbar buttons" in windows settings
4. OPTIONAL: Setup [taskbarx](https://github.com/ChrisAnd1998/TaskbarX) to center the taskbar icons. This isn't a requirement, but it makes windows' animations fit in better with this project.
5. Install the [Fira code](https://github.com/tonsky/FiraCode) font family
6. Download `AllanWm.exe` from the latest release [here](https://github.com/Aworldc/AllanWm/releases)
7. Create a file called `.allanwmrc` and paste into it [this text](https://raw.githubusercontent.com/Aworldc/AllanWm/main/.allanwmrc). If you have trouble creating that file, press <kbd>win + r</kbd>, paste the following command into the popup, then press <kbd>enter</kbd>.
    ```batch
    cmd /c cd Desktop && echo "" > ".allanwmrc"
    ```
8. Move `AllanWm.exe` and `.allanwmrc` into a folder on your computer you won't move or rename. I suggest you use `username/Documents/Bin`, `username/Bin`, `username/bin`, or `C:/bin`.
9. Right click on `AllanWm.exe`, click `Send to`, and then `Desktop (create shortcut)`. A shortcut will appear on your desktop.
10. Press <kbd>win + r</kbd>, type `shell:startup`, then press <kbd>enter</kbd>. This will open a special folder.
11. Drag and drop the shortcut from step 9 into the folder opened by step 10.
12. You're done! Reboot and AllanWm should start soon after you log on.
