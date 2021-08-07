;#!/usr/bin/sbcl --script
       

(load "/home/umut/bin/lisp/aux.lisp")


(defun command-line ()
  (or 
	#+CLISP *args*
	#+SBCL *posix-argv*
	#+LISPWORKS system:*line-arguments-list*
	#+CMU extensions:*command-line-words*
	nil))

(defun main ()
  (let* ((cl (command-line))
         (inputfile (caddr cl))
         (outfile (aux:string-to-pathname inputfile ".tex"))
       
         (proc (case (read-from-string (cadr cl))
                 (qtree #'aux:tree2qtree)
                 (avm #'aux:tree2avm))))
    (aux:write-string-to-file
      (apply #'concatenate
             'string
             (mapcar
               proc
               (aux:read-from-file inputfile)))
      outfile)))

(main)
