# UTC Latex

This repository contains **unofficial** LaTeX templates for the [Université de Technologie de Compiègne (UTC)](https://www.utc.fr).

I'm not the original author of theses, i've simply adapted for my usage. The original authors are :

- UTC Article : milouse, under the [WTFPL license](./licenses/utc-article.txt) ([Source](https://github.com/milouse/utclatex))
- UTC Beamer : milouse, under the [WTFPL license](./licenses/utc-beamer.txt) ([Source](https://github.com/milouse/utclatex))
- UTC Report : Florent Chehab, under the [BSD-2 license](./licenses/utc-report.txt) ([Source](https://gitlab.utc.fr/LaTeX-UTC/Templates/Rapport-TP-LaTeX-UTC))

The [legal notice](https://www.utc.fr/mentions-legales.html) of the UTC website stipulates :

> Any use whatsoever of the brand names and logos on this site is prohibited without the authorization of the Université de Technologie de Compiègne.

It is therefore advisable to use them within a framework satisfying this rule.

I'm not a (yet) LaTeX master, so feel free to open issues if you see something absolutely stupid or if something can be optimized, and of course, pull requests are very welcome :)

## Contributors
    
 - Thanks to [Hugo Pereira](https://github.com/tigrou23) for his awesome work on the CI/CD process !
 - Thanks to the original authors for theses templates.

## Installation
### Archlinux

These theme are packaged on the [AUR](https://aur.archlinux.org/) :

- utc-latex-article
- utc-latex-beamer
- utc-latex-report

With yay, you can install it like this :
```bash
yay -Syu utc-latex-{article,beamer,report}
```

### Manually 

 - Find your TEXMFHOME / TEXMFDIST folder (home is only for the current user, dist is for all users on the system)
 - Place utc-article, utc-beamer and utc-report folders *only* in the tex/latex
 - Refresh you LaTeX files cache 

(Search the steps for your configuration, like "MacOs where is my TEXMF ?")

## Todolist (By priority)

- [ ] Fix utc-report by adding a \utclogo and the first page
- [ ] Add examples (WIP: beamer and report are still missing)
- [ ] Clean up 'utc-report' package (files and source code)
- [ ] Clean up AUR packages (WIP: only utc-report left)
- [ ] Make graphics and color commons for all packages
- [X] Add 'utc-article' package
- [X] Add CI/CD (Unsuccessful on ubuntu-latest github actions yet)