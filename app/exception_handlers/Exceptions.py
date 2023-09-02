from werkzeug.exceptions import HTTPException

class InvalidRequestException(HTTPException):
    code = 400
    description = "Invalid request. Kindly check the format"


class APIConnectionException(HTTPException):
    code = 404
    description = "API connection error"