FROM ghcr.io/openai/codex-universal:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pytest

WORKDIR /app
COPY . /app

CMD ["bash"]
