
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    eval "`dircolors -b`"
    alias ls='ls --color=always'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias la='ls -A'
alias l='ls -CF'
alias ll='ls -lh'
alias la='ls -A'
alias lt='ls -lt'
alias lsnc='ls --color=never'
alias lspdf='ls -l *pdf'
alias lstex='ls -l *tex'
alias gmail='mutt -F ~/.muttrc.gmail'
alias course='vim -S ~/.vim/sessions/course.vim'
alias paper='vim -S ~/.vim/sessions/paper.vim'
alias lit='vim -S ~/.vim/sessions/lt.vim'
alias jan='vim -S ~/.vim/sessions/jandarma.vim'
alias e502='vim -S ~/.vim/sessions/502.vim'
alias e543='vim -S ~/.vim/sessions/543.vim'
alias u532='echo "." | gmail -s "pls check for updates" cogsci-532'
alias u502='echo "." | gmail -s "pls check for updates" cogsci-502'
alias remi='remind -n ~/.reminders|sort'
alias sbcl='rlwrap sbcl'
alias cwd='cd ~/wd'
alias ent='vim ~/Dropbox/mn/nt.md'
alias evince='evince &> /dev/null'
