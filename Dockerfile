FROM python:3.12-slim-bullseye as production

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y curl gcc build-essential \
 && curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python -\
 && cd /usr/local/bin \
 && ln -s /opt/poetry/bin/poetry \
 && poetry config virtualenvs.create false \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock /app/
RUN poetry install -n --only main --no-root

ADD app /app/
RUN chmod +x scripts/* \
 && poetry install -n --only-root \
 && pybabel compile -d locales -D bot

ENTRYPOINT ["python"]
CMD ["main.py"]