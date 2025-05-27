\ProvidesClass{utc-report}

\LoadClass[a4paper,12pt]{article}

\usepackage[T1]{fontenc} % French accents
\usepackage{graphicx} % Figures
\usepackage[headheight=61pt]{geometry} % Margins
\usepackage{float} % Layout stuff
\usepackage{xspace} % Spaces at the end of latex macros
\usepackage{enumitem} %For custom itemize
\geometry{vmargin=3cm, textwidth=16cm} % Margins
\usepackage{fancyhdr}		% Pour l'entête et les pieds de page
\pagestyle{fancy}			% Pour l'entête et les pieds de page

\usepackage{ulem} % Color underlining
\usepackage{utc_colors} % UTC colorsfrom 'utc-common'

% TODO EXPLICATION
\newif\if@noUTCcolors\@noUTCcolorsfalse
\DeclareOption{noUTCcolors}{
  \@noUTCcolorstrue
}
\ProcessOptions\relax

%Nouvelles variables
\newcommand{\UV}[1]{\def\theUV{#1}} %Passage de l'UV en variable

%Redéfinition des niveaux de titre
\if@noUTCcolors
  \definecolor{utcyellow}{RGB}{0,0,0} % hack to remove all trace of UTCjaune
\else
  \renewcommand{\labelitemi}{\color{utcyellow}$\bullet$} %Changement des puces itemize de niveau 1
  \renewcommand{\labelitemii}{\color{grisUTC}$\bullet$} %Changement des puces itemize de niveau 2

  \makeatletter

  \newcommand\sectionuline{% Commande pour souligner les sections en utcyellow
    \bgroup\markoverwith{\textcolor{utcyellow}{\rule[-0.5ex]{0.1mm}{0.5mm}}}%
    \ULon%
  }
  \renewcommand\section{\@startsection {section}{1}{\z@}% Redéfinition de la commande section (plus gros, souligné)
    {-3.5ex \@plus -1ex \@minus -.2ex}%
    {2.3ex \@plus .2ex}%
    {\normalfont\LARGE\bfseries\sectionuline}%
  }
  \renewcommand\subsection{\@startsection {subsection}{2}{0em}% Redéfinition de la commande subsection (plus gros, en gris UTC)
    {-3ex \@plus -0.8ex \@minus -.2ex}%
    {1.8ex \@plus .2ex}%
    {\normalfont\Large\bfseries}%
  }

  \renewcommand\subsubsection{\@startsection {subsubsection}{3}{0em}% Redéfinition de la commande subsubsection (plus gros, en gris UTC)
    {-2.5ex \@plus -0.6ex \@minus -.2ex}%
    {1.8ex \@plus .2ex}%
    {\normalfont\large\bfseries\color{grisUTC}}%
  }

  \renewcommand\paragraph{\@startsection {paragraph}{4}{3em}% Redéfinition de la commande paragraph (plus gros en gris clair UTC)
    {-2ex \@plus -0.4ex \@minus -.2ex}%
    {1.3ex \@plus .2ex}%
    {\normalfont\large\bfseries\color{grisClairUTC}}%
  }

  \renewcommand\subparagraph{\@startsection {subparagraph}{5}{4em}% Redéfinition de la commande subparagraph (en gris clair UTC)
    {-1.5ex \@plus -0.2ex \@minus -.2ex}%
    {.8ex \@plus .2ex}%
    {\normalfont\bfseries\color{grisClairUTC}}%
  }

  \makeatother
\fi

%En-tête et pied de page
\renewcommand{\headrulewidth}{0.5pt} %Épaisseur de la ligne d'en-tête
\renewcommand{\footrulewidth}{1.5pt} %Épaisseur de la ligne de pied de page
\renewcommand{\footrule}{%
  {\color{utcyellow} \hrule width\headwidth height\footrulewidth \vskip+2mm}
} %Changement de la couleur de la ligne de pied de page
%Contenu de l'en-tête :
\lhead{\textsc{\includegraphics[height=1.5cm]{utc_icon.png} \leftmark }} %Section actuelle à gauche de l'en-tête
\rhead{\theUV} %Code de l'UV à droite de l'en-tête
\renewcommand{\title}[1]{\def\thetitle{#1}}
\renewcommand{\author}[1]{\def\theauthor{#1}}
%Contenu du pied de page :
\cfoot{\thepage} %Numéro de page au centre
\lfoot{\theauthor} %auteur(s) à gauche

%Environements
\newenvironment{myabstract}{%
  \begin{quote} \begin{center}
    \bf}
  {\end{center} \end{quote}}
