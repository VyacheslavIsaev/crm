FROM python:alpine
LABEL maintainer="visaev@nil.com"

WORKDIR /usr/app-crm

COPY requires.txt ./
RUN apk add --no-cache mariadb-dev build-base && \
    pip install -r requires.txt

EXPOSE 5000/tcp

COPY ./data   ./data
COPY ./src   ./src
COPY ./certs ./certs
COPY ./tests ./tests

ENTRYPOINT ["python"]
CMD ["src/start.py"]
