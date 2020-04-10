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
\RequirePackage[disable]{todonotes}
\DeclareOption*{\PassOptionToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\pagestyle{fancy}
\fancyhf{}
\rhead{\rightmark}
\lhead{\leftmark}

\newenvironment{xmlfeed}{}{\bigskip}
\newcommand{\xmlfeedtitle}[1]{\section{#1}}
\newenvironment{xmlfeedtitledetail}
\newcommand{\xmltitledetailtype}{}
\newcommand{\xmltitledetailbase}{}
\newcommand{\xmltitledetailvalue}{}
\newenvironment{xmlfeedlinks}{\small \itshape}{\normalsize}
\newcommand{\xmllinkshref}[1]{RSS feed available \href{#1}{here}.}
\newcommand{\xmllinksre}{}
\newcommand{\xmllinkstype}{}
\newcommand{\xmllinksrel}{}
\newcommand{\xmllinkstype}{}
\newcommand{\xmlfeedlink}[1]{\href{#1}{Homepage}\\}
\newcommand{\xmlfeedsubtitle}{}
\newcommand{\xmlfeedupdated}[1]{Updated #1\\}
\newcommand{\xmlentrieslink}[1]{\href{#1}{Original Page}\\}
\newcommand{\xmlentriescomments}[1]{\href{#1}{Comments}\\}
\newcommand{\xmlentriespublished}[1]{Published #1\\}
\newcommand{\xmlentriesauthor}[1]{Written by #1}
\newcommand{\xmlentriessummary}[1]{\large \textit{#1}\\}
\newenvironment{xmlentriescontent}{}{}
\newcommand{\p}[1]{\indent #1 \\}

\newcommand{\xmlentriestitle}[1]{\subsection{#1}}
