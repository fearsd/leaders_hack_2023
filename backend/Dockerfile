FROM python:3.8-slim

# Install basic requirements for application
RUN apt-get update 

WORKDIR /
COPY *.txt .

RUN pip install -r requirements.txt --no-cache-dir


# Install applicaiton

RUN mkdir /app
WORKDIR /app
ADD *.py .
ADD .env .

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000