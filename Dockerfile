FROM python:3.10.10-alpine3.17
LABEL maintainer="hyanbatista42@gmail.com"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        app-user

ENV PATH="/venv/bin:$PATH"

USER app-user

ENTRYPOINT [ "python", "-m", "main" ]
