
FROM python:slim-buster
RUN pip install discord
RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
COPY example.py /
ENTRYPOINT python example.py