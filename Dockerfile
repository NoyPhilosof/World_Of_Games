FROM python:alpine

RUN adduser -D mruser

USER mruser
ENV PATH="/home/mruser/.local/bin:${PATH}"

RUN pip install --upgrade pip
WORKDIR /home/mruser
COPY ./flask/ .
COPY ./scores/Scores.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "MainScores.py"]
