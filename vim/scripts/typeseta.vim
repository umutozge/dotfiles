" The script typeset.vim
" sourced by the tex ftplugin

function! InitProcList(buffer,isbeamer)
" takes the name of the buffer and whether the buffer is beamer base file
	if a:isbeamer 
		return [substitute(a:buffer,'\(^.\+\)main\.tex','\1.hdt',"g"),substitute(a:buffer,'\(^.\+\)main\.tex','\1.bmr',"g")]
	else
		return [a:buffer] 
	endif
endfunction

function! SecureCopy(file,silent)
	if silent
		execute "silent !scp -q -c blowfish " . a:file . " oezge@141.58.164.102:~/Documents/pdf/" . a:file ." > /dev/null&"
		execute "redraw!"
	else
		execute "!scp -c blowfish " . a:file . " oezge@141.58.164.102:~/Documents/pdf/" . a:file 
	endif
endfunction

function! Typeset_aux(file,copy,silent)
	if a:silent && a:copy
		execute "silent !pdflatex -interaction=batchmode " . a:file ." > /dev/null&"
		call SecureCopy(substitute(a:file,'\(^.\+\).tex','\1.pdf',"g",a:silent)
		execute "redraw!"
	elseif a:silent && !a:copy
		execute "silent !pdflatex -interaction=batchmode " . a:file ." > /dev/null&"
		execute "redraw!"
	elseif !a:silent && a:copy
		execute "!pdflatex " . a:file 
		call SecureCopy(substitute(a:file,'\(^.\+\).tex','\1.pdf',"g",a:silent)
	elseif !a:silent && !a:copy
		execute "!pdflatex " . a:file 
	endif
endfunction

function! Typeset(copy,silent)
for i in b:proclist
	Typeset_aux(i,a:copy,a:silent)
endfor	
endfunction



let b:bufname = "tiblisi.main.tex"
"let b:bufname = bufname("%")
"Check whether you are working on a beamer base file 
let b:isbeamer = !(matchstr(b:bufname,'\.main\.') == "")
"Initialize the list of files to be processed

let b:proclist = InitProcList(b:bufname,!(matchstr(b:bufname,'\.main\.') == ""))


call Typeset(1,1)
"function! PDFLatexProcWithCopy(bufname)
"
"let b:pdf = substitute(bufname,'\(^.\+\).tex','\1.pdf',"g")
