FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .

COPY templates/ ./templates/
COPY static/ ./static/

EXPOSE 3000

CMD ["python3", "app.py"]