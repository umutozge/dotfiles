#!/bin/bash
cd ~/Dropbox/lib/dotfiles/
echo -n {'profile','bashrc','mutt','muttrc.gmail','muttrc.riseup','mytex','screenrc','vim','vimrc','xmonad'} | xargs -d ' ' -I + echo  'ln -s `pwd`/.+ ~/.+'|sh
