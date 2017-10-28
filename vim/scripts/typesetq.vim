let bufname = bufname("%")
execute "silent !pdflatex -interaction=batchmode " . bufname . " > /dev/null&" 
execute "redraw!"
