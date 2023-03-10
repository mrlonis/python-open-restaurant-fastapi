FROM python:3.10

RUN apt-get update --fix-missing \
    && apt-get install -f -y \
    && apt-get upgrade -y \
    && apt-get install -y curl lsb-release iputils-ping iproute2 telnet

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade -r /code/requirements.txt
RUN pip install --upgrade uvicorn[standard]

COPY ./app /code/app
COPY ./.env_docker /code/.env

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8008"]
