from flask_socketio import SocketIO, emit
from flask import request, jsonify
from views import logics
from http import HTTPStatus
import time, traceback
from config.constants import poem
from exception_handlers.Exceptions import InvalidRequestException, APIConnectionException

socketio = SocketIO()
# connected_clients = set()

@socketio.on('generate_poem')
def generate_poem(data):
    '''
        request:
            JSON object with a key 'prompt' containing an idea for a poem
        response:
            201: 
                description: AI generated poem
    '''
    try:
        # data = request.json if request.data else None
        
        if logics.validate_request(data) == "invalid":
            raise InvalidRequestException
        print(f"\n\n{data = }\n\n")
        # response = logics.generate_ai_poem(data["prompt"])
        response = poem
        if response == "error":
            raise APIConnectionException
        for token in response.split():
            print(f'{token = }')
            emit('poem_token', {'token': token})
            time.sleep(0.1)
        emotion_analysis = logics.analyze_emotion(response)
        print(f'{emotion_analysis = }')
        emit('emotion_analysis', {"emotions": emotion_analysis})
    #     emotion_analysis = logics.analyze_emotion(response)
    #     return {"poem": response, "emotions": emotion_analysis}
    # except InvalidRequestException as e:
    #     return jsonify(message = e.description), e.code
    # except APIConnectionException as e:
    #     return jsonify(message = e.description), e.code
    except:
        print(f"{traceback.format_exc()}")
        return jsonify(message="Internal Server Error"), HTTPStatus.INTERNAL_SERVER_ERROR

# @socketio.on('UserConnect')
# def handle_connect(data):
    
#     connected_clients.add(request.sid)

# @socketio.on('disconnect')
# def handle_disconnect():
#     connected_clients.remove(request.sid)
