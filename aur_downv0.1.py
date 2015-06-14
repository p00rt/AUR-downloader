#!/usr/bin/python
import os

os.system("mkdir /tmp/.AUR_DOWN")
in_pkgs = raw_input( "Type AUR packages names separated byspaces (eg. eggs spam foo): " )
med_pkgs = in_pkgs.split(' ')
pkgs = []
for i in med_pkgs:
    pkgs.append(i)
del in_pkgs, med_pkgs


def pkgs_install():
    for i in pkgs:
        os.system( "cd /tmp/.AUR_DOWN && wget https://aur.archlinux.org/packages/" + i[0] + i[1] + '/' + i +'/' + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN && tar xvf " + i +".tar.gz" )
        os.system("cd /tmp/.AUR_DOWN/"+i +" && makepkg -si")

pkgs_install()
os.system("rm -r /.tmp/AUR_DOWN")

