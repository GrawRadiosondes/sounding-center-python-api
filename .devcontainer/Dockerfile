# syntax=docker/dockerfile:1

FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV UV_LINK_MODE=copy

ENV PYTHONDONTWRITEBYTECODE="1"
ENV PYTHONUNBUFFERED="1"
ENV PYTHONPATH="src"

RUN apt update && apt install -y --no-install-recommends \
    build-essential \
    git \
    htop \
    iproute2 \
    netcat-openbsd \
    nmap \
    openssh-client \
    socat \
    && rm -rf /var/lib/apt/lists/*

RUN git config --global submodule.recurse true
RUN git config --global pull.rebase true
RUN git config --global rebase.autoStash true

RUN mkdir -p -m 0600 ~/.ssh
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts

WORKDIR /app
RUN uv venv
ENV PATH="/app/.venv/bin:$PATH"
COPY pyproject.toml uv.lock* /app/
RUN ls -lisha ~/.ssh
RUN --mount=type=ssh uv sync

RUN uv tool update-shell
RUN uv tool install bump-my-version
RUN uv tool install ruff

CMD ["sleep", "infinity"]
