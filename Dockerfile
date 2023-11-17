FROM python:3.10
COPY ./assets /assets
COPY app.py tasks.py requirements.txt ./
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y supervisor
COPY confs/supervisord.conf supervisord.conf
EXPOSE 8000
CMD [ "supervisord" ]