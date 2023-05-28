FROM python:3.8-slim

# Install basic requirements for application
RUN apt-get update
RUN apt-get --assume-yes install git

WORKDIR /ml
ADD . .

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install git+https://github.com/RUCAIBox/RecBole.git
# RUN git clone https://github.com/RUCAIBox/RecBole.git
# RUN cd RecBole
# RUN pip install -e . --verbose
# RUN cd ../ && rm -rf RecBole

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EXPOSE 8000