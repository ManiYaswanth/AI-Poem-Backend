from flask import Blueprint, request, json, jsonify, abort
# from flask_socketio import emit
# from socket_conn.clients import connected_clients
from views import logics
from http import HTTPStatus
import time, traceback
from config.constants import poem
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
        print(f"{request.data = }\n\n\n")
        data = request.json if request.data else None
        
        if logics.validate_request(data) == "invalid":
            raise InvalidRequestException
        print(f"\n\n{data = }\n\n")
        # response = logics.generate_ai_poem(data["prompt"])
        response = poem

        if response == "error":
            raise APIConnectionException
        for token in response.split():
            print(f"{token = }")
            # for client in connected_clients:
                # emit('poem_token', {'token': token}, room=client)

        emotion_analysis = logics.analyze_emotion(response)
        return {"poem": response, "emotions": emotion_analysis}
    except InvalidRequestException as e:
        return jsonify(message = e.description), e.code
    except APIConnectionException as e:
        return jsonify(message = e.description), e.code
    except:
        print(f"{traceback.format_exc()}")
        return jsonify(message="Internal Server Error"), HTTPStatus.INTERNAL_SERVER_ERROR