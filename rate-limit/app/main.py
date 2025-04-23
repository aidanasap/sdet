from fastapi import FastAPI, HTTPException, Request
from app.token_bucket import TokenBucket

app = FastAPI()
rate_limiter = TokenBucket(capacity=5, refill_rate=1)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if not rate_limiter.allow_request():
        raise HTTPException(status_code=429, detail="Too Many Requests")
    response = await call_next(request)
    return response

@app.get("/")
async def default():
    return {"message": "Fine"}
