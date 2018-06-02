from waitress import serve
from app import app
import os

if __name__ == '__main__':
    serve(app,
          host=os.environ.get("HOST", "localhost"),
          port=os.environ.get("PORT", 3000),
          expose_tracebacks=True)
