from flask import Flask
import argparse
from util.app import create_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Flask on a specific port.")
    parser.add_argument(
        "--port", type=int, default=8080, help="Port to run the Flask app."
    )
    args = parser.parse_args()
    app = Flask(__name__)
    app = create_app(app)
    # app.run(
    #     host="0.0.0.0", port=args.port
    # )
    # Create OpenSSH certificates for HTTPS
    app.run(
        host="0.0.0.0", port=args.port, debug=True, ssl_context="adhoc"
    )
