FROM python:3.9

EXPOSE 8000/tcp

WORKDIR /FastAPIIntern

COPY ./requirements.txt /FastAPIIntern/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /FastAPIIntern/requirements.txt

COPY app /FastAPIIntern/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]