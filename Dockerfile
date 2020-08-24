FROM python:alpine
LABEL maintainer="visaev@nil.com"

WORKDIR /usr/app

COPY requires.txt ./
RUN apk add --no-cache mariadb-dev build-base && \
    pip install -r requires.txt

EXPOSE 5000/tcp

COPY ./app ./
COPY ./certs /usr/certs

ENTRYPOINT ["python"]
CMD ["start.py"]
