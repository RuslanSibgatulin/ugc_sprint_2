import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from db import kafka

app = FastAPI(
    title='Kafka API',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

# app.include_router(views.router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    kafka.kafka_handler = await kafka.get_kafka_handler()


@app.on_event("shutdown")
async def shutdown_event():
    await kafka.kafka_handler.producer.stop()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
