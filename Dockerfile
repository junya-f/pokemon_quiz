FROM python:3.12.0

WORKDIR /app
COPY . /app

RUN pip3 install --nocache-dir -r requirements.txt

CMD ["python", "app.py"]
