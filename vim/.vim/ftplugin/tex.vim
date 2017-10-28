"Only do this when not done yet for this buffer

if exists("b:did_ftplugin")
	finish
endif
let b:did_ftplugin = 1


setlocal spell
"Change to the directory of the opened file
lcd %:p:h
"Load the function definition for typesetting
source ~/.vim/scripts/latextools.vim


"latex with secure copy
map <buffer> ,l :w<CR>:mkview<CR>:lcd %:p:h<CR>:call Typeset(1,1)<CR>
map <buffer> ,,l :w<CR>:mkview<CR>:lcd %:p:h<CR>::call Typeset(1,0)<CR><CR><CR><CR><CR>
"latex without secure copy
map <buffer> ,r :w<CR>:mkview<CR>:lcd %:p:h<CR>:call Typeset(0,1)<CR>
map <buffer> ,,r :w<CR>:mkview<CR>:lcd %:p:h<CR>::call Typeset(0,0)<CR><CR><CR>
"bibtex
map <buffer> ,b :w<CR>:call Bibtex()<CR>

"view the pdf by evince
map <buffer> ,v :!evince %pdf&<CR>

map ,a  i\textsf{f i}

"verbatim
imap ,V \Verb++i

"map ,i   i{\lli}
"map ,u   i\"
"map ,g   i\u{lli}
"map ,c   i\c{lli}
"map ,I   i\.

"VARIOUS SHORTCUTS 

"insert environment
map <buffer> ,ie 0dawi\begin{<C-o>p}<CR>\end{<C-o>p}O


"(un)comment region
vmap <buffer> ,c :s/\(^.*$\)/% \1/g<CR>
vmap <buffer> ,u :s/^% \(.*\)$/\1/g<CR>

"latex commands:
"\label
map <buffer> \l <Esc>0i\label{<Esc>Ea}<Esc>v%"lyA<Esc> 
"\myenum
map <buffer> \m  i\myenum{}<Esc>li
map <buffer> \mm  i\myeenum{}<Esc>li
" copy label to the label register  l 
map <buffer> \cl v%"ly
" \xref using the label register l 
map <buffer> \xr i \xref<Esc>"lpa 
" \xxref ditto 
map <buffer> \xxr i \xxref<Esc>"lpa{ }<Esc>hxi
"curly brace
map <buffer> \b <Esc>Bi{<Esc>Ea}<Esc>

"inserting environments
map ,it i\begin{itemize}<CR><CR>\item<CR><CR>\end{itemize}<Esc>?\\item<CR>A 

"math related commands
map ,al i\begin{align*}<CR>\end{align*}<Esc>O
map ,,al i\begin{align}<CR>\end{align}<Esc>O

"Beamer related commands
map ,if i\begin{frame}<CR><CR>\end{frame}<Esc>?begin{frame}<CR>A{}

"for adding 'draft' to the options of the document class
"useful for beamer
map <buffer> ,d <Esc>?documentclass<CR>f]i,draft<Esc>''
map <buffer> ,,d <Esc>?draft]<CR>dawhx<Esc>''

"Older days
map <buffer> <F2> :source ~/.vim/scripts/shortex.vim<CR> 

map <buffer> <F6> :w<CR>/maketitle<CR>jV/% NOTES<CR>k:w! tomain.tex<CR>``<CR>:chdir ..<CR><CR> :!pdflatex main.tex<CR><CR>:!bibtex main<CR><CR>:!pdflatex main.tex<CR><CR>:!pdflatex main.tex<CR><CR>:chdir -<CR><CR>
imap <buffer> <F6> <Esc>:w<CR>/maketitle<CR>jV/% NOTES<CR>k:w! tomain.tex<CR>``<CR>:chdir ..<CR><CR> :!pdflatex main.tex<CR><CR>:!bibtex main<CR><CR>:!pdflatex main.tex<CR><CR>:!pdflatex main.tex<CR><CR>:chdir -<CR><CR> 
