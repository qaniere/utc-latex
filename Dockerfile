FROM archlinux:latest

RUN pacman -Sy --noconfirm \
    texlive \
    texlive-basic \
    texlive-latex \
    texlive-latexextra \
    texlive-lang \
    && pacman -Scc --noconfirm \
    && rm -rf /var/cache/pacman/pkg/* \
    && rm -rf /var/lib/pacman/sync/* \
    && rm -rf /tmp/* /root/.cache
