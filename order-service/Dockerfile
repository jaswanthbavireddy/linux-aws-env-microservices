FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --gid 10001 appgroup \
    && useradd --uid 10001 --gid appgroup --no-create-home appuser

COPY --chown=appuser:appgroup app.py /app/app.py

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]
