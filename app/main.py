# Importing libs
import os
import redis
from fastapi import FastAPI

# Create fastapi object
app = FastAPI()

# Get the service name and port from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

# Create a redis client object using the variables above
# decode_responses means that python objects are returned rather than raw bytes
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


# Endpoint 1: /health
# Registers an http get endpoint at /health, and then runs a function (if the ping succeeds)
@app.get("/health")
def health():
    try:
        r.ping
        return{"status": "ok", "redis": "ok"}
    except Exception as e:
        return {"status": "degraded", "redis": "down", "error": str(e)}


# Endpoint 2: /hit
# Registers another http get endpoint at /hit, and then incrementing a value stored at the key "hits" by redis
@app.get("/hit")
def hit():
    count = r.incr("hits")
    return {"hits": count}

