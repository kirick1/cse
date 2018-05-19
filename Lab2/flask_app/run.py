from app import app
from waitress import serve
import os

if __name__ == '__main__':
    serve(app,
          host=os.environ.get("HOST", "0.0.0.0"),
          port=os.environ.get("PORT", 3000),
          expose_tracebacks=True)
