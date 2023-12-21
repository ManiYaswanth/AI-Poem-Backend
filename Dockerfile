FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENV FLASK_APP main.py

CMD ["python3", "app/main.py"]
