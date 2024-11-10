FROM python:3.11.9

COPY ./requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip install -r requirements.txt
RUN pip install tf-keras

COPY webapp/* /webapp
ENTRYPOINT [ "uvicorn" ]
EXPOSE 8000

CMD [ "--host", "0.0.0.0", "main:app" ]

