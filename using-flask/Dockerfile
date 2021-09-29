FROM python:3.6-buster
WORKDIR /appflask
ENV FLASK_APP=index:server
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . .
CMD ["flask", "run"]