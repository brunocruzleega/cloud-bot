# set base image (host OS)
FROM python:3.8

# copy the dependencies file to the working directory
COPY *.py /

# command to run on container start
CMD [ "python", "/*.py" ]