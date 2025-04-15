FROM python:3.11-slim

RUN useradd -m -d /home/python python

WORKDIR /app
#Afiner cette ligne et jouer avec ce qui est copié pour faire echouer les tests
COPY --chown=python:python app.py .
COPY --chown=python:python requirement.txt .
COPY --chown=python:python data.txt . 

RUN pip install --no-cache-dir -r requirements.txt
ENV TEST=test
# Change user
USER python
CMD ["python", "app.py"]
