let bufname = bufname("%")
let pdf = substitute(bufname,'\(^.\+\).tex','\1.pdf',"g")
execute "silent !pdflatex -interaction=batchmode " . bufname ." > /dev/null&"
execute "silent !scp -q -c blowfish " . pdf . " oezge@141.58.164.102:~/Documents/pdf/" . pdf ." > /dev/null&"
execute "redraw!"
