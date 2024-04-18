FROM python:3.10-slim

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3105

ENTRYPOINT [ "python3" ]
CMD [ "server.py" ]
