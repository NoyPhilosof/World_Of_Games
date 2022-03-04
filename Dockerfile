FROM python:alpine

RUN adduser mruser

USER mruser
ENV PATH="/home/mruser/.local/bin:${PATH}"

RUN pip install --upgrade pip
WORKDIR /home/mruser
COPY ./flask/ .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "MainScores.py"]
