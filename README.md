nltk.download('vader_lexicon') 
# Download the VADER lexicon if you haven't already

gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker main:app