#!/bin/bash

rsync -av --delete-before ~/res/ /media/amnesia/pers-bk/home-bk/res/
rsync -av --delete-before ~/lib/ /media/amnesia/pers-bk/home-bk/lib/
rsync -av --delete-before ~/mn/ /media/amnesia/pers-bk/home-bk/mn/
rsync -av --delete-before ~/tmp/ /media/amnesia/pers-bk/home-bk/tmp/
rsync -av --delete-before ~/var/ /media/amnesia/pers-bk/home-bk/var/
rsync -av --delete-before ~/bck/ /media/amnesia/pers-bk/home-bk/bck/
rsync -av --delete-before ~/gdrive/ /media/amnesia/pers-bk/home-bk/gdrive/
rsync -av --delete-before ~/VirtualBox\ VMs/ /media/amnesia/pers-bk/home-bk/VirtualBox\ VMs/
