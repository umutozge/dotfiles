for i in range(1,argc())
	let s:bufn = bufname(i)
	execute "e " . s:bufn 
	normal ggVGy
	let s:bufn = bufname(i)
	let s:newbfn = substitute(bufname(i),'txt','text','g')
	execute "tabedit " . s:newbfn 
	normal pggdd
	execute 'wq'
endfor
