from flask import Flask
import aioredis
app = Flask(__name__)

@app.route('/')
def hello_world():
    redis = aioredis.from_url("redis://red-c8sf3jd0maldij14587g:6379")
    return 'Hello, World!'
