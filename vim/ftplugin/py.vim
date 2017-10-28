
"(un)comment region
vmap <buffer> ,c :s/\(^.*$\)/# \1/g<CR>
vmap <buffer> ,u :s/^# \(.*\)$/\1/g<CR>

set textwidth=10000
set shiftwidth=4
