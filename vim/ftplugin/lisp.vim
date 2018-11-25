colorscheme obsidian

"start sbcl on a screen window
nnoremap <buffer> <localleader>s :ScreenShell rlwrap sbcl<CR> 
"quit the screen window -- you need to be in vim window
nnoremap <buffer> <localleader>q :ScreenQuit<CR>
"send the selection to sbcl on the screen window
vnoremap <buffer> <localleader>,e :'<,'>ScreenSend<CR><C-A><TAB>

"evaluate the selection in sbcl shell opened inside vim
noremap <buffer> <localleader>e ymw:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 
"do the same as above if the start and end of selection has not changed -- it is OK to add lines in between
noremap <buffer> <localleader>re gvy:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 
"send the region between marks s and e
noremap <buffer> <localleader>em mw`sV`ey:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 
"send the entire file to internal sbcl 
noremap <buffer> <localleader>w mwggVGy:call writefile(split(@0,'\n'),'.tmp')<CR>:!rlwrap sbcl --load ".tmp"<CR> 

"deletes the form included in the nearest leftward and matching parentheses
nnoremap <buffer> <localleader>d ?(<CR>v%d
"copies the form included in the nearest leftward and matching parentheses
nnoremap <buffer> <localleader>y ?(<CR>v%y
"folds the form included in the nearest leftward parenthesis at the start of
"a line and matching parentheses. Works anywhere from within the def*
nnoremap <buffer> <localleader>f ?^(<CR>V%zf
"strips the enclosing func
nnoremap <buffer> <localleader>,t ?(<CR>mz%x`zxdt(
"comment selection
vnoremap <buffer> <localleader>c :s/\(^.*$\)/; \1/g<CR>
"uncomment selection
vnoremap <buffer> <localleader>u :s/^; \(.*\)$/\1/g<CR>
"wrap the visual selection in parentheses
vnoremap <buffer> <localleader>p meo<Esc>i(<Esc>`ela)<Esc>
"re-indendts the next line after a change -- give a count if needed. 
nnoremap <localleader>i Ji<CR><c-c>
"go back to where you have marked as w(orking point)
nnoremap <localleader>b `wzz20<c-e>
