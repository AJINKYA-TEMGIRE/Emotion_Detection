from python:3.9

workdir /app

copy flaskapp/ /app/

copy models/vectorizer.pkl /app/models/vectorizer.pkl

run pip install -r requirements.txt

RUN python -m nltk.downloader stopwords wordnet

expose 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]