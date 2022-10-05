FROM python:3.8 AS compile-image

WORKDIR /app

COPY ./app/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./

COPY ./compose/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["runserver"]