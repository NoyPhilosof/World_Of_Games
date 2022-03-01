FROM python:alpine

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# CMD ["flask", "run", "-h", "0.0.0.0"]

CMD ["python3", "MainScores.py"]
