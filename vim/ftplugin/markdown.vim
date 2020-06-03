
" comment region

vnoremap <buffer> <localleader>c Ombova-->`bi<!---

inoremap <buffer> <localleader>t ``<Esc>i
noremap <buffer> <localleader>t i ``<Esc>i
noremap <buffer> <localleader>,t o```bash<Return>```<Esc>ko

noremap <buffer> <localleader>k  o```sql<Return><Return>```<Esc>k:set paste<Return>"+p:set nopaste<Return>

"noremap <buffer> <localleader>,k  o```sql<Return><Return>```<Esc>ki<C-A><C-]>

noremap <buffer> <localleader>,k i```sql^M^M```^[



noremap <buffer> <localleader>d V/```<Return>k:s/.*> //g<Return>  
