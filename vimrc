"" vim initialization
"" Umut Ozge
""

set encoding=utf-8
set runtimepath=~/.vim/,$VIMRUNTIME

" this setting is used by tabfind command, with tabfind you can access any file in the
" path quickly
set path=~/.mytex/**,~/res/**,~/.vim/,~/bin/**

filetype plugin on
syn on

let leader = "\\"
let maplocalleader = ","

set laststatus=2
""uncomment and adjust the following if you want the text to autowrap when past the textwidth
"set textwidth=80
set autoindent
set tabstop=4
set wildmode=longest,list,full
set wildmenu
set viminfo+=f1
set incsearch

"global key bindings

nnoremap <TAB> 0i<TAB><ESC>
inoremap jk <ESC>
inoremap <C-F> <Right>
inoremap <C-B> <Left>

"" If you open and close brackets quickly, you end up inside them in insert mode
inoremap () ()<Esc>i
inoremap {} {}<Esc>i
inoremap [] []<Esc>i
inoremap <> <><Esc>i


"" edit vimrc
nnoremap <leader>ev :vsplit $MYVIMRC<CR>
"" source vimrc
nnoremap <leader>sv :source $MYVIMRC<CR>

"" append selection to a scratch file
vnoremap <leader>as y:call writefile(split(@0,'\n'),'.scratch')<CR>
"y:w! >> ~/.scratch<CR>
"" view scratch
nnoremap <leader>vs :vsplit ~/.scratch<CR>

"" various ways of inserting dates
nnoremap <leader>id  :r!date +\%Y\%m\%d
nnoremap <leader>idr :r!date +\%b\%t\%d\%t\%Y
nnoremap <leader>idd  :r!date +\%Y\%m\%d\%t\%a
nnoremap <leader>idt :r!date +'\%a, \%d \%b \%y -- \%H:\%M'
nnoremap <leader>idh :r!date +\%F


" mutt starts vim global settings, so this is for switching to mutt-mode
nnoremap <leader>mm :set textwidth=0<CR>:colors zenburn<CR>

"locally change to the directory of the current file
noremap <leader>cd :lcd %:p:h<CR>

" toggle spell check
nnoremap <leader>s :set spell!<CR>

"toggle highlight search
nnoremap <leader>h :set hlsearch!<CR>

"remove brackets, do this while you are on one of the brackets 
nnoremap <leader>rp %x``x

"word count the selection
vnoremap <leader>wc y:!echo '<C-R>"'\|wc -w 

hi SpellBad ctermfg=white ctermbg=red

"remove leading white space in selection
vnoremap <leader>rs :s/^\s\+//g<CR>

"auto commands

augroup python
	autocmd!
	autocmd FileType python iabbrev <buffer> iff if:<left>
	autocmd FileType python iabbrev <buffer> forr for:<left>
	autocmd FileType python iabbrev <buffer> eliff elif:<left>
augroup END

augroup markdown
	autocmd FileType markdown colorscheme zenburn 
augroup END

augroup latex
	autocmd!
	autocmd FileType tex inoremap <buffer> ;; <C-c>:!setxkbmap -layout tr<CR>i<right>
	autocmd FileType tex inoremap <buffer> şş <C-c>:!setxkbmap -layout us<CR>i<right>
augroup END

augroup ccg
	autocmd!
	autocmd BufNewFile,BufRead *.ccg nnoremap <buffer> <localleader>i :vsplit inspect<CR>:set paste<CR><C-a>>:read /tmp/screen-exchange<CR>:set nopaste<CR>
augroup END
