setlocal foldmethod=manual


imap <buffer> \s <Esc>o<CR>=p<Esc>:w<CR>:mkview<CR>a
map  <buffer> \s o<CR>=p<Esc>:w<CR>:mkview<CR>a

