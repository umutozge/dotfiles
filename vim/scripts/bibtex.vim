let bufname = bufname("%")
let name = substitute(bufname,'\(^.\+\).tex','\1',"g")
execute "!bibtex " . name
