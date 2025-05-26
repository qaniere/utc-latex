FROM archlinux:latest

RUN pacman -Sy --noconfirm \
    texlive \
    texlive-basic \
    texlive-latex \
    texlive-latexextra \
    texlive-lang \
    && pacman -Scc --noconfirm
