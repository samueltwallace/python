\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{blogTemplate}

\LoadClass{article}

\RequirePackage{amssymb}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{hyperref}
\RequirePackage{mathrsfs}
\RequirePackage{mathtools}
\RequirePackage{import}
\RequirePackage{fancyhdr}
\RequirePackage{datetime}
\DeclareOption*{\PassOptionToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\pagestyle{fancy}
\fancyhf{}
\rhead{\rightmark}
\lhead{\leftmark}

\newenvironment{xmlfeed}{}{\bigskip}
\newcommand{\xmlfeedtitle}[1]{\section{#1}}
\newcommand{\xmlentriestitle}[1]{\subsection{#1}}
