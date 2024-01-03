FROM python:3.13-rc-alpine

WORKDIR /opt

COPY src/ /opt/
COPY requirements.txt /opt/
RUN pip install -r requirements.txt 

ENTRYPOINT ["python", "main.py"]