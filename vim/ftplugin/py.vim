
"colorscheme apprentice


"(un)comment region
"vmap <buffer> ,c :s/\(^.*$\)/# \1/g<CR>
vmap <buffer> ,c :s/^/#/<CR>
"vmap <buffer> ,u :s/^# \(.*\)$/\1/g<CR>
vmap <buffer> ,u :s/^#//<CR>

" run non-interactive
noremap <buffer> <localleader>r :w<CR>:!python3 <c-r>%<CR>
" run interactive
noremap <buffer> <localleader>,r :w<CR>:!python3 -i <c-r>%<CR>

set textwidth=10000
set shiftwidth=4
