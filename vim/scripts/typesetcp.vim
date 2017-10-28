let bufname = bufname("%")
let pdf = substitute(bufname,'\(^.\+\).tex','\1.pdf',"g")
execute "!pdflatex " . bufname 
execute "!scp -c blowfish " . pdf . " oezge@141.58.164.102:~/Documents/pdf/" . pdf 
