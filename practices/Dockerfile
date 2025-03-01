FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /practicefolder

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /practicefolder/entrypoint.sh

COPY . .

EXPOSE 8000

ENTRYPOINT ["/practicefolder/entrypoint.sh"]