FROM python:3.6-alpine

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY lib ./lib
COPY app.py ./
CMD ["flask", "run", "--host=0.0.0.0"]
