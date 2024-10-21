FROM python:3.12-alpine

WORKDIR /app

COPY asso2.py /app

RUN pip install -r requirements.txt

CMD ["python", "asso2.py"]