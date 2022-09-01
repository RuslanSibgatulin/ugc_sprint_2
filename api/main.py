import uvicorn
from db import mongo
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1.bookmark import router as bookmark_router
from api.v1.progress import router as progress_router
from api.v1.rating import router as rating_router
from core.logger import LOGGING

app = FastAPI(
    title="UGC API",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(progress_router, prefix="/api/v1")
app.include_router(rating_router, prefix="/api/v1")
app.include_router(bookmark_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    # kafka.kafka_handler = await kafka.get_kafka_handler()
    mongo.mongo_client = await mongo.get_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    # await kafka.kafka_handler.stop()
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_config=LOGGING)
