\ProvidesClass{utc-report/utc-report}

\LoadClass[a4paper,12pt]{article}

\usepackage[T1]{fontenc} % French accents
\usepackage{graphicx} % Figures
\usepackage[headheight=61pt,bottom=1cm]{geometry} % Margins
\usepackage{float} % Layout stuff
\usepackage{xspace} % Spaces at the end of latex macros
\usepackage{enumitem} %For custom itemize
\geometry{vmargin=3cm, textwidth=16cm} % Margins
\usepackage{fancyhdr} % Header and footer customisation
\pagestyle{fancy} % Header and footer customisation

\usepackage{ulem} % Color underlining
\usepackage{utc-common/utc_colors} % UTC colors from 'utc-common'

\ProcessOptions\relax

\newcommand{\UV}[1]{\def\theUV{#1}}
\renewcommand{\labelitemi}{\color{utcyellow}$\bullet$} % itemize level 1
\renewcommand{\labelitemii}{\color{utcgray}$\bullet$} % itemize level 2
\renewcommand{\title}[1]{\def\thetitle{#1}}
\renewcommand{\author}[1]{\def\theauthor{#1}}
\newcommand{\supervisor}[1]{\def\thesupervisor{#1}}
\newcommand{\displaysupervisor}{%
  \@ifundefined{thesupervisor}{}{%
    \large{\thesupervisor} \\[0.5cm]
  }%
}
\newcommand{\partnerlogofooter}[1]{\def\thepartnerlogofooter{#1}}
\newcommand{\partnerlogotitle}[1]{\def\thepartnerlogotitle{#1}}
\newcommand{\displaypartnerlogofooter}{%
  \@ifundefined{thepartnerlogofooter}{}{%
    \includegraphics[height=0.5cm]{\thepartnerlogofooter}%
  }%
}

\newcommand{\displaypartnerlogotitle}{%
  \@ifundefined{thepartnerlogotitle}{}{%
    \includegraphics[width=5cm]{\thepartnerlogotitle}%
  }%
}
\makeatletter

% Sections underlined in utcyellow
\newcommand\sectionuline{
  \bgroup\markoverwith{\textcolor{utcyellow}{\rule[-0.5ex]{0.1mm}{0.5mm}}}%
  \ULon%
}

% Sections bigger and underlined
\renewcommand\section{\@startsection {section}{1}{\z@}
  {-3.5ex \@plus -1ex \@minus -.2ex}%
  {2.3ex \@plus .2ex}%
  {\normalfont\LARGE\bfseries\sectionuline}%
}

% Subsections bigger
\renewcommand\subsection{\@startsection {subsection}{2}{0em}
  {-3ex \@plus -0.8ex \@minus -.2ex}%
  {1.8ex \@plus .2ex}%
  {\normalfont\Large\bfseries}%
}

% Subsections bigger and in gray UTC
\renewcommand\subsubsection{\@startsection {subsubsection}{3}{0em}
  {-2.5ex \@plus -0.6ex \@minus -.2ex}%
  {1.8ex \@plus .2ex}%
  {\normalfont\large\bfseries\color{utcgray}}%
}

% Paragraph bigger and in light gray utc
\renewcommand\paragraph{\@startsection {paragraph}{4}{3em}
  {-2ex \@plus -0.4ex \@minus -.2ex}%
  {1.3ex \@plus .2ex}%
  {\normalfont\large\bfseries\color{utcgray_light}}%
}

% Subparagraph in light gray utc
\renewcommand\subparagraph{\@startsection {subparagraph}{5}{4em}% Redéfinition de la commande subparagraph (en gris clair UTC)
  {-1.5ex \@plus -0.2ex \@minus -.2ex}%
  {.8ex \@plus .2ex}%
  {\normalfont\bfseries\color{utcgray_light}}%
}

\makeatother

% Header and footer
\renewcommand{\headrulewidth}{0.5pt} % Thickness of the header line 
\renewcommand{\footrulewidth}{1.5pt} % Thickness of the footer line 

% Set the footer size
\setlength{\footskip}{15mm} 

%Changing the color of the footer line
\renewcommand{\footrule}{%
  {\color{utcyellow} \hrule width\headwidth height\footrulewidth \vskip+2mm}
} 

% Header content
\lhead{\textsc{\includegraphics[height=1cm]{utc-common/utc_icon.png} \leftmark }} % Actual section
\rhead{\theUV} % Current UV

% Footer content
\cfoot{\thepage} % Page number
\lfoot{\theauthor} % Autors
\rfoot{%
  \includegraphics[height=0.5cm]{utc-common/utc_icon.png}%
  \hspace{0.5cm}%
  \displaypartnerlogofooter
}

% No space after section number
\makeatletter
\def\@seccntformat#1{\csname the#1\endcsname.\ }
\makeatother

% Title page
\newcommand{\maketitlepage}{
  \thispagestyle{empty}
  \setcounter{page}{0}
  
  \begin{figure}[H]
    \centering
    \includegraphics[width=7cm]{utc-common/utc_su_logo.png}
    
    \vspace{1cm}
    \displaypartnerlogotitle
  \end{figure}

  \vspace{3cm}
  
  \begin{center}
  {\color{utcyellow}\rule{\linewidth}{0.8mm}}
  \vspace*{0mm}
  
  \Huge{\textbf{\theUV \\ \thetitle}}
  {\color{utcyellow}\rule{\linewidth}{0.8mm}}
  \vspace{2cm}

  \Large{\theauthor} \\[0.5cm]
  \displaysupervisor

  \vspace{5cm}
  \Large{\today}
  \end{center}
  
  \vspace{3cm}
  \pagebreak
}

\makeatletter

% Custom itemize with UTC yellow
\newif\ifutc@customitemize
\utc@customitemizetrue % Enabled by default

% Option to disable it
\newcommand{\disableutcitemize}{\utc@customitemizefalse}

% Redefine the itemize if enabled
\AtBeginDocument{%
  \ifutc@customitemize
    \setlist[itemize,1]{label=\raisebox{0.2ex}{\includegraphics[height=1ex]{utc-common/utc_dot.png}}, labelsep=0.6em, left=1.5em}
    \renewcommand{\labelitemii}{\raisebox{0.15ex}{\includegraphics[height=0.7ex]{utc-common/utc_dot.png}}}
  \fi
}

\makeatother
