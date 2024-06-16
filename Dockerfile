FROM python:3.8.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY myshop .

COPY db.sqlite3 .

CMD ["python3", "manage.py", "runserver", "0:8000"]