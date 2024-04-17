FROM python:3.10-slim

RUN pip install -U Flask

RUN pip install requests

RUN pip install redis

WORKDIR /app

COPY . .

EXPOSE 3105

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
