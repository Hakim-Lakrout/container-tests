FROM python:3.13-alpine
RUN adduser -D python
WORKDIR /app
COPY --chown=python:python requirements.txt .  
#Afiner cette ligne et jouer avec ce qui est copié pour faire echouer les tests
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=python:python app.py .
COPY --chown=python:python --chmod=400 data.html . 
COPY --chown=python:python --chmod=400 static static
ENV NAME="Qui suis je ?"
# Change user
USER python
CMD ["python", "app.py"]