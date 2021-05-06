let SessionLoad = 1
if &cp | set nocp | endif
nnoremap 	 0i	
noremap ,av ggi\documentclass{article}\usepackage{avm}\begin{document}Go\end{document}
noremap ,ar /\\begin{avm}V/end{avm}dk"+p
nnoremap Y yg_
nnoremap \dt GVgg:s/\t/    /g
nnoremap \p :set paste"+p:set nopaste
vnoremap \rs :s/^\s\+//g
nnoremap \wc :!wc -w %
vnoremap \wc y:!echo '"'|wc -w
nnoremap \rp %x``x
nnoremap \h :set hlsearch!
nnoremap \s :set spell!
nnoremap \da :%d+:w
nnoremap \ya :%y+
noremap \cd :lcd %:p:h
nnoremap \mm :set textwidth=0:colors zenburn
nnoremap \gr :lcd %:p:h:!git rm --cached % 
nnoremap \ga :lcd %:p:h:!git add % 
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
inoremap  la
inoremap () ()i
inoremap <> <>i
nnoremap ı i
inoremap Jk 
inoremap JK 
inoremap [] []i
inoremap jK 
inoremap jk 
inoremap {} {}i
inoremap || ||i
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=indent,eol,start
set fileencodings=ucs-bom,utf-8,default,latin1
set guioptions=aegimrLt
set helplang=en
set incsearch
set laststatus=2
set nomodeline
set path=~/.mytex/**,~/res/**,~/.vim/,~/bin/**
set printoptions=paper:letter
set ruler
set runtimepath=~/.vim/,/usr/share/vim/vim81
set spelllang=tr
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabpagemax=50
set tabstop=4
set textwidth=80
set viminfo='100,<50,s10,h,f1
set wildmenu
set wildmode=longest,list,full
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Dropbox/mn/lt/oyku/yalan
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd yalan.tex
edit yalan.tex
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
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
nnoremap <buffer> ,aq i``''hi
noremap <buffer> ,dc gg/comment}%start0i%/comment}%end0i%
noremap <buffer> ,ac gg/comment}%start0x/comment}%end0x
vnoremap <buffer> ,u :s/^% \(.*\)$/\1/g
vnoremap <buffer> ,c :s/\(^.*$\)/% \1/g
noremap <buffer> ,ie 0dawi\begin{p}\end{p}O
vnoremap <buffer> ,p meoi{`ela}
nnoremap <buffer> ,pt :!rm -r pythontex* ; pythontex3 %
noremap <buffer> ,v :!evince &> /dev/null %pdf&
noremap <buffer> ,b :w:call Bibtex()
noremap <buffer> ,,r :w:mkview:lcd %:p:h::call Typeset(0,0)
noremap <buffer> ,r :w:mkview:lcd %:p:h:call Typeset(0,1)
noremap <buffer> ,,ls :w:mkview:lcd %:p:h::call Typeset(1,0)
noremap <buffer> ,ls :w:mkview:lcd %:p:h:call Typeset(1,1)
vnoremap <buffer> \q :s/\(^.*$\)/> \1/g
inoremap <buffer> ,m $$i
inoremap <buffer> ,s \sysm{}
inoremap <buffer> ,an \ldots 
inoremap <buffer> ,V \Verb++i
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
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
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
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=GetTeXIndent()
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e,[,(,{,),},],&,=^s*\\bibitem,=\\item
setlocal noinfercase
setlocal iskeyword=@,48-57,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
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
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=tr
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
setlocal termmode=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=80
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 127 - ((34 * winheight(0) + 17) / 35)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
127
normal! 0
lcd ~/Dropbox/mn/lt/oyku/yalan
tabnext 1
badd +0 ~/Dropbox/mn/lt/oyku/yalan/yalan.tex
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
