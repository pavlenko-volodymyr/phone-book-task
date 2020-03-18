FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT ["python"]
CMD ["run.py"]