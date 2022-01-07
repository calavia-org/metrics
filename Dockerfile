FROM python:alpine3.15

RUN apk fix

RUN apk --update add git git-lfs openssh && \
    git lfs install && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*
