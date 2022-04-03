# import base image 
FROM ubuntu:20.04

# install python 
RUN apt-get update && apt-get install python3 -y && apt install python3-pip -y

# copy files
COPY main.py requirements.txt ./

# install from reqs
RUN python3 -m pip install -r requirements.txt

# on launch
CMD["python3", "-m", "uvicorn", \
	"main:app", "--reload", "--host", "0.0.0.0", "--port", 8080]