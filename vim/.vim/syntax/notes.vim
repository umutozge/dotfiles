 augroup filetypedetect
        au BufNewFile,BufRead *.notes     setf notes
        augroup END




:syntax clear
:syntax case match

:syn region myFold start="\begin" end="\end" transparent fold
   :syn sync fromstart
   :set foldmethod=syntax

