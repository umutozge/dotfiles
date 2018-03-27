" The script typeset.vim
" sourced by the tex ftplugin
" Umut Ozge

function! InitProcList(buffer,isbeamer)
" takes the name of the buffer and whether the buffer is beamer base file
	if a:isbeamer 
		return [substitute(a:buffer,'\(^.\+\)main\.tex','\1hdt',"g"),substitute(a:buffer,'\(^.\+\)main\.tex','\1bmr',"g")]
	else
		return [substitute(a:buffer,'\(^.\+\)\.tex','\1',"g")] 
	endif
endfunction

function! SecureCopy(file,silent)
	if a:silent
		execute "silent !scp -q -c blowfish " . a:file . " oezge@141.58.164.102:~/Dropbox/x/" . a:file ." > /dev/null&"
		execute "redraw!"
	else
		execute "!scp -c blowfish " . a:file . " oezge@141.58.164.102:~/Dropbox/x/" . a:file 
	endif
endfunction

function! Typeset_aux(file,copy,silent)
if a:silent && a:copy
	execute "silent !pdflatex -interaction=batchmode " . a:file ." > /dev/null&"
	call SecureCopy(a:file . ".pdf",a:silent)
	execute "redraw!"
elseif a:silent && !a:copy
	execute "silent !pdflatex -interaction=batchmode " . a:file ." > /dev/null&"
	execute "redraw!"
elseif !a:silent && a:copy
	execute "!pdflatex --shell-escape " . a:file 
	call SecureCopy(a:file . ".pdf",a:silent)
elseif !a:silent && !a:copy
	execute "!pdflatex --shell-escape " . a:file 
endif
endfunction

function! Typeset(copy,silent)
for i in b:proclist
	call Typeset_aux(i,a:copy,a:silent)
endfor	
endfunction

function! Bibtex()
for i in b:proclist
	execute "!bibtex " . i
endfor
endfunction

let b:bufname = bufname("%")

"Initialize the list of files to be processed, the second argument is
"a flag that checks whether we are working on a beamer project
let b:proclist = InitProcList(b:bufname,!(matchstr(b:bufname,'\.main\.') == ""))

