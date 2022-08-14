#!/usr/bin/env python3

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Notify 
# for testing

# win = Gtk.Window()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()

def notify(layout):
    Notify.init ("msm-layout")
    Hello=Notify.Notification.new ("Layout Applied",f"Layout: {layout}","")
    Hello.show()
    
def default():
    #this function first disables all the extensions (those are modified here)
    os.system('gnome-extensions disable dash-to-dock@micxgx.gmail.com')
    os.system('gnome-extensions disable dash-to-panel@jderose9.github.com')
    os.system('gnome-extensions disable arcmenu@arcmenu.com')

class Handler:
    def onDestroy():
        Gtk.main_quit()
    

        
    def gnomelay(self, *args):
        layout_name='GNOME'
        default()
        notify(layout_name)
        return
        
        
        


    def macishlay(self, *args):
        layout_name='MacOS-ish'
        default()
        
        os.system('gnome-extensions enable dash-to-dock@micxgx.gmail.com')
        notify(layout_name)
        return

    def ubuntuislay(self, *args):
        return

    def winelevenish(self, *args):
        return

    def winxpish(self, *args):
        layout_name='WinXP-ish'
        default()
        
        os.system('gnome-extensions enable dash-to-panel@jderose9.github.com')
        os.system('gnome-extensions enable arcmenu@arcmenu.com')
        notify(layout_name)
        return

    def materialshell(self, *args):
        return
    
    def exec_installex(self, *args):
        os.system('pkexec curl --proto \'=https\' --tlsv1.2 -sSf https://raw.githubusercontent.com/msm-linux/msm-layouts/master/extension-index/installer.py | python3')
        return








if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_file("msmlayout.glade")
    builder.connect_signals(Handler())
    
    
    window = builder.get_object("window1")
    window.show_all()
    Gtk.main()