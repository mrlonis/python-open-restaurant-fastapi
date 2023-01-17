#
FROM python:3.10

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --upgrade -r /code/requirements.txt
RUN pip install --upgrade uvicorn[standard]

#
COPY ./app /code/app
COPY ./.env_docker /code/.env

#
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8008"]
