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
set nohlsearch
set showtabline=0
set incsearch

"global key bindings

nnoremap <Space> <Right>
nnoremap <TAB> 0i<TAB><ESC>
nnoremap <C-U> <PageUp>
nnoremap <C-D> <PageDown>
inoremap <C-F> <Right>
inoremap <C-B> <Left>

"" If you open and close brackets quickly, you end up inside them in insert mode
inoremap () ()<Esc>i
inoremap {} {}<Esc>i
inoremap [] []<Esc>i
inoremap <> <><Esc>i

"" various ways of inserting dates
nnoremap <leader>id  :r!date +\%Y\%m\%d
nnoremap <leader>idt :r!date +'\%a, \%d \%b \%y -- \%H:\%M'
nnoremap <leader>idd :r!date +\%F

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

"hi SpellBad ctermfg=white ctermbg=red
