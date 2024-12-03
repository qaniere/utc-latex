FROM alpine:latest

ENV PYTHONUNBUFFERED=1 \
    TEXINPUTS=/usr/local/texmf/tex/latex//:.:$TEXINPUTS

RUN apk add --no-cache \
    git \
    python3 \
    py3-pip \
    py3-jinja2 \
    texmf-dist \
    texlive-most \
    texmf-dist-langfrench

ENV PATH="/md-converter:${PATH}"

COPY md-converter /
RUN chmod +x /*.py

COPY utc-beamer /usr/local/texmf/tex/latex/utc-beamer

WORKDIR /ws
