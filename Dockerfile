# Dockerfile
FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache shadow && \
	useradd userdevops && \
	chown -R userdevops:userdevops /app

COPY requirements.txt .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

USER userdevops

EXPOSE 8080
ENTRYPOINT ["python", "main.py"]
