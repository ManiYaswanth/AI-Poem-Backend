from flask import Blueprint, request, jsonify
# from flask_socketio import emit
# from socket_conn.clients import connected_clients
from views import logics
from http import HTTPStatus
import time, traceback
from config.constants import example_poem
from exception_handlers.Exceptions import InvalidRequestException, APIConnectionException


mod = Blueprint("routes", __name__, template_folder="templates")

@mod.route("/poem-generator", methods=["POST"])
def generate_poem():
    '''
        request:
            JSON object with a key idea containing an idea for a poem
        response:
            201: 
                description: AI generated poem
    '''
    try:
        data = request.json if request.data else None
        
        if logics.validate_request(data) == "invalid":
            raise InvalidRequestException
        # response = logics.generate_ai_poem(data["prompt"])
        response = example_poem

        if response == "error":
            raise APIConnectionException
        for token in response.split():
            pass
            # for client in connected_clients:
                # emit('poem_token', {'token': token}, room=client)

        emotion_analysis = logics.analyze_emotion(response)
        return {"poem": response, "emotions": emotion_analysis}
    except InvalidRequestException as e:
        return jsonify(message = e.description), e.code
    except APIConnectionException as e:
        return jsonify(message = e.description), e.code
    except:
        return jsonify(message="Internal Server Error"), HTTPStatus.INTERNAL_SERVER_ERROR