# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# ADD bot.py /app/bot.py
# ADD bot.py /app/bot.py

COPY bot.py bot.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# COPY . .

# CMD [ "python3", "bot.py"]
CMD [ "nohup", "python", "./bot.py"]
# ENTRYPOINT [ "python" ]