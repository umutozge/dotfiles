"Only do this when not done yet for this buffer
if exists("b:did_ftplugin")
	finish
endif

let b:did_ftplugin = 1

"turn on spell check
setlocal spell

"Change to the directory of the opened file
lcd %:p:h

"Load the function definitions for typesetting
source ~/.vim/scripts/latextools.vim

"latex with secure copy
noremap <buffer> <localleader>ls :w<CR>:mkview<CR>:lcd %:p:h<CR>:call Typeset(1,1)<CR>
noremap <buffer> <localleader>,ls :w<CR>:mkview<CR>:lcd %:p:h<CR>::call Typeset(1,0)<CR><CR><CR><CR><CR>

"latex without secure copy
noremap <buffer> <localleader>r :w<CR>:mkview<CR>:lcd %:p:h<CR>:call Typeset(0,1)<CR>
noremap <buffer> <localleader>,r :w<CR>:mkview<CR>:lcd %:p:h<CR>::call Typeset(0,0)<CR><CR><CR>

"bibtex
noremap <buffer> <localleader>b :w<CR>:call Bibtex()<CR>

"view the pdf by evince
noremap <buffer> <localleader>v :!evince %pdf&<CR>

"verbatim
inoremap <buffer> <localleader>V \Verb++i

"run pythontex on the current buffer
nnoremap <buffer> <localleader>pt :!rm -r pythontex* ; pythontex3 <C-R>%<CR>

"wrap the visual selection in curly braces
vnoremap <buffer> <localleader>p meo<Esc>i{<Esc>`ela}<Esc>

"insert environment on the basis of the current register
noremap <buffer> <localleader>ie 0dawi\begin{<C-o>p}<CR>\end{<C-o>p}O

"(un)comment region
vnoremap <buffer> <localleader>c :s/\(^.*$\)/% \1/g<CR>
vnoremap <buffer> <localleader>u :s/^% \(.*\)$/\1/g<CR>

"latex commands:
" produce a label with the current word and copy it to label register
noremap <buffer> <localleader>l <Esc>0i\label{<Esc>Ea}<Esc>v%"lyA<Esc> 
" copy label to the label register  l 
noremap <buffer> <localleader>cl v%"ly
" \xref using the label register l 
noremap <buffer> <localleader>xr i \xref<Esc>"lpa 
" \xxref ditto 
noremap <buffer> <localleader>xxr i \xxref<Esc>"lpa{ }<Esc>hxi

"insert itemize 
noremap <buffer> <localleader>it i\begin{itemize}<CR><CR>\item<CR><CR>\end{itemize}<Esc>?\\item<CR>A 

"math related commands
nnoremap <buffer> <localleader>al i\begin{align*}<CR>\end{align*}<Esc>O
nnoremap <buffer> <localleader>,al i\begin{align}<CR>\end{align}<Esc>O
nnoremap <buffer> <localleader>s i\sysm{} 
inoremap <buffer> <localleader>s \sysm{}
nnoremap <buffer> <localleader>m i$$<Esc>i
inoremap <buffer> <localleader>m $$<Esc>i
nnoremap <buffer> <localleader>n i\{\}<Esc>hi 
inoremap <buffer> <localleader>n \{\}<Esc>hi 


"Beamer related commands
noremap <buffer> <localleader>if i\begin{frame}<CR><CR>\end{frame}<Esc>?begin{frame}<CR>A{}

"for adding 'draft' to the options of the document class
"useful for beamer
noremap <buffer> <localleader>d <Esc>?documentclass<CR>f]i,draft<Esc>''
noremap <buffer> <localleader>,d <Esc>?draft]<CR>dawhx<Esc>''

"Lecture notes
noremap <buffer> <localleader>hl /labelf{lvf}hy/end{uexerciseO\hyperlink{pasol}{\qed}O
