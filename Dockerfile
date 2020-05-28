FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "main.py"]

