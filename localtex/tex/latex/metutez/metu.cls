%%
%% This is file `report.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% classes.dtx  (with options: `report')
%% 
%% This is a generated file.
%% 
%% Copyright 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004
%% The LaTeX3 Project and any individual authors listed elsewhere
%% in this file.
%% 
%% This file was generated from file(s) of the LaTeX base system.
%% --------------------------------------------------------------
%% 
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%% 
%% This file has the LPPL maintenance status "maintained".
%% 
%% This file may only be distributed together with a copy of the LaTeX
%% base system. You may however distribute the LaTeX base system without
%% such generated files.
%% 
%% The list of all files belonging to the LaTeX base distribution is
%% given in the file `manifest.txt'. See also `legal.txt' for additional
%% information.
%% 
%% The list of derived (unpacked) files belonging to the distribution
%% and covered by LPPL is defined by the unpacking scripts (with
%% extension .ins) which are part of the distribution.
%% \CharacterTable
%%  {Upper-case    \A\B\C\D\E\F\G\H\I\J\K\L\M\N\O\P\Q\R\S\T\U\V\W\X\Y\Z
%%   Lower-case    \a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z
%%   Digits        \0\1\2\3\4\5\6\7\8\9
%%   Exclamation   \!     Double quote  \"     Hash (number) \#
%%   Dollar        \$     Percent       \%     Ampersand     \&
%%   Acute accent  \'     Left paren    \(     Right paren   \)
%%   Asterisk      \*     Plus          \+     Comma         \,
%%   Minus         \-     Point         \.     Solidus       \/
%%   Colon         \:     Semicolon     \;     Less than     \<
%%   Equals        \=     Greater than  \>     Question mark \?
%%   Commercial at \@     Left bracket  \[     Backslash     \\
%%   Right bracket \]     Circumflex    \^     Underscore    \_
%%   Grave accent  \`     Left brace    \{     Vertical bar  \|
%%   Right brace   \}     Tilde         \~}
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{metu}
              [2007/07/17 1.2
METU thesis class derived from Standard LaTeX document class `report']
\newcommand\@ptsize{}
\newif\if@restonecol
\newif\if@titlepage
\@titlepagetrue
\newif\if@doublespacing
\@doublespacingfalse
\newif\if@openright
\if@compatibility\else
\DeclareOption{a4paper}
   {\setlength\paperheight {297mm}%
    \setlength\paperwidth  {210mm}}
\DeclareOption{a5paper}
   {\setlength\paperheight {210mm}%
    \setlength\paperwidth  {148mm}}
\DeclareOption{b5paper}
   {\setlength\paperheight {250mm}%
    \setlength\paperwidth  {176mm}}
\DeclareOption{letterpaper}
   {\setlength\paperheight {11in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{legalpaper}
   {\setlength\paperheight {14in}%
    \setlength\paperwidth  {8.5in}}
\DeclareOption{executivepaper}
   {\setlength\paperheight {10.5in}%
    \setlength\paperwidth  {7.25in}}
\DeclareOption{landscape}
   {\setlength\@tempdima   {\paperheight}%
    \setlength\paperheight {\paperwidth}%
    \setlength\paperwidth  {\@tempdima}}
\fi
\if@compatibility
  \renewcommand\@ptsize{0}
\else
\DeclareOption{10pt}{\renewcommand\@ptsize{0}}
\fi
\DeclareOption{11pt}{\renewcommand\@ptsize{1}}
\DeclareOption{12pt}{\renewcommand\@ptsize{2}}
\if@compatibility\else
\DeclareOption{oneside}{\@twosidefalse \@mparswitchfalse}
\fi
\DeclareOption{twoside}{\@twosidetrue  \@mparswitchtrue}
\DeclareOption{draft}{\setlength\overfullrule{5pt}}
\if@compatibility\else
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\fi
\DeclareOption{titlepage}{\@titlepagetrue}
\if@compatibility\else
\DeclareOption{notitlepage}{\@titlepagefalse}
\fi
\DeclareOption{doublespacing}{\@doublespacingtrue}
\if@compatibility\else
\DeclareOption{onehalfspacing}{\@doublespacingfalse}
\fi
\if@compatibility
\else
\DeclareOption{openright}{\@openrighttrue}
\DeclareOption{openany}{\@openrightfalse}
\fi
\if@compatibility\else
\DeclareOption{onecolumn}{\@twocolumnfalse}
\fi
\DeclareOption{twocolumn}{\@twocolumntrue}
\DeclareOption{leqno}{\input{leqno.clo}}
\DeclareOption{fleqn}{\input{fleqn.clo}}
\DeclareOption{openbib}{%
  \AtEndOfPackage{%
   \renewcommand\@openbib@code{%
      \advance\leftmargin\bibindent
      \itemindent -\bibindent
      \listparindent \itemindent
      \parsep \z@
      }%
   \renewcommand\newblock{\par}}%
}
\ExecuteOptions{a4paper,12pt,onehalfspacing,oneside,onecolumn,final,openany}
\ProcessOptions
\input{size1\@ptsize.clo}
\setlength\lineskip{1\p@}
\setlength\normallineskip{1\p@}
\renewcommand\baselinestretch{}
\if@doublespacing
\renewcommand\baselinestretch{2}
\else
\renewcommand\baselinestretch{1.5}
\fi
\setlength\parskip{0\p@ \@plus \p@}
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301
\setcounter{topnumber}{2}
\renewcommand\topfraction{.7}
\setcounter{bottomnumber}{1}
\renewcommand\bottomfraction{.3}
\setcounter{totalnumber}{3}
\renewcommand\textfraction{.2}
\renewcommand\floatpagefraction{.5}
\setcounter{dbltopnumber}{2}
\renewcommand\dbltopfraction{.7}
\renewcommand\dblfloatpagefraction{.5}
\if@twoside
  \def\ps@headings{%
      \let\@oddfoot\@empty\let\@evenfoot\@empty
      \def\@evenhead{\thepage\hfil\slshape\leftmark}%
      \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
      \let\@mkboth\markboth
    \def\chaptermark##1{%
      \markboth {\MakeUppercase{%
        \ifnum \c@secnumdepth >\m@ne
            \@chapapp\ \thechapter. \ %
        \fi
        ##1}}{}}%
    \def\sectionmark##1{%
      \markright {\MakeUppercase{%
        \ifnum \c@secnumdepth >\z@
          \thesection. \ %
        \fi
        ##1}}}}
\else
  \def\ps@headings{%
    \let\@oddfoot\@empty
    \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
    \let\@mkboth\markboth
    \def\chaptermark##1{%
      \markright {\MakeUppercase{%
        \ifnum \c@secnumdepth >\m@ne
            \@chapapp\ \thechapter. \ %
        \fi
        ##1}}}}
\fi
\def\ps@myheadings{%
    \let\@oddfoot\@empty\let\@evenfoot\@empty
    \def\@evenhead{\thepage\hfil\slshape\leftmark}%
    \def\@oddhead{{\slshape\rightmark}\hfil\thepage}%
    \let\@mkboth\@gobbletwo
    \let\chaptermark\@gobble
    \let\sectionmark\@gobble
    }
  \if@titlepage
  \newcommand\maketitle{\begin{titlepage}%
  \let\footnotesize\small
  \let\footnoterule\relax
  \let \footnote \thanks
  \null\vfil
  \vskip 60\p@
  \begin{center}%
    {\LARGE \@title \par}%
    \vskip 3em%
    {\large
     \lineskip .75em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
      \vskip 1.5em%
    {\large \@date \par}%       % Set date in \large size.
  \end{center}\par
  \@thanks
  \vfil\null
  \end{titlepage}%
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}
\else
\newcommand\maketitle{\par
  \begingroup
    \renewcommand\thefootnote{\@fnsymbol\c@footnote}%
    \def\@makefnmark{\rlap{\@textsuperscript{\normalfont\@thefnmark}}}%
    \long\def\@makefntext##1{\parindent 1em\noindent
            \hb@xt@1.8em{%
                \hss\@textsuperscript{\normalfont\@thefnmark}}##1}%
    \if@twocolumn
      \ifnum \col@number=\@ne
        \@maketitle
      \else
        \twocolumn[\@maketitle]%
      \fi
    \else
      \newpage
      \global\@topnum\z@   % Prevents figures from going at top of page.
      \@maketitle
    \fi
    \thispagestyle{plain}\@thanks
  \endgroup
  \setcounter{footnote}{0}%
  \global\let\thanks\relax
  \global\let\maketitle\relax
  \global\let\@maketitle\relax
  \global\let\@thanks\@empty
  \global\let\@author\@empty
  \global\let\@date\@empty
  \global\let\@title\@empty
  \global\let\title\relax
  \global\let\author\relax
  \global\let\date\relax
  \global\let\and\relax
}
\def\@maketitle{%
  \newpage
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\LARGE \@title \par}%
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@author
      \end{tabular}\par}%
    \vskip 1em%
    {\large \@date}%
  \end{center}%
  \par
  \vskip 1.5em}
\fi
\newcommand*\chaptermark[1]{}
\setcounter{secnumdepth}{2}
\newcounter {part}
\newcounter {chapter}
\newcounter {section}[chapter]
\newcounter {subsection}[section]
\newcounter {subsubsection}[subsection]
\newcounter {paragraph}[subsubsection]
\newcounter {subparagraph}[paragraph]
\renewcommand \thepart {\@Roman\c@part}
\renewcommand \thechapter {\@arabic\c@chapter}
\renewcommand \thesection {\thechapter.\@arabic\c@section}
\renewcommand\thesubsection   {\thesection.\@arabic\c@subsection}
\renewcommand\thesubsubsection{\thesubsection .\@arabic\c@subsubsection}
\renewcommand\theparagraph    {\thesubsubsection.\@arabic\c@paragraph}
\renewcommand\thesubparagraph {\theparagraph.\@arabic\c@subparagraph}
\newcommand\@chapapp{\chaptername}
\newcommand\part{%
  \if@openright
    \cleardoublepage
  \else
    \clearpage
  \fi
  \thispagestyle{plain}%
  \if@twocolumn
    \onecolumn
    \@tempswatrue
  \else
    \@tempswafalse
  \fi
  \null\vfil
  \secdef\@part\@spart}

\def\@part[#1]#2{%
    \ifnum \c@secnumdepth >-2\relax
      \refstepcounter{part}%
      \addcontentsline{toc}{part}{\thepart\hspace{1em}#1}%
    \else
      \addcontentsline{toc}{part}{#1}%
    \fi
    \markboth{}{}%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \ifnum \c@secnumdepth >-2\relax
       \huge\bfseries \partname\nobreakspace\thepart
       \par
       \vskip 20\p@
     \fi
     \Huge \bfseries #2\par}%
    \@endpart}
\def\@spart#1{%
    {\centering
     \interlinepenalty \@M
     \normalfont
     \Huge \bfseries #1\par}%
    \@endpart}
\def\@endpart{\vfil\newpage
              \if@twoside
               \if@openright
                \null
                \thispagestyle{empty}%
                \newpage
               \fi
              \fi
              \if@tempswa
                \twocolumn
              \fi}
\newcommand\chapter{\if@openright\cleardoublepage\else\clearpage\fi
                    \thispagestyle{plain}%
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
                         \refstepcounter{chapter}%
                         \typeout{\@chapapp\space\thechapter.}%
                         \addcontentsline{toc}{chapter}%
                                   {\protect\numberline{\thechapter}#1}%
                    \else
                      \addcontentsline{toc}{chapter}{#1}%
                    \fi
                    \chaptermark{#1}%
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@topnewpage[\@makechapterhead{#2}]%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}
\def\@makechapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \raggedright \normalfont
    \ifnum \c@secnumdepth >\m@ne
	\centerline{\Large\bfseries\@chapapp\space \thechapter}
        \par\nobreak
        \vskip 20\p@
    \fi
    \interlinepenalty\@M
	\begin{center}
    \Large\bfseries\uppercase{#1}\par\nobreak%umut huge-> Large
	\end{center}
    \vskip 40\p@
  }}
\def\@schapter#1{\if@twocolumn
                   \@topnewpage[\@makeschapterhead{#1}]%
                 \else
                   \@makeschapterhead{#1}%
                   \@afterheading
                 \fi}
\def\@makeschapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \raggedright
    \normalfont
    \interlinepenalty\@M
    \begin{center}\huge \bfseries\uppercase{#1}\end{center}\par\nobreak
    \vskip 40\p@
  }}
\newcommand\section{\@startsection {section}{1}{\z@}%
                                   {-3.5ex \@plus -1ex \@minus -.2ex}%
                                   {2.3ex \@plus.2ex}%
                                   {\normalfont\Large\bfseries}}
\newcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\large\bfseries}}
\newcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-3.25ex\@plus -1ex \@minus -.2ex}%
                                     {1.5ex \@plus .2ex}%
                                     {\normalfont\normalsize\bfseries}}
\newcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {3.25ex \@plus1ex \@minus.2ex}%
                                    {-1em}%
                                    {\normalfont\normalsize\bfseries}}
\newcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}%
                                       {3.25ex \@plus1ex \@minus .2ex}%
                                       {-1em}%
                                      {\normalfont\normalsize\bfseries}}
\if@twocolumn
  \setlength\leftmargini  {2em}
\else
  \setlength\leftmargini  {2.5em}
\fi
\leftmargin  \leftmargini
\setlength\leftmarginii  {2.2em}
\setlength\leftmarginiii {1.87em}
\setlength\leftmarginiv  {1.7em}
\if@twocolumn
  \setlength\leftmarginv  {.5em}
  \setlength\leftmarginvi {.5em}
\else
  \setlength\leftmarginv  {1em}
  \setlength\leftmarginvi {1em}
\fi
\setlength  \labelsep  {.5em}
\setlength  \labelwidth{\leftmargini}
\addtolength\labelwidth{-\labelsep}
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
\renewcommand\theenumi{\@arabic\c@enumi}
\renewcommand\theenumii{\@alph\c@enumii}
\renewcommand\theenumiii{\@roman\c@enumiii}
\renewcommand\theenumiv{\@Alph\c@enumiv}
\newcommand\labelenumi{\theenumi.}
\newcommand\labelenumii{(\theenumii)}
\newcommand\labelenumiii{\theenumiii.}
\newcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\theenumi(\theenumii)}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
\newcommand\labelitemi{\textbullet}
\newcommand\labelitemii{\normalfont\bfseries \textendash}
\newcommand\labelitemiii{\textasteriskcentered}
\newcommand\labelitemiv{\textperiodcentered}
\newenvironment{description}
               {\list{}{\labelwidth\z@ \itemindent-\leftmargin
                        \let\makelabel\descriptionlabel}}
               {\endlist}
\newcommand*\descriptionlabel[1]{\hspace\labelsep
                                \normalfont\bfseries #1}
\if@titlepage
  \newenvironment{abstract}{%
      \titlepage
      \null\vfil
      \@beginparpenalty\@lowpenalty
      \begin{center}%
        \bfseries \abstractname
        \@endparpenalty\@M
      \end{center}}%
     {\par\vfil\null\endtitlepage}
\else
  \newenvironment{abstract}{%
      \if@twocolumn
        \section*{\abstractname}%
      \else
        \small
        \begin{center}%
          {\bfseries \abstractname\vspace{-.5em}\vspace{\z@}}%
        \end{center}%
        \quotation
      \fi}
      {\if@twocolumn\else\endquotation\fi}
\fi
\newenvironment{verse}
               {\let\\\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -1.5em%
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin 1.5em}%
                \item\relax}
               {\endlist}
\newenvironment{quotation}
               {\list{}{\listparindent 1.5em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                \item\relax}
               {\endlist}
\newenvironment{quote}
               {\list{}{\rightmargin\leftmargin}%
                \item\relax}
               {\endlist}
\if@compatibility
\newenvironment{titlepage}
    {%
      \if@twocolumn
        \@restonecoltrue\onecolumn
      \else
        \@restonecolfalse\newpage
      \fi
      \thispagestyle{empty}%
      \setcounter{page}\z@
    }%
    {\if@restonecol\twocolumn \else \newpage \fi
    }
\else
\newenvironment{titlepage}
    {%
      \if@twocolumn
        \@restonecoltrue\onecolumn
      \else
        \@restonecolfalse\newpage
      \fi
      \thispagestyle{empty}%
      \setcounter{page}\@ne
    }%
    {\if@restonecol\twocolumn \else \newpage \fi
     \if@twoside\else
        \setcounter{page}\@ne
     \fi
    }
\fi
\newcommand\appendix{\par
  \setcounter{chapter}{0}%
  \setcounter{section}{0}%
  \gdef\@chapapp{\appendixname}%
  \gdef\thechapter{\@Alph\c@chapter}}
\setlength\arraycolsep{5\p@}
\setlength\tabcolsep{6\p@}
\setlength\arrayrulewidth{.4\p@}
\setlength\doublerulesep{2\p@}
\setlength\tabbingsep{\labelsep}
\skip\@mpfootins = \skip\footins
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}
\@addtoreset {equation}{chapter}
\renewcommand\theequation
  {\ifnum \c@chapter>\z@ \thechapter.\fi \@arabic\c@equation}
\newcounter{figure}[chapter]
\renewcommand \thefigure
     {\figurename\nobreakspace\ifnum \c@chapter>\z@ \thechapter.\fi \@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\thefigure}
%\def\fnum@figure{\figurename\nobreakspace\thefigure}
\newenvironment{figure}
               {\@float{figure}}
               {\end@float}
\newenvironment{figure*}
               {\@dblfloat{figure}}
               {\end@dblfloat}
\newcounter{table}[chapter]
\renewcommand \thetable
     {\tablename\nobreakspace\ifnum \c@chapter>\z@ \thechapter.\fi\@arabic\c@table}
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
%\def\fnum@table{\tablename\nobreakspace\thetable}
\def\fnum@table{\thetable}
\newenvironment{table}
               {\@float{table}}
               {\end@float}
\newenvironment{table*}
               {\@dblfloat{table}}
               {\end@dblfloat}
\newlength\abovecaptionskip
\newlength\belowcaptionskip
\setlength\abovecaptionskip{0\p@}
\setlength\belowcaptionskip{0\p@}
\long\def\@makecaption#1#2{%
  \vskip\abovecaptionskip
  \sbox\@tempboxa{#1: #2}%
  \ifdim \wd\@tempboxa >\hsize
    #1: #2\par
  \else
    \global \@minipagefalse
    \hb@xt@\hsize{\hfil\box\@tempboxa\hfil}%
  \fi
  \vskip\belowcaptionskip}
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareRobustCommand*\cal{\@fontswitch\relax\mathcal}
\DeclareRobustCommand*\mit{\@fontswitch\relax\mathnormal}
\newcommand\@pnumwidth{1.55em}
\newcommand\@tocrmarg{2.55em}
\newcommand\@dotsep{4.5}
\setcounter{tocdepth}{2}
\newcommand\tableofcontents{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\contentsname
        \@mkboth{%
           \MakeUppercase\contentsname}{\MakeUppercase\contentsname}}%
    \addcontentsline{toc}{leads}{\protect\numberline {}TABLE OF CONTENTS}%
    \@starttoc{toc}%
    \if@restonecol\twocolumn\fi
    }
\newcommand*\l@part[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{2.25em \@plus\p@}%
    \setlength\@tempdima{3em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      {\leavevmode
       \large \bfseries #1\hfil \hb@xt@\@pnumwidth{\hss #2}}\par
       \nobreak
         \global\@nobreaktrue
         \everypar{\global\@nobreakfalse\everypar{}}%
    \endgroup
  \fi}
\newcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1.0em \@plus\p@
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode \bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}
%\newcommand*\l@section{\@dottedtocline{1}{1.5em}{2.3em}}
%\newcommand*\l@subsection{\@dottedtocline{2}{3.8em}{3.2em}}
%\newcommand*\l@subsubsection{\@dottedtocline{3}{7.0em}{4.1em}}
%\newcommand*\l@paragraph{\@dottedtocline{4}{10em}{5em}}
%\newcommand*\l@subparagraph{\@dottedtocline{5}{12em}{6em}}
\newcommand*\l@section{\@dottedtocline{1}{3em}{2.3em}}
\newcommand*\l@subsection{\@dottedtocline{2}{4.5em}{3.2em}}
\newcommand*\l@subsubsection{\@dottedtocline{3}{6.0em}{4.1em}}
\newcommand*\l@paragraph{\@dottedtocline{4}{7.5em}{5em}}
\newcommand*\l@subparagraph{\@dottedtocline{5}{9em}{6em}}
\newcommand\listoffigures{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listfigurename}%
    \addcontentsline{toc}{leads}{\protect\numberline {}LIST OF FIGURES}%
      \@mkboth{\MakeUppercase\listfigurename}%
              {\MakeUppercase\listfigurename}%
    \@starttoc{lof}%
    \if@restonecol\twocolumn\fi
    }
\newcommand*\l@figure{\@dottedtocline{1}{1.5em}{5.2em}}
\newcommand\listoftables{%
    \if@twocolumn
      \@restonecoltrue\onecolumn
    \else
      \@restonecolfalse
    \fi
    \chapter*{\listtablename}%
    \addcontentsline{toc}{leads}{\protect\numberline {}LIST OF TABLES}%
      \@mkboth{%
          \MakeUppercase\listtablename}%
         {\MakeUppercase\listtablename}%
    \@starttoc{lot}%
    \if@restonecol\twocolumn\fi
    }
\newcommand*\l@table{\@dottedtocline{1}{1.5em}{4.7em}}
%\let\l@table\l@figure
\newdimen\bibindent
\setlength\bibindent{1.5em}
\newenvironment{thebibliography}[1]
     {\chapter*{\bibname}%
     \addcontentsline{toc}{leads}{\protect\numberline {}\bibname}
      \@mkboth{\MakeUppercase\bibname}{\MakeUppercase\bibname}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\newcommand\newblock{\hskip .11em\@plus.33em\@minus.07em}
\let\@openbib@code\@empty
\newenvironment{theindex}
               {\if@twocolumn
                  \@restonecolfalse
                \else
                  \@restonecoltrue
                \fi
                \twocolumn[\@makeschapterhead{\indexname}]%
                \@mkboth{\MakeUppercase\indexname}%
                        {\MakeUppercase\indexname}%
                \thispagestyle{plain}\parindent\z@
                \parskip\z@ \@plus .3\p@\relax
                \columnseprule \z@
                \columnsep 35\p@
                \let\item\@idxitem}
               {\if@restonecol\onecolumn\else\clearpage\fi}
\newcommand\@idxitem{\par\hangindent 40\p@}
\newcommand\subitem{\@idxitem \hspace*{20\p@}}
\newcommand\subsubitem{\@idxitem \hspace*{30\p@}}
\newcommand\indexspace{\par \vskip 10\p@ \@plus5\p@ \@minus3\p@\relax}
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule\@width.4\columnwidth
  \kern2.6\p@}
\@addtoreset{footnote}{chapter}
\newcommand\@makefntext[1]{%
    \parindent 1em%
    \noindent
    \hb@xt@1.8em{\hss\@makefnmark}#1}
\newcommand\contentsname{\Large TABLE OF CONTENTS}
\newcommand\listfigurename{\Large LIST OF FIGURES}
\newcommand\listtablename{\Large LIST OF TABLES}
\newcommand\bibname{\Large REFERENCES}
\newcommand\indexname{Index}
\newcommand\figurename{Figure}
\newcommand\tablename{Table}
\newcommand\partname{Part}
\newcommand\chaptername{\Large CHAPTER}
\newcommand\appendixname{Appendix}
\newcommand\abstractname{Abstract}
\def\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
\setlength\columnsep{10\p@}
\setlength\columnseprule{0\p@}
\pagestyle{plain}
\pagenumbering{arabic}
\if@twoside
\else
  \raggedbottom
\fi
\if@twocolumn
  \twocolumn
  \sloppy
  \flushbottom
\else
  \onecolumn
\fi
%%
%% metu specific commands
%%

%% set margins to 4cm left 2.5cm others
\newlength{\@tmpdimension}
\setlength{\oddsidemargin}{4cm}
\if@twoside
	\setlength{\evensidemargin}{2.5cm}
\else
	\setlength{\evensidemargin}{4cm}
\fi
\setlength{\topmargin}{25mm}
\setlength{\@tmpdimension}{\paperwidth}
\addtolength{\@tmpdimension}{-57mm}
\setlength{\textwidth}{\@tmpdimension}
\setlength{\@tmpdimension}{\paperheight}
\addtolength{\@tmpdimension}{-45mm}
\addtolength{\@tmpdimension}{-\footskip}
\setlength{\textheight}{\@tmpdimension}

\addtolength{\evensidemargin}{-32mm}
\addtolength{\oddsidemargin}{-32mm}
\addtolength{\topmargin}{-30mm}
\addtolength{\topmargin}{-\headheight}
\addtolength{\topmargin}{-\headsep}
\setlength{\textfloatsep}{3em \@plus 1em \@minus 0em}
\setlength{\intextsep}{3em \@plus 1em \@minus 0em}

\newcommand{\restore@spacing}{%
  \endgroup
  \if@doublespacing
    \renewcommand\baselinestretch{2}
  \else
    \renewcommand\baselinestretch{1.5}
  \fi
  \@currsize
}

\newenvironment{singlespace}{%
  \begingroup
    \renewcommand{\baselinestretch}{1} 
    \@currsize
}{%
  \restore@spacing
}

% one and a half spacing is 1.5 x pt size
\newenvironment{onehalfspace}{%
  \begingroup
    \renewcommand{\baselinestretch}{1.5}
    \@currsize
}{%
  \restore@spacing
}

\def\singlespacing{\renewcommand{\baselinestretch}{1}\@currsize}
\def\oneandhalfspacing{\renewcommand{\baselinestretch}{1.5}\@currsize}

% double spacing is 2 x pt size
\newenvironment{doublespace}{%
  \begingroup
    \renewcommand\baselinestretch{2}
    \@currsize
}{%
  \restore@spacing
}

%%%%%%%%%%%% Preample definitions %%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\def\@graduateschool{}\def\graduateschool#1{\def\@graduateschool{#1}}
\def\@department{}\def\department#1{\def\@department{#1}}
\def\@tdepartment{}\def\turkishdepartment#1{\def\@tdepartment{#1}}
\def\@degree{}\def\degree#1{\def\@degree{#1}}
\def\@tdegree{}\def\turkishdegree#1{\def\@tdegree{#1}}
\def\@shortdegree{}\def\shortdegree#1{\def\@shortdegree{#1}}
\def\@ttitle{}\def\turkishtitle#1{\def\@ttitle{#1}}
\def\@director{} \def\director#1{\def\@director{#1}}
\def\@headofdept{} \def\headofdept#1{\def\@headofdept{#1}}
\newif\ifexist@co \exist@cofalse
\def\@cosupervisor{} \def\@cosupervisoraff{} 
\def\cosupervisor#1#2{\def\@cosupervisor{#1}%
	\def\@cosupervisoraff{#2} \exist@cotrue}
\def\@supervisor{} \def\@supervisoraff{}
\def\supervisor#1#2{\def\@supervisor{#1}\def\@supervisoraff{#2}}
\def\@turkishcosupervisor{}\def\@turkishcosupervisoraff {}
\def\turkishcosupervisor#1#2{\def\@turkishcosupervisor{#1}%
	\def\@turkishcosupervisoraff{#2} \exist@cotrue}
\def\@turkishsupervisor{} \def\@turkishsupervisoraff{}
\def\turkishsupervisor#1#2{\def\@turkishsupervisor{#1}%
	\def\@turkishsupervisoraff{#2}}
\def\@keywords{} \def\keywords#1{\def\@keywords{#1}}
\def\@anahtarklm{} \def\anahtarklm#1{\def\@anahtarklm{#1}}
\def\turkishdate#1{\def\@tdate{#1}}

%\def\@prelimsize{\@setsize\@prelimsize{14pt}\xiipt\@xiipt
%\let\currentsize=\@prelimsize}
\def\@prelimsize{\@setfontsize\@prelimsize\@xiipt{14}
\let\currentsize=\@prelimsize}
\newtoks\@last \newtoks\@name
\def\i@uthor#1 #2.mend{\def\paramtw@{#2}\ifx\paramtw@\empty\@last={#1}%
\else\ifx\t@r\empty\@name={#1}\def\t@r{t@r}\else%
\@name=\expandafter{\the\@name{} #1}\fi\i@uthor#2.mend\fi}
\def\inv@uthor#1{\def\t@r{}\@name={}\@last={}\i@uthor#1 .mend%
\expthr@@{\the\@last}, \expthr@@{\the\@name}}

\def\TRUppercase#1{\uccode`i=`^^9d%
	\MakeUppercase{#1}}%

%%%%%%%%%%%%%%%%%%% Title page %%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewenvironment{titlepage}{\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \else \newpage \fi \@prelimsize 
 \pagestyle{empty}}
{\if@restonecol\twocolumn \else \newpage \fi
 \pagestyle{plain}\normalsize}
\def\maketitle{\begin{titlepage}
\let\footnotesize\small \let\footnoterule\relax \setcounter{page}{1}
\null \nointerlineskip
\vskip -1.2cm 
%\vskip -2.2cm 
\begin{center} \nointerlineskip
 \vbox{\begin{singlespace}\uppercase\expandafter{\@title}\end{singlespace}}
\vskip 4.5cm plus0pt minus1cm \nointerlineskip
 \begin{singlespace}\vbox{A THESIS SUBMITTED TO \\
       THE GRADUATE SCHOOL OF \uppercase\expandafter{\@graduateschool}\\
       OF \\ THE MIDDLE EAST TECHNICAL UNIVERSITY}\end{singlespace}
\vskip 2.35cm plus0pt minus2mm \nointerlineskip
 \vbox{BY}
\vskip 2.35cm plus0pt minus2mm \nointerlineskip
 \vbox{\TRUppercase{\@author}}
\vskip 3.5cm plus0pt minus1cm \nointerlineskip
% \begin{singlespace}
 \vbox{
       \mbox{IN PARTIAL FULFILLMENT OF THE REQUIREMENTS}
       FOR
       THE DEGREE OF \uppercase\expandafter{\@degree} \\
       IN \\THE DEPARTMENT OF 
       \uppercase\expandafter{\@department}}
% \end{singlespace}
\vskip 4cm plus0pt minus1cm \nointerlineskip
 \vbox{\uppercase\expandafter{\@date}} \end{center}
\end{titlepage}
\setcounter{footnote}{0} \let\thanks\relax
\gdef\@thanks{}\let\maketitle\relax}

%%%%%%%%%%%%
\def\expthr@@#1{\expandafter #1}
\def\uplowcase#1{#1}

\def\compare#1{
	
}
% \def\@makemembersigof#1{
% 	\@makemembersig{\csname @committeemember#1\endcsname}%
% 	{\csname @committeemember#1aff\endcsname}
% }

\def\@makemembersigof#1{
	\@mymembersigf{\csname @committeemember#1\endcsname}%
	{\csname @committeemember#1aff\endcsname}
}

\def\@makemembersig#1#2{\vbox{\hbox to \textwidth{%
	\vtop{\hbox{\expthr@@{#1}}\hbox spread -4cm {#2}}
	\hfill \rule{50mm}{1pt}}}}

% \def\@mymembersig#1#2{\vbox{\rule{50mm}{1pt}\\
%  #1\\
% \hfill#2\hfill}}
\def\@mymembersig#1#2{\begin{tabular}[t]{c}
\rule{50mm}{1pt}\\
#1\\
#2
\end{tabular}
}

\def\@mymembersigf#1#2{
#1 \hfill (#2)~~~\rule{50mm}{1pt}\\
}

\def\@tmakedef#1#2{\expandafter\xdef\csname #1\endcsname{#2}}
\def\committeemember#1#2#3{%
	\@tmakedef{@committeemember#1}{#2}
	\@tmakedef{@committeemember#1aff}{#3}
}

%%%%%%%%%%%%%%%% New approval page %%%%%%%%%%%%%%%%%%%%%%%%%%%
\newenvironment{newapprovalpage}%
	{\renewcommand{\thefootnote}{\fnsymbol{footnote}}
	\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 	\else \newpage \fi \@prelimsize 
	\pagestyle{empty}\let\footnoterule\relax
 	\begin{singlespace}}%
	{\if@restonecol\twocolumn \else \newpage \fi
	\pagestyle{plain}\end{singlespace}\normalsize}

\def\makenewapproval{\begin{newapprovalpage}\let\footnotesize\normalsize \parskip \z@
\topsep \z@ \partopsep \z@ \parsep \z@ \itemsep \z@
\null \nointerlineskip \parindent=0pt
\vskip 0.2cm \nointerlineskip
% \vbox{\centering Approval of the thesis}
%\vskip8mm plus0pt minus2mm \nointerlineskip
% \vbox{\centering ``\textbf{\uppercase\expandafter{\@title}}''}
%\vskip15mm plus0pt minus2mm \nointerlineskip
% \vbox{submitted by \ \textbf{\@author} \ in partial fullfillment of 
% the requirements for the degree of \ \textbf{\@degree \  in \ \@department}
% \ by,}
\vbox{Approval of the Graduate School of \@graduateschool}
\vskip12mm plus0pt minus2mm \nointerlineskip
\hfill\@mymembersig{\@director}{Director}

\vskip1.2cm plus0pt minus2mm \nointerlineskip
\vbox{I certify that this thesis satisfies all the requirements as a
thesis for the degree of \@degree.}

\vskip14mm plus0pt minus2mm \nointerlineskip
\hfill\@mymembersig{\@headofdept}{Head of Department}

\vskip1.2cm plus0pt minus2mm \nointerlineskip

\vbox{This is to certify that we have read this thesis and that in our
opinion it is fully adequate, in scope and quality, as a thesis for
the degree of \@degree.}

\vskip14mm plus0pt minus2mm \nointerlineskip


\ifexist@co \vskip10mm plus0pt minus2mm \nointerlineskip


    \@mymembersig{\@cosupervisor}{Co-supervisor}  \hfill \@mymembersig{\@supervisor}{Supervisor}
\else \hfill \@mymembersig{\@supervisor}{Supervisor}
\vskip9mm plus0pt minus2mm \nointerlineskip
\fi

\vskip12mm plus0pt minus2mm \nointerlineskip
 \vbox{{Examining Committee Members:}}
\vskip10mm plus0pt minus2mm \nointerlineskip
\@makemembersigof{i}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@mymembersigf{\@supervisor}{\@supervisoraff}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersigof{ii}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersigof{iii}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersigof{iv}
\vskip8mm plus0pt minus2mm \nointerlineskip
%\vbox{\hfill\hbox{Date:}\hskip 2em \rule{50mm}{1pt}}
\end{newapprovalpage}
\gdef\@director{}\let\director\relax
\gdef\@headofdept{}\let\headofdept\relax
\gdef\@degree{}\let\degree\relax
\gdef\@committeememberi{}\let\committeememberi\relax
\gdef\@committeememberii{}\let\committeememberii\relax
\gdef\@committeememberiii{}\let\committeememberiii\relax
\gdef\@committeememberiv{}\let\committeememberiv\relax
\gdef\@graduateschool{}\let\graduateschool\relax \let\makeapproval\relax}


%%%%%%%%%%%%%%%% Approval page %%%%%%%%%%%%%%%%%%%%%%%%%%%
\def\approvalpage{\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \else \newpage \fi \@prelimsize \pagestyle{empty}\begin{singlespace}}
\def\endapprovalpage{\if@restonecol\twocolumn \else \newpage \fi
\pagestyle{plain}\end{singlespace}\normalsize}

\def\makeapproval{\begin{approvalpage} \parskip \z@
\topsep \z@ \partopsep \z@ \parsep \z@ \itemsep \z@
\null \nointerlineskip \parindent=0pt
\vskip 0.2cm \nointerlineskip
 \vbox{Approval of the Graduate School of \@graduateschool.}
\vskip2.0cm plus0pt minus2mm \nointerlineskip
\vbox{\parbox[t]{1cm}{} \hfill
      \parbox[t]{5.5cm}{\begin{center}
      \rule{5.5cm}{1pt} \\
      \expthr@@{\@director}\\
      Director \end{center}\nointerlineskip}}
\vskip1.6cm \@plus0pt \@minus4mm \nointerlineskip%
 \vbox{I certify that this thesis satisfies all the requirements as a
     thesis for the degree of \@degree.}
\vskip2.0cm plus0pt minus2mm \nointerlineskip
 \vbox{\parbox{1cm}{} \hfill \parbox{6cm}{\begin{center}
                      \rule{6cm}{1pt} \\
                      \expthr@@{\@headofdept}
                      \\ Head of Department\end{center}\nointerlineskip}}
\vskip1.0cm \@plus0pt \@minus4mm \nointerlineskip
 \vbox{This is to certify that we have read this thesis and that in our
       opinion it is fully adequate, in scope and quality, as a thesis for
       the degree of \@degree.}
\nointerlineskip \vskip1.8cm plus0pt minus2mm
 \vbox{\ifexist@co \parbox[t]{6cm}{\begin{center}
                   \rule{6cm}{1pt} \\ \expthr@@{\@cosupervisor}\\
                   Co-Supervisor \end{center}\nointerlineskip}
       \else \parbox{1cm}{}\fi \hfill
                      \parbox[t]{6cm}{\begin{center}
                \hfill\rule{6cm}{1pt} \\ \expthr@@{\@supervisor}\\
                      Supervisor \end{center}\nointerlineskip}}
\vskip1.2cm plus0pt minus2mm \nointerlineskip
 \vbox{Examining Committee Members}
\vskip7mm plus0pt minus2mm \nointerlineskip
\@makemembersig{\@committeememberi}{\@committeememberiaff}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersig{\@supervisor}{\@supervisoraff}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersig{\@committeememberii}{\@committeememberiiaff}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersig{\@committeememberiii}{\@committeememberiiiaff}
\vskip8mm plus0pt minus2mm \nointerlineskip
\@makemembersig{\@committeememberiv}{\@committeememberivaff}
\end{approvalpage}
\gdef\@director{}\let\director\relax
\gdef\@headofdept{}\let\headofdept\relax
\gdef\@degree{}\let\degree\relax
\gdef\@committeemember1{}\let\committeemember1\relax
\gdef\@committeemember2{}\let\committeemember2\relax
\gdef\@committeemember3{}\let\committeemember3\relax
\gdef\@committeemember4{}\let\committeemember4\relax
\gdef\@committeemember5{}\let\committeemember5\relax
\gdef\@graduateschool{}\let\graduateschool\relax \let\makeapproval\relax}


%%%%%%%%%%%%%%%%%%%%%%%%%%%% ABSTRACT OZ %%%%%%%%%%%%%%%%%%%%%%%%%%

\def\abstract{\addcontentsline{toc}{leads}{\protect\numberline {}ABSTRACT}
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{\Large ABSTRACT}\@mkboth {ABSTRACT}{ABSTRACT}\parskip \z@
 \topsep \z@ \partopsep \z@ \parsep \z@ \itemsep \z@
 \begin{center}\uppercase\expandafter{\@title} \\ \vskip 0.5\baselineskip
 \expandafter\expandafter\expandafter\inv@uthor\expandafter{\@author} \\
 \@shortdegree, Department of \@department \\
Supervisor: \expthr@@{\@supervisor} \\
\ifexist@co Co-Supervisor: \expthr@@{\@cosupervisor} \\ \fi
\vskip 0.5\baselineskip \uplowcase\@date, \pageref{`@lastpage'} pages\end{center}
\vskip \baselineskip}
\def\endabstract{\vskip 0.5\baselineskip \par \noindent Keywords: \@keywords
\gdef\@keywords{}\let\keywords\relax
\gdef\@shortdegree{}\let\shortdegree\relax
\gdef\@department{}\let\department\relax
\if@restonecol \twocolumn\fi\newpage }

\def\oz{\addcontentsline{toc}{leads}{\protect\numberline {}\"{O}Z}
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{\Large \"{O}Z}\@mkboth {\"{O}Z}{\"{O}Z}\begin{center}
\TRUppercase{\@ttitle} \\ \vskip 0.5\baselineskip
 \expandafter\expandafter\expandafter\inv@uthor\expandafter{\@author} \\
 \@tdegree, \@tdepartment\ B\"{o}l\"{u}m\"{u}\\
Tez Y\"{o}neticisi: \expthr@@{\@turkishsupervisor} \\
\ifexist@co Ortak Tez Y\"{o}neticisi: \expthr@@{\@turkishcosupervisor} \\ \fi
\vskip 0.5\baselineskip\uplowcase\@tdate, \pageref{`@lastpage'} sayfa\end{center}
\vskip \baselineskip}
\def\endoz{\vskip 0.5\baselineskip \par \noindent
Anahtar Kelimeler: \@anahtarklm
\gdef\@anahtarklm{}\let\anahtarklm\relax
\gdef\@tdegree{}\let\turkishdegree\relax
\gdef\@tdepartment{}\let\turkishdepartment\relax
\gdef\@ttitle{}\let\turkishtitle\relax
\gdef\@supervisor{}\let\supervisor\relax
\gdef\@cosupervisor{}\let\cosupervisor\relax
\if@restonecol \twocolumn\fi\newpage }

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
\def\makeplagiarismpage{\@prelimsize
\mbox{}
\vfill
{\noindent\bf
I hereby declare that all information in this document has been obtained
and presented in
accordance with academic rules and ethical conduct. I also declare that, as
required by these
rules and conduct, I have fully cited and referenced all material and
results that are not
original to this work.}
\vskip 3em
\begin{flushright}
\begin{tabular}{l@{\hskip 1em:\hskip 1em}p{14em}}
Name, Last name &\@author \\[1.5em]
Signature &  \\
\end{tabular}
\end{flushright}
\vskip 12em
\normalsize
\newpage
}

\newcommand*\l@leads{\noindent\@dottedtocline{1}{0em}{0em}}
\newcommand*\l@nodots[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 0em \@plus\p@
    \setlength\@tempdima{0em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      \uppercase{#1}\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss}\par
      \penalty\@highpenalty
    \endgroup
  \fi}

\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1.0em \@plus\p@
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode
      \advance\leftskip\@tempdima
      %\hskip -\leftskip
      \uppercase{#1}\nobreak\hfil \nobreak\hb@xt@\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}


\def\dedication#1{\addcontentsline{toc}{leads}{\protect\numberline {}DEDICATON}\begin{center}\null
\vspace*{\fill}#1\vspace*{\fill}\end{center}\newpage}

\def\acknowledgments{\addcontentsline{toc}{leads}{\protect\numberline {}ACKNOWLEDGMENTS}
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
\fi\chapter*{\Large ACKNOWLEDGMENTS}\@mkboth {ACKNOWLEDGMENTS}{ACKNOWLEDGMENTS}}
\def\endacknowledgments{\if@restonecol \twocolumn\fi\newpage}

\def\glossary{\@ifnextchar[\gl@ssary{\gl@ssary[ABBREVIATIONS]}}
\def\endglossary{\endgl@ssary}
\def\gl@ssary[#1]{\@restonecoltrue\if@twocolumn\@restonecolfalse\fi\columnseprule \z@
\columnsep 35pt\twocolumn
\chapter*{\vskip 3.5mm \Large LIST OF #1}\@mkboth {#1}{#1}
\addcontentsline{toc}{leads}{\protect\numberline {}LIST OF \uppercase{#1}}\begin{singlespace}}
\def\endgl@ssary{\end{singlespace}\if@restonecol\onecolumn\else\clearpage\fi}

\def\preface{\addcontentsline{toc}{leads}{\protect\numberline {}PREFACE}
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \fi\chapter*{PREFACE}\@mkboth {PREFACE}{PREFACE}}
\def\endpreface{\if@restonecol \twocolumn\fi\newpage}

\def\vita{
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \pagestyle{plain}
 \fi\chapter*{\Large VITA}\@mkboth {VITA}{VITA}\addcontentsline{toc}{leads}{\protect\numberline {}VITA}}
\def\endvita{\if@restonecol \twocolumn\fi}

\def\trsum{
\@restonecolfalse\if@twocolumn\@restonecoltrue\onecolumn
 \pagestyle{plain}
 \fi\chapter*{\Large TURKISH SUMMARY}\@mkboth {TURKISH SUMMARY}{TURKISH
 SUMMARY}\addcontentsline{toc}{leads}{\protect\numberline {}TURKISH SUMMARY}}
\def\endtrsum{\if@restonecol \twocolumn\fi}

\def\preliminaries{\pagenumbering{roman}\pagestyle{plain}}%
\def\endpreliminaries{\newpage\pagestyle{headings}\pagenumbering{arabic}%
\addcontentsline{toc}{nodots}{\protect\numberline {}CHAPTER}%
\addcontentsline{lof}{nodots}{\protect\numberline {}FIGURES}%
\addcontentsline{lot}{nodots}{\protect\numberline {}TABLES}}

\def\@enddocumenthook{\label{`@lastpage'}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\endinput
%% end of file `metu.cls'
