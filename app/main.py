from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template
from flask_cors import CORS
from socket_conn.clients import socketio
from api import routes
from views import logics

app = Flask(__name__)
socketio.init_app(app, cors_allowed_origins="*", async_mode="gevent")
CORS(app, origins="*")
app.register_blueprint(routes.mod, url_prefix="/api/v1")
app.register_blueprint(logics.mod, url_prefix="/")

@app.route("/")
def landing_page():
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)
