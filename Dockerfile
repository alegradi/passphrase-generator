FROM python:3.12-alpine

WORKDIR /passphrase-generator

COPY requirements.txt .

RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT ["python3", "app/main.py"]
