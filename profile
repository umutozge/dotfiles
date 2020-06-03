export EDITOR="/usr/bin/vim"
export TZ='Europe/Istanbul'
export LANG=en_US.UTF-8

export TEXMFHOME="${HOME}/.mytex//"
export TEXINPUTS="${TEXMFHOME}:${TEXINPUTS}:/usr/local/share/texmf//:/usr/share/texmf//"
export PYTHONPATH="${PYTHONPATH}:${HOME}/bin/py/:${HOME}/res/github/prog-book/code/:${HOME}/local/bin/"
export PS1="[\A-\W]$ "
export BIB=".mytex/bibtex/bib/ozge.bib"
export PATH="${PATH}:${HOME}/bin/sh:${HOME}/bin/sh/langtools:${HOME}/bin/py:${HOME}/bin/MMAX2:${HOME}/sp"
export CDPATH=:~/res/

shopt -s cdable_vars
export dsp=${HOME}/res/github/symbols-and-programming/
export dtl=${HOME}/res/github/theoretical-linguistics/


# keyboard layout switcher

# setxkbmap -option grp:switch,grp:win_space_toggle,grp_led:scroll tr,us

# stuff added by CCGlab installer
export RLWRAP=rlwrap
export CCGLAB_HOME=/home/umut/res/github/ccglab
export CCGLAB_LISP=/usr/bin/sbcl
export LALR_HOME=/home/umut/res/github/ccglab
export PATH=:.:$CCGLAB_HOME/bin:$PATH
# end of stuff added by CCGlab installer

# stanford parser
export CORENLP_HOME=${HOME}/sp
export STANFORDNLP_HOME=${HOME}/sp
export CLASSPATH=${HOME}/sp:${HOME}/sp/stanford-parser.jar:${HOME}/sp/stanford-parser-3.9.2-models.jar:${HOME}/sp/:/home/umut/sp/slf4j-simple-1.7.26.jar:${HOME}/sp/stanford-english-corenlp-2018-10-05-models.jar:${HOME}/sp/stanford-parser-3.9.2-javadoc.jar:${HOME}/sp/stanford-parser-3.9.2-sources.jar:${HOME}/sp/ejml-0.23.jar

#smallworld
#export SW_HOME=/home/umut/res/github/computational-semantics/code/main

source ~/.bashrc
