FROM python:3.9

WORKDIR /FastAPIIntern

COPY ./requirements.txt /FastAPIIntern/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastAPIIntern/requirements.txt

COPY app /FastAPIIntern/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]