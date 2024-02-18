from fastapi import APIRouter,FastAPI
import routers
from redis_conn import create_redis_pool
from contextlib import asynccontextmanager

app = FastAPI()
app.include_router(APIRouter())

main_app_lifespan = app.router.lifespan_context
@asynccontextmanager
async def lifespan_wrapper(app):
    print("Custom startup actions")
    global redis
    redis = await create_redis_pool()
    
    async with main_app_lifespan(app) as maybe_state:
        yield maybe_state
    
    print("Custom shutdown actions")
    if redis:
        redis.close()
        await redis.wait_closed()

app.router.lifespan_context = lifespan_wrapper


@app.get("/")
async def get_data():
    key = "A60rnce0cblbrmt9l2pw30otkv73nsaxta0iqr79mzdkahdrefe"
    value = await redis.get(key)

    if value is None:
        value = "None"
        await redis.setex(key, 3600, value)

    return {"data": value}
