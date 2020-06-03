# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
# don't overwrite GNU Midnight Commander's setting of `ignorespace'.
export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups
# ... or force ignoredups and ignorespace
export HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
#case "$TERM" in
#    xterm-color) color_prompt=yes;;
#esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

#if [ -n "$force_color_prompt" ]; then
#    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
#	color_prompt=yes
#    else
#	color_prompt=
#    fi
#fi

#if [ "$color_prompt" = yes ]; then
#    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
#else
#    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
#fi
#unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
#case "$TERM" in
#xterm*|rxvt*)
#    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
#    ;;
#*)
#    ;;
#esac

# Alias definitions.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi


# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi

export LANG=en_US.UTF-8

#source .fehbg
#source .xinitrc

`if [ -n "$DISPLAY" ]; then
          xset b off
         fi`


# Various utility functions

function drops
{
watch -n1 dropbox status
}

function lsswp
{
find . -regex '.*.sw[^zf]'
}

function edd 
{

declare -A files

f=$(find . -name $1)
k=`echo $f | xargs -n1` 

count=0
for x in $k
do
	files[$count]=$x
	count=$(($count + 1))
done


if [ ${#files[@]} = 0 ]
then
	echo $1 not found.
elif [ ${#files[@]} -gt 1 ]
then
	keys=${!files[@]}
	echo $keys
	keys=`echo $keys | xargs -n 1 | sort -n`
	echo $keys
	for x in $keys 
	do
		echo $x ${files[$x]}
	done
	read -p 'Select the file to edit: ' selection
	vim ${files[$selection]}
else
	vim $f
fi
}

function rn 
{

declare -A files

f=$(find . -name $2)
k=`echo $f | xargs -n1` 

count=0
for x in $k
do
	files[$count]=$x
	count=$(($count + 1))
done


if [ ${#files[@]} = 0 ]
then
	echo $1 not found.
elif [ ${#files[@]} -gt 1 ]
then
	keys=${!files[@]}
	keys=`echo $keys | xargs -n 1 | sort -n`
	for x in $keys 
	do
		echo $x ${files[$x]}
	done
	read -p "Select the file to run $1 on: " selection
	$1 ${files[$selection]}&
else
	$1 $f&
fi
}

export -f rn 
export -f edd
export -f drops
export -f lsswp
