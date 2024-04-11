FROM python
EXPOSE 5000

WORKDIR /app

RUN pip install flask

COPY . /app

CMD ["flask", "run", "--host", "0.0.0.0"]