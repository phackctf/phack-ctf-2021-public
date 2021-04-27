FROM python:3

RUN mkdir /chall
WORKDIR /chall
COPY ./the_bot .

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

CMD ["bot.py"]

ENTRYPOINT ["python3"]
