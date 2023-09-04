from flask_socketio import SocketIO, emit
from flask import request
from views import logics
import time, traceback
from config.constants import example_poem
from exception_handlers.Exceptions import InvalidRequestException, APIConnectionException

socketio = SocketIO()
connected_clients = set()

@socketio.on('generate_poem')
def generate_poem(data):
    '''
        request:
            JSON object with a key 'prompt' containing an idea for a poem
        response:
            webscocket emission of generated poem stream and emotion analysis
    '''
    try:
        if logics.validate_request(data) == "invalid":
            raise InvalidRequestException
        response = logics.generate_ai_poem(data["prompt"])
        # response = example_poem
        if response == "error":
            raise APIConnectionException
        for token in response.split("\n"):
            emit('poem_token', {'token': token}, room=request.sid)
            time.sleep(0.1)
        try:
            emotion_analysis = logics.analyze_emotion(response)
            emit('emotion_analysis', {"emotions": emotion_analysis}, room = request.sid)
        except Exception as e:
            print(traceback.format_exc())
            emit('chart_generation_error', {'error_message': str(e)})
    except Exception as e:
        emit('poem_generation_error', {'error_message': str(e)})
        

@socketio.on('connect')
def handle_connect(data):
    connected_clients.add(request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    connected_clients.remove(request.sid)
