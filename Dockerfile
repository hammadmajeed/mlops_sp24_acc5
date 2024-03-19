FROM python:3.11-slim
RUN mkdir -p /app/src
COPY ./src/. /app/src
WORKDIR /app/src
RUN pip install -r requirements.txt
CMD ["python", "app.py"]