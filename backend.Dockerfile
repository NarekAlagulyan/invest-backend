FROM python:3.10

WORKDIR /project
COPY requirements.txt /project/

RUN python -m pip install --upgrade pip; pip install -r requirements.txt

ENV PYTHONIOENCODING=utf-8 \
    PYTHONUNBUFFERED=1


COPY . /project/

#ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["/usr/local/bin/gunicorn", "-w", "3", "InvestBackend.wsgi", "-b", "0.0.0.0:8000"]
