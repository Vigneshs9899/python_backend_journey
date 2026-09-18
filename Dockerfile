FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY 03_Flask/ .

EXPOSE 5000

CMD ["python", "app.py"]