 
# qwqfetch

Hi!

This is a replacement of neofetch in [hyfetch](https://github.com/hykilpikonna/hyfetch), written in python. It will serve as a module for output system information.

Now it is still in its early state, several items has not been worked on, and it may (very possibly) display weird information on your system, or even simply throw an exception.

This is the output on my Arch Linux:
```
aleksana@Aleksana-laptop
------------------------
OS: Arch Linux x86_64
Host: LENOVO LNVNB161216
Kernel: 5.19.1-zen1-1.1-zen
Uptime: 1 day, 7 hours, 21 mins
Packages: 1120 (pacman), 11 (flatpak)
Shell: zsh 5.9
Resolution: 2240x1400
DE: Plasma 5.25.4 [KF5 5.97.0] [Qt 5.15.5]
Theme: Breeze [GTK2/3/Qt]
Icons: Papirus-Dark [GTK2/3/Qt]
Cursor: breeze_cursors
Terminal: konsole
Terminal Font: SFMono Nerd Font Mono 11
CPU: AMD Ryzen 7 5800H (16) @ 3.200GHz
GPU: AMD ATI Cezanne
Memory: 6124MiB / 13816MiB
```

And also windows (without the need of MinGW):
```
Aleksana@DESKTOP-8D84B2M
------------------------
OS: Microsoft Windows 10 Pro AMD64
Host: Intel Corporation 440BX Desktop Reference Platform
Kernel: NT 10.0.19044
Uptime: 5 hours, 1 min
Shell: cmd 10.0.19044.1889
Resolution: 2226x1205
DE: Windows Shell
Terminal: WindowsTerminal
CPU: AMD Ryzen 7 5800H (4) @ 3.19 GHz
GPU: VMware SVGA 3D
Memory: 2.5 GiB / 4.0 GiB
```

The platforms we plan to support first are GNU/Linux (popular distributions that adheres to a set of specifications), Windows and MacOS. But if you need it, feel free to ask, and we'll try our best.(Note that we don't plan to support python<3.7)

Any kind of contributions is welcomed. For faster test & feedback, join our telegram group [@hyfetch](https://t.me/hyfetch).