#!/usr/bin/env python3
## curl https://raw.githubusercontent.com/msm-linux/msm-layouts/master/extension-index/installer.py | python
# curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/msm-linux/msm-layouts/master/extension-index/installer.py | python3
## curl -sL https://raw.githubusercontent.com/wimpysworld/deb-get/main/deb-get | sudo -E bash -s install deb-get

######### EXTENSION INDEX ############
### All extensions are tested to work on GNOME 41
### Maintainence Status: ACTIVE

extension_index = {
    "dash-to-dock@micxgx.gmail.com":"https://extensions.gnome.org/extension-data/dash-to-dockmicxgx.gmail.com.v71.shell-extension.zip",
    "disable dash-to-panel@jderose9.github.com":"https://extensions.gnome.org/extension-data/dash-to-paneljderose9.github.com.v46.shell-extension.zip",
    "arcmenu@arcmenu.com":"https://extensions.gnome.org/extension-data/arcmenuarcmenu.com.v35.shell-extension.zip",
}

print(extension_index)

for extension in extension_index:
    print(extension)