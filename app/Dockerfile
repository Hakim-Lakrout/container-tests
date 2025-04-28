FROM python:3.13-alpine
RUN adduser -D python
WORKDIR /app
COPY --chown=python:python --chmod=400 requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=python:python app.py .
COPY --chown=python:python --chmod=555 static static 
ENV APP_NAME="chti tremplin"
USER python
CMD ["python3", "app.py"]