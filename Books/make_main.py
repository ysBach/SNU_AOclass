from pathlib import Path
import subprocess


def newline(fileobj, repeat=1):
    return fileobj.write("\n" * repeat)


alltex = list(Path("chaps").glob("*.tex"))
alltex.sort(reverse=False)

firststr = r'''\documentclass[11pt,a4paper]{book}
\usepackage[top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm,headsep=10pt,letterpaper]{geometry}
\usepackage{physics}
\usepackage{siunitx}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{thmtools}
\usepackage{tikz}
\usepackage{hyperref}
\usepackage{cleveref} % cleverref must come AFTER hyperref
\usepackage{bm}
\usepackage{xcolor}
\usepackage[font=small]{caption}
\usepackage[perpage]{footmisc}
\usepackage{pythonhighlight}
\usepackage{fancyhdr}

\usepackage[shortlabels]{enumitem}
\setlist[itemize]{noitemsep}
\setlist[enumerate]{noitemsep}

\setlength{\parindent}{1em}
\setlength{\parskip}{0.5em}
\setlength{\footnotesep}{1em}

% https://tex.stackexchange.com/questions/300340/topsep-itemsep-partopsep-and-parsep-what-does-each-of-them-mean-and-wha
\setlist[itemize]{noitemsep, topsep=-\parskip, parsep=0pt}
\setlist[enumerate]{noitemsep, topsep=-\parskip, parsep=0pt}

\renewcommand{\baselinestretch}{1.1}
\renewcommand{\thefootnote}{\fnsymbol{footnote}}

\pagestyle{fancy}
\renewcommand{\chaptermark}[1]{\markboth{#1}{}}

\fancyhf{} % clear the headers
\fancyhead[R]{%
   % We want italics
   %\itshape
   % The chapter number only if it's greater than 0
   \ifnum\value{chapter}>0 Ch\ \thechapter. \fi
   % The chapter title
   \leftmark}
\fancyfoot[C]{\thepage}

%\fancyhf{}
%\rhead{Ch \thechapter. \rightmark}
\lhead{SNU AO Seminar Notes}
\chead{Y. P. Bach}
%\rfoot{\thepage}

% below from https://tex.stackexchange.com/questions/80286/can-i-define-a-new-unit-that-behaves-like-ang-in-siunitx
\newcommand*{\hms}[2][]{{
    \ang[
        math-degree=\textsuperscript{h},             % Solution 2
        text-degree=\textsuperscript{h},             % Solution 2
        math-arcminute=\textsuperscript{m},          % Solution 2
        text-arcminute=\textsuperscript{m},          % Solution 2
        math-arcsecond=\textsuperscript{s},          % Solution 2
        text-arcsecond=\textsuperscript{s},          % Solution 2
        #1]{#2}%
}}

\newcommand*{\m}[2][]{{
    \ang[
        math-degree=\textsuperscript{m},             % Solution 2
        text-degree=\textsuperscript{m},             % Solution 2
        #1]{#2}%
}}

\renewcommand{\lg}{\ensuremath{\log_{10}}}
\newcommand{\degr}{\ensuremath{\degree}}
\newcommand{\sun}{\ensuremath{\odot}}
\newcommand{\earth}{\ensuremath{\oplus}}

\newcommand{\lineseg}[1]{\ensuremath{\overline{\mathrm{#1}}}}
\newcommand{\triang}[1]{\ensuremath{\triangle \mathrm{#1}}}
\newcommand{\rect}[1]{\ensuremath{\Box \mathrm{#1}}}
\newcommand{\linevec}[1]{\ensuremath{\overrightarrow{\mathrm{#1}}}}


\newcommand{\sep}{\quad;\quad}


\declaretheorem[
  thmbox={style=M, bodystyle=\normalfont\small, headstyle=\small\color{red!55!black}\bfseries Ex \upshape\theex}
  ]{ex}
\declaretheorem[
  thmbox={style=M, bodystyle=\normalfont\small, headstyle=\small\color{blue!55!black}\bfseries Thm \upshape\thethm}
  ]{thm}
\declaretheorem[
  thmbox={style=M, bodystyle=\normalfont\small, headstyle=\small\color{green!55!black}\bfseries Def \upshape\thedefn}
  ]{defn}


%% This bit allows you to either specify only the files which you wish to
%% process, or `all' to process all files which you \include.
%% Krishna Sethuraman (1990).
%
%\typein [\files]{Enter file names to process, (chap1,chap2 ...), or `all' to process all files:}
%\def\all{all}
%\ifx\files\all \typeout{Including all files.} \else \typeout{Including only \files.} \includeonly{\files} \fi

\begin{document}
\begingroup
\thispagestyle{empty}
\centering
\vspace*{5cm}
\par\normalfont\fontsize{35}{35}\sffamily\selectfont
\textbf{SNU AO Seminar Notes}\\
{\LARGE Astronomical Observation and Lab at Seoul National University}\par % Book title
\vspace*{1cm}
{\Huge Yoonsoo P. Bach}\par % Author name
\vspace*{5cm}
{\normalsize This book is prepared since 2019 Spring,} \par
{\normalsize Seminars are given since 2016 Fall.} \par
\endgroup

\tableofcontents
'''

with open("main.tex", "w+") as mf:
    mf.write(firststr)
    for t in alltex:
        mf.write(r"\input{{{}}}".format(t) + '\n')
    newline(mf, 2)
    mf.write(r"\end{document}")

subprocess.check_call(["pdflatex", "main.tex"])
