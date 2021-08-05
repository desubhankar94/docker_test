FROM centos:7
RUN mkdir -p /myapp/
RUN apt-get update && apt-get install python3 -y
COPY . /myapp/
EXPOSE 8080
ENTRYPOINT ["python3", "/myapp/main.py"]