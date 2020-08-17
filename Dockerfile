FROM python

ENV COMMAND worker

COPY . /meete/

USER meete

ENTRYPOINT python3 /meete/main/app.py $COMMAND
