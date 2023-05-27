FROM python:3.8-slim

# Install basic requirements for application
RUN apt-get update 

WORKDIR /backend
ADD . .

RUN pip install -r requirements.txt --no-cache-dir


ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000