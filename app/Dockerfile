FROM python:3.13-alpine

RUN adduser -D python

WORKDIR /app
#Afiner cette ligne et jouer avec ce qui est copié pour faire echouer les tests
COPY --chown=python:python app.py .
COPY --chown=python:python requirements.txt .
COPY --chown=python:python data.html . 

RUN pip install --no-cache-dir -r requirements.txt
ENV NAME=chti_tremplin_app
# Change user
USER python
CMD ["python", "app.py"]
