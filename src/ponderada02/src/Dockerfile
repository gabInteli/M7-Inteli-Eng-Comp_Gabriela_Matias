FROM python:latest

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]