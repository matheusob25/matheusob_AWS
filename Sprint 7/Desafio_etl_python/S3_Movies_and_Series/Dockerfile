FROM python:latest

WORKDIR  /app/arq

RUN pip install boto3

COPY ArquivosCsv/Script.py /app/arq/

CMD ["python", "Script.py"]