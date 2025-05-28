# UTC Latex

This repository contains **unofficial** LaTeX templates for the [Université de Technologie de Compiègne (UTC)](https://www.utc.fr).

I'm not the original author of theses, i've simply adapted and simplified them for my usage. The original authors are :

- UTC Article : milouse, under the [WTFPL license](./licenses/utc-article.txt) ([Source](https://github.com/milouse/utclatex))
- UTC Beamer : milouse, under the [WTFPL license](./licenses/utc-beamer.txt) ([Source](https://github.com/milouse/utclatex))
- UTC Report : Florent Chehab, under the [BSD-2 license](./licenses/utc-report.txt) ([Source](https://gitlab.utc.fr/LaTeX-UTC/Templates/Rapport-TP-LaTeX-UTC))

The [legal notice](https://www.utc.fr/mentions-legales.html) of the UTC website stipulates :

> Any use whatsoever of the brand names and logos on this site is prohibited without the authorization of the Université de Technologie de Compiègne.


Feel free to open issues and of course, pull requests are very welcome.

## Usage

You can see compiled examples [here](https://qaniere.github.io/utc-latex/). In each package, you will also find a minimal example (main.tex).

### Overleaf

A zip archive for each template (article, beamer, report) is automatically generated at each release. You can go to [the release tab](https://github.com/qaniere/utc-latex/releases) and download the archive you want (one which end in 'overleaf'). Then, you can go to Overleaf and import the zip as a new project and start editing.

If you are a french student, you might have access to the [CNRS Overleaf instance](https://plmlatex.math.cnrs.fr/).

### Locally

A zip archive is generated at each release. This release contains all the templates. You can download it from [the release tab](https://github.com/qaniere/utc-latex/releases) (utc-latex.zip) and extract it in your TEXMFHOME / DIST. 

A shell script 'setup.sh' is provided to automate the installation on Linux only.

## Contributors
    
 - Thanks to [Hugo Pereira](https://github.com/tigrou23) for his awesome work on the CI/CD process.
 - Thanks to the original authors.