FROM python:3.12.10-alpine

COPY ./requirements.txt /webapplication/requirements.txt

WORKDIR /webapplication

RUN apk update && apk add bash

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app /webapplication/app
COPY materialverwaltung.py /webapplication
COPY materialausgabe.db /webapplication

ENTRYPOINT ["python"]

CMD ["materialverwaltung.py"]
