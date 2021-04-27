FROM python:3

ENV CHALL_PORT 4242

RUN mkdir /chall
WORKDIR /chall

COPY main.py .
COPY libs libs
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["main.py"]

ENTRYPOINT ["python3"]
