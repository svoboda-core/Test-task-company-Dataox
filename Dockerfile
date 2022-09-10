FROM python:3.7

LABEL Vasily Konoval "vasilykonoval@gmail.com"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python" "main.py"]