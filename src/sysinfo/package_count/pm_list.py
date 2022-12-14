# Do not use unix pipe!!!

package_managers = [
    {"name": "pacman", "command": "pacman -Qq --color never"},
    {
        "name": "dpkg",
        "command": r"dpkg-query -f '.\n' -W",
    },
    {
        "name": "flatpak",
        "command": "flatpak list --all",
    },
    {
        "name": "pm",
        "command": "pm list packages",
    },
    {"name": "swupd", "command": "swupd bundle-list --quiet"},
    {"name": "bulge", "command": "bulge list"},
    {"name": "pacinstall", "command": "pacinstall -l"},
    {"name": "butch", "command": "butch list"},
    {"name": "lvu", "command": "lvu installed"},
    {"name": "pkgin", "command": "pkgin list"},
    {"name": "xbps", "command": "xbps-query -l"},
    {"name": "tce", "command": "tce-status -i"},
    {"name": "socery", "command": "gaze installed"},
    {"name": "alps", "command": "alps showinstalled"},
    {"name": "opkg", "command": "opkg list-installed"},
    {"name": "cpt", "command": "cpt list"},
    {"name": "pisi", "command": "pisi li"},
    {"name": "apk", "command": "apk info"},
    {"name": "pkgin", "command": "pkgin list"},
    {"name": "cygwin", "command": "cygcheck -cd"},
]
