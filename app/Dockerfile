FROM python:3.8-slim

RUN pip install -U Flask

RUN pip install requests

WORKDIR /app

COPY . .

EXPOSE 3105

ENTRYPOINT [ "python3"]
CMD [ "app.py" ]
