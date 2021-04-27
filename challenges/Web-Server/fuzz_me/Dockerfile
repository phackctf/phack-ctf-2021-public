FROM python:3
MAINTAINER contact@phack.fr

RUN mkdir /chall
WORKDIR /chall

COPY static static
COPY templates templates
COPY server.py .
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["server.py"]

ENTRYPOINT ["python3"]
