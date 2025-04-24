FROM python:3.13-alpine
WORKDIR /app
RUN adduser -D python
COPY . .  
RUN pip install --no-cache-dir -r requirements.txt
ENV APP_NAME="chti tremplin"
USER python
CMD ["python3", "app.py"]