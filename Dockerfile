FROM python:3.11-rc-alpine

WORKDIR /opt

COPY src/ /opt/
COPY requirements.txt /opt/
RUN pip install -r requirements.txt 

ENTRYPOINT ["python", "main.py"]