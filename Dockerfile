FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY tap_tally/ ./tap_tally
CMD ["flask", "run", "--host", "0.0.0.0"]
