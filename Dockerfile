FROM python:3.7-slim-stretch

RUN apt-get -y update && apt-get -y install gcc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . .

CMD ["python", "src/GPT2-Learning.py"]
