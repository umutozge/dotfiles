colorscheme obsidian

"start sbcl on a screen window
nnoremap <buffer> <localleader>s :ScreenShell rlwrap sbcl<CR> 
"quit the screen window -- you need to be in vim window
nnoremap <buffer> <localleader>q :ScreenQuit<CR>
"send the selection to sbcl on the screen window
vnoremap <buffer> <localleader>r :'<,'>ScreenSend<CR>

"evaluate the selection in sbcl shell opened inside vim
noremap <buffer> <localleader>e y:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 
"do the same as above if the start and end of selection has not changed -- it is OK to add lines in between
noremap <buffer> <localleader>,e gvy:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 
"send the entire file to internal sbcl 
noremap <buffer> <localleader>w ggvGy:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 

"when on a parenthesis deletes the form included in the current and matching parenthesis
nnoremap <buffer> <localleader>d v%d
"comment selection
vnoremap <buffer> <localleader>c :s/\(^.*$\)/; \1/g<CR>
"uncomment selection
vnoremap <buffer> <localleader>u :s/^; \(.*\)$/\1/g<CR>
"wrap the visual selection in parentheses
vnoremap <buffer> <localleader>p meo<Esc>i(<Esc>`ela)<Esc>
