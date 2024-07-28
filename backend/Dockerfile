FROM python:3.11.4-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /backend
WORKDIR /backend

ADD . /backend

RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh
RUN chmod +x entrypoint.sh
COPY . .

ENTRYPOINT ["sh","./entrypoint.sh"]
