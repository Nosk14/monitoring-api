FROM python:3.5.4-alpine3.4
ENV FLASK_APP /usr/local/monitoring-api/api.py
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY monitoring-api /usr/local/monitoring-api/
WORKDIR /usr/local/monitoring-api/
CMD gunicorn -w 2 -b 0.0.0.0:5000 api:app