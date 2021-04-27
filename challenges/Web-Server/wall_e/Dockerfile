FROM python:3

RUN mkdir /chall
WORKDIR /chall

COPY static static
COPY templates templates
COPY resources resources
COPY server.py .
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["server.py"]

ENTRYPOINT ["python3"]
