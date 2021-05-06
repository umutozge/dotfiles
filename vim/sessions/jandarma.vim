let SessionLoad = 1
if &cp | set nocp | endif
nnoremap 	 0i	
map ,c :wggVG"+y
map ,p v/Forumlllld?h2nllpau?h2lllvey?namellllpguuVj"qy
map ,a "qpfnxxxxihreflli#/h2lllvf(hhdk/><lPjdd
map ,j bi<a href="+pi target="_blank">A</a>A
vmap ,,h yi<a href=A target="_blank">pa</a>kkkJJJ
vmap ,s :s/\(.*>\)\(http:\/\/[^\/]*\/\).*$/\1\2<\/a>/g
map ,h /Kaynak:j"+pv,,hV,s
map ,ap a&apos;
map ,pp i<p></p>hhhi
map ,bq i<blockquote></blockquote>ki
map ,q i&quot;&quot;hhhhhi
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
abbr vr veritabanı
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
set runtimepath=~/.vim/,/usr/share/vim/vim81
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set tabstop=4
set viminfo='100,<50,s10,h,f1
set wildmenu
set wildmode=longest,list,full
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/Dropbox/res/github/veritabani-dersi/chapters
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd yapilandirma.md
edit yapilandirma.md
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
noremap <buffer> ,d V/```k:s/.*> //g  
noremap <buffer> ,k o```sql```k:set paste"+p:set nopaste
noremap <buffer> ,,t o```bash```ko
noremap <buffer> ,t i ``i
vnoremap <buffer> ,c Ombova-->`bi<!---
inoremap <buffer> ,t ``i
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
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
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
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal sidescrolloff=-1
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
setlocal termmode=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
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
let s:l = 486 - ((28 * winheight(0) + 16) / 32)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
486
normal! 0
tabnext 1
badd +0 yapilandirma.md
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
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
