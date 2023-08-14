# imagem base
FROM python:3.11
# diretório da imagem que vamos trabalhar
WORKDIR /code
#
COPY ./requirements.txt /code/requirements.txt
#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY . /code
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]