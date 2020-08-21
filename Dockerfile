FROM python:alpine
LABEL maintainer="visaev@nil.com"

RUN pip install flask

WORKDIR /usr/app

EXPOSE 5000/tcp

ENTRYPOINT ["python"]
CMD ["start.py"]