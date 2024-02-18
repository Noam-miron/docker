FROM python:3.12-slim as base

WORKDIR /app
COPY app.py /app

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

FROM base as testing

COPY test_inc.py /app
RUN python -m pip install pytest

CMD ["pytest"]

FROM base as production

CMD ["python", "app.py"]

