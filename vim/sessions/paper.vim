let SessionLoad = 1
if &cp | set nocp | endif
nnoremap 	 0i	
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
nnoremap Y yg_
nnoremap \p :set paste"+p:set nopaste
vnoremap \rs :s/^\s\+//g
vnoremap \wc y:!echo '"'|wc -w 
nnoremap \rp %x``x
nnoremap \h :set hlsearch!
nnoremap \s :set spell!
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
vnoremap jk 
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
inoremap  <Left>
inoremap  <Right>
inoremap  <PageUp>
inoremap () ()i
inoremap <> <>i
inoremap [] []i
inoremap jk 
inoremap {} {}i
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
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
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 Dropbox/res/pp/sent-nom/sent-nom.tex
badd +1 Dropbox/res/github/bare-objects/paper/tr-bare-objects.tex
badd +23 Dropbox/res/pp/nominalization-biblio/nominalization-bibliography.tex
badd +1 Dropbox/res/pp/otsoi/otsoi.tex
badd +15 Dropbox/lib/dotfiles/.mytex/bibtex/bib/ozge.bib
badd +92 .vimrc
badd +4 Dropbox/res/pp/sentnom-biblio/sentnom-biblio.tex
badd +1 Dropbox/res/pp/cc-biblio/cc-biblio.tex
badd +1 Dropbox/res/pp/sent-nom/mais-abstract.tex
badd +3 Dropbox/res/tpcs/comparatives.md
badd +1 Dropbox/res/tlks/2018-01-05-cogs-colloq/2018-01-05-cogs-colloq.tex
argglobal
silent! argdel *
argadd Dropbox/res/pp/sent-nom/sent-nom.tex
set stal=2
edit Dropbox/res/pp/sent-nom/sent-nom.tex
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
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=~/.vim//spell/en.utf-8.add
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
let s:l = 550 - ((28 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
550
normal! 0
lcd ~/Dropbox/res/pp/sent-nom
tabedit ~/Dropbox/res/tlks/2018-01-05-cogs-colloq/2018-01-05-cogs-colloq.tex
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
let s:l = 160 - ((32 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
160
normal! 0
lcd ~/Dropbox/res/tlks/2018-01-05-cogs-colloq
tabedit ~/Dropbox/lib/dotfiles/.mytex/bibtex/bib/ozge.bib
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
if &filetype != 'bib'
setlocal filetype=bib
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
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=~/.vim//spell/en.utf-8.add
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'bib'
setlocal syntax=bib
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
let s:l = 14 - ((13 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
14
normal! 027|
lcd ~/Dropbox/res/pp/sent-nom
tabedit ~/Dropbox/res/pp/sent-nom/mais-abstract.tex
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
let s:l = 6 - ((5 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 0
lcd ~/Dropbox/res/pp/sent-nom
tabedit ~/Dropbox/res/pp/cc-biblio/cc-biblio.tex
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
let s:l = 31 - ((30 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
31
normal! 0
lcd ~/Dropbox/res/pp/cc-biblio
tabedit ~/Dropbox/lib/dotfiles/.mytex/bibtex/bib/ozge.bib
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
if &filetype != 'bib'
setlocal filetype=bib
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
setlocal spellfile=~/.vim//spell/en.utf-8.add
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'bib'
setlocal syntax=bib
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
let s:l = 28 - ((27 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
28
normal! 032|
lcd ~/Dropbox/res/pp/cc-biblio
tabedit ~/Dropbox/res/github/bare-objects/paper/tr-bare-objects.tex
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
let s:l = 85 - ((37 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
85
normal! 0
lcd ~/Dropbox/res/github/bare-objects/paper
tabedit ~/Dropbox/res/pp/otsoi/otsoi.tex
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
let s:l = 27 - ((26 * winheight(0) + 27) / 55)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
27
normal! 0
lcd ~/Dropbox/res/pp/otsoi
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
