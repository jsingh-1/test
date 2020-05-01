FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get update && apt-get install -y python3 
RUN apt-get update && apt-get install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
