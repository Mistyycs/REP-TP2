FROM python:3.12-alpine

WORKDIR /app

COPY asso2.py /app

CMD ["python", "asso2.py"]