FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python3","rut.py"]