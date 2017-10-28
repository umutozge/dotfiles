imap <buffer> \s <Esc>o<Esc>o=p<Esc>:w<CR>:mkview<CR>a
map  <buffer> \s o<Esc>o=p<Esc>:w<CR>:mkview<CR>a

map <buffer> ,f /begin{<CR>V/end{<CR>zf<CR>k

setlocal foldmethod=marker
setlocal fmr=\\begin,\\end
setlocal foldmethod=marker
