FROM tiangolo/meinheld-gunicorn:python3.7
RUN pip install flask
COPY ./app /app