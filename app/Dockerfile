FROM python:3.8-slim as base
RUN useradd app


FROM base as builder
COPY requirements.txt /requirements.txt
RUN python3 -m pip install --no-cache-dir --prefix=/install -r /requirements.txt

FROM base
ENV PYTHONUNBUFFERED=1

COPY --from=builder /install /usr/local

WORKDIR /opt
COPY --chown=app:app app.py .
USER app
ENTRYPOINT ["gunicorn", "app:app", "--bind=0.0.0.0:8000", "--workers=4", "--log-level=debug", "--reload"]