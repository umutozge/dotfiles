let SessionLoad = 1
if &cp | set nocp | endif
nnoremap 	 0i	
nnoremap ,b `wzz20
nnoremap ,i Ji
map ,q i&quot;&quot;hhhhhi
map ,bq i<blockquote></blockquote>ki
map ,pp i<p></p>hhhi
map ,ap a&apos;
map ,h /Kaynak:j"+pv,,hV,s
vmap ,s :s/\(.*>\)\(http:\/\/[^\/]*\/\).*$/\1\2<\/a>/g
vmap ,,h yi<a href=A target="_blank">pa</a>kkkJJJ
map ,j bi<a href="+pi target="_blank">A</a>A
map ,a "qpfnxxxxihreflli#/h2lllvf(hhdk/><lPjdd
map ,p v/Forumlllld?h2nllpau?h2lllvey?namellllpguuVj"qy
map ,c :wggVG"+y
noremap ,av ggi\documentclass{article}\usepackage{avm}\begin{document}Go\end{document}
noremap ,ar /\\begin{avm}V/end{avm}dk"+p
nnoremap Y yg_
nnoremap \dt GVgg:s/\t/    /g
nnoremap \p :set paste"+p:set nopaste
vnoremap \rs :s/^\s\+//g
vnoremap \wc y:!echo '"'|wc -w
nnoremap \rp %x``x
nnoremap \h :set hlsearch!
nnoremap \s :set spell!
nnoremap \da :%d+:w
nnoremap \ya :%y+
noremap \cd :lcd %:p:h
nnoremap \mm :set textwidth=0:colors zenburn
nnoremap \idh :r!date +\%F
nnoremap \idt :r!date +'\%a, \%d \%b \%y -- \%H:\%M'
nnoremap \idd :r!date +\%Y\%m\%d\%t\%a
nnoremap \idr :r!date +\%b\%t\%d\%t\%Y
nnoremap \id :r!date +\%Y\%m\%d
nnoremap \es :vsplit ~/.scratch
vnoremap \as y:call writefile(split(@0,'\n'),'.scratch')
nnoremap \q :wall|execute "mksession!" . v:this_session|qall
nnoremap \sv :source $MYVIMRC
nnoremap \ev :vsplit $MYVIMRC
let s:cpo_save=&cpo
set cpo&vim
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
inoremap  <Left>
inoremap  <Right>
inoremap () ()i
inoremap <> <>i
nnoremap ı i
inoremap Jk 
inoremap JK 
inoremap [] []i
inoremap jK 
inoremap jk 
inoremap {} {}i
abbr lispp \Verb+LISP+
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=indent,eol,start
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=en
set incsearch
set laststatus=2
set nomodeline
set path=~/.mytex/**,~/res/**,~/.vim/,~/bin/**
set printoptions=paper:letter
set ruler
set runtimepath=~/.vim/,/usr/share/vim/vim80
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
set viminfo='100,<50,s10,h,f1
set wildmenu
set wildmode=longest,list,full
set window=69
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/res/github/symbols-and-programming
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 README.md
badd +53 assignments/cogs502-assignment-01.tex
badd +813 notes/cogs502-lecture-notes.tex
badd +1 assignments/cogs502-assignment-02.tex
badd +1 assignments/test.lisp
badd +105 assignments/cogs502-assignment-03.tex
badd +4 assignments/cogs502-assignment-05.tex
badd +33 assignments/cogs502-assignment-06.tex
badd +117 code/iteration.lisp
badd +1 ~/Dropbox/res/cr/ex.pool
badd +44 assignments/cogs502-assignment-07.tex
badd +97 code/assignment-07.lisp
badd +1 code/assignment-08.lisp
badd +80 code/assignment-06.lisp
badd +1 code/assignment-05.lisp
badd +0 assignments/cogs502-assignment-12.tex
argglobal
silent! argdel *
argadd README.md
set stal=2
edit README.md
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=fb:*,fb:-,fb:+,n:>
setlocal commentstring=>\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'markdown'
setlocal filetype=markdown
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcqln
setlocal formatlistpat=^\\s*\\d\\+\\.\\s\\+\\|^[-*+]\\s\\+\\|^\\[^\\ze[^\\]]\\+\\]:
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal nomodeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=htmlcomplete#CompleteTags
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'markdown'
setlocal syntax=markdown
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 22 - ((15 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
22
normal! 078|
tabedit notes/cogs502-lecture-notes.tex
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
noremap <buffer> ,hl /labelf{lvf}hy/end{uexerciseO\hyperlink{pasol}{\qed}O
noremap <buffer> ,,udr ?draft]dawhx''
noremap <buffer> ,dr ?documentclassf]i,draft''
noremap <buffer> ,if i\begin{frame}\end{frame}?begin{frame}A{}
nnoremap <buffer> ,n i\{\}hi 
nnoremap <buffer> ,m i$$i
nnoremap <buffer> ,s i\sysm{} 
nnoremap <buffer> ,,al i\begin{align}\end{align}O
nnoremap <buffer> ,al i\begin{align*}\end{align*}O
noremap <buffer> ,it i\begin{itemize}\item\end{itemize}?\\itemA 
noremap <buffer> ,xxr i \xxref"lpa{ }hxi
noremap <buffer> ,xr i \xref"lpa 
noremap <buffer> ,cl v%"ly
noremap <buffer> ,l 0i\label{Ea}v%"lyA 
noremap <buffer> ,dc gg/comment}%start0i%/comment}%end0i%
noremap <buffer> ,ac gg/comment}%start0x/comment}%end0x
vnoremap <buffer> ,u :s/^% \(.*\)$/\1/g
vnoremap <buffer> ,c :s/\(^.*$\)/% \1/g
noremap <buffer> ,ie 0dawi\begin{p}\end{p}O
vnoremap <buffer> ,p meoi{`ela}
nnoremap <buffer> ,pt :!rm -r pythontex* ; pythontex3 %
noremap <buffer> ,v :!evince %pdf&
noremap <buffer> ,b :w:call Bibtex()
noremap <buffer> ,,r :w:mkview:lcd %:p:h::call Typeset(0,0)
noremap <buffer> ,r :w:mkview:lcd %:p:h:call Typeset(0,1)
noremap <buffer> ,,ls :w:mkview:lcd %:p:h::call Typeset(1,0)
noremap <buffer> ,ls :w:mkview:lcd %:p:h:call Typeset(1,1)
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> şş :!setxkbmap -layout usi<Right>
inoremap <buffer> ,n \{\}hi 
inoremap <buffer> ,m $$i
inoremap <buffer> ,s \sysm{}
inoremap <buffer> ,V \Verb++i
inoremap <buffer> ;; :!setxkbmap -layout tri<Right>
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'tex'
setlocal filetype=tex
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal nomodeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'tex'
setlocal syntax=tex
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 1162 - ((29 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1162
normal! 0
lcd ~/Dropbox/res/github/symbols-and-programming/notes
tabedit ~/Dropbox/res/cr/ex.pool
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != ''
setlocal filetype=
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal nomodeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != ''
setlocal syntax=
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 109 - ((33 * winheight(0) + 24) / 49)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
109
normal! 0
lcd ~/Dropbox/res/github/symbols-and-programming/assignments
tabedit ~/Dropbox/res/github/symbols-and-programming/assignments/cogs502-assignment-12.tex
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
argglobal
noremap <buffer> ,hl /labelf{lvf}hy/end{uexerciseO\hyperlink{pasol}{\qed}O
noremap <buffer> ,,udr ?draft]dawhx''
noremap <buffer> ,dr ?documentclassf]i,draft''
noremap <buffer> ,if i\begin{frame}\end{frame}?begin{frame}A{}
nnoremap <buffer> ,n i\{\}hi 
nnoremap <buffer> ,m i$$i
nnoremap <buffer> ,s i\sysm{} 
nnoremap <buffer> ,,al i\begin{align}\end{align}O
nnoremap <buffer> ,al i\begin{align*}\end{align*}O
noremap <buffer> ,it i\begin{itemize}\item\end{itemize}?\\itemA 
noremap <buffer> ,xxr i \xxref"lpa{ }hxi
noremap <buffer> ,xr i \xref"lpa 
noremap <buffer> ,cl v%"ly
noremap <buffer> ,l 0i\label{Ea}v%"lyA 
noremap <buffer> ,dc gg/comment}%start0i%/comment}%end0i%
noremap <buffer> ,ac gg/comment}%start0x/comment}%end0x
vnoremap <buffer> ,u :s/^% \(.*\)$/\1/g
vnoremap <buffer> ,c :s/\(^.*$\)/% \1/g
noremap <buffer> ,ie 0dawi\begin{p}\end{p}O
vnoremap <buffer> ,p meoi{`ela}
nnoremap <buffer> ,pt :!rm -r pythontex* ; pythontex3 %
noremap <buffer> ,v :!evince %pdf&
noremap <buffer> ,b :w:call Bibtex()
noremap <buffer> ,,r :w:mkview:lcd %:p:h::call Typeset(0,0)
noremap <buffer> ,r :w:mkview:lcd %:p:h:call Typeset(0,1)
noremap <buffer> ,,ls :w:mkview:lcd %:p:h::call Typeset(1,0)
noremap <buffer> ,ls :w:mkview:lcd %:p:h:call Typeset(1,1)
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> şş :!setxkbmap -layout usi<Right>
inoremap <buffer> ,n \{\}hi 
inoremap <buffer> ,m $$i
inoremap <buffer> ,s \sysm{}
inoremap <buffer> ,V \Verb++i
inoremap <buffer> ;; :!setxkbmap -layout tri<Right>
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'tex'
setlocal filetype=tex
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=2
setlocal imsearch=2
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal nomodeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'tex'
setlocal syntax=tex
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 38 - ((26 * winheight(0) + 33) / 67)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
38
normal! 0
lcd ~/Dropbox/res/github/symbols-and-programming/assignments
tabnext 4
set stal=1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
