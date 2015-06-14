#!/usr/bin/python
import os

os.system("mkdir /tmp/.AUR_DOWN")

def pkgs_install():
    for i in sys.argv:
        os.system( "cd /tmp/.AUR_DOWN && wget https://aur.archlinux.org/packages/" + i[0] + i[1] + '/' + i +'/' + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN && tar xvf " + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN/"+i +" && makepkg -si")

pkgs_install()
os.system("rm -r /.tmp/AUR_DOWN")

