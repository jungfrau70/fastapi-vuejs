import asyncio
import uvicorn
import pandas as pd
import pytz

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from models import *
from config import config

section_name = 'common'
section = config[section_name]
CLIENT_ORIGIN = section.get('CLIENT_ORIGIN')

app = FastAPI()
origins = [
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # milisecond

@app.get('/stream')
async def message_stream(request: Request):
    def new_messages():
        # Add logic here to check for new messages
        # query = f"SELECT DISTINCT sym FROM backtest WHERE market = '{market}'"
        query = f"SELECT * FROM signals"
        result = pd.read_sql(query, engine)
        print(result)

        # Check if data in table
        if result.empty:
            return None
        else:
            json_data = result.to_json(orient='records')
            return json_data        
    async def event_generator():
        while True:
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break

            json_response = new_messages()
            # Checks for new messages and return them to client if any
            if json_response:
                yield {
                        "event": "new_message",
                        "id": "message_id",
                        "retry": RETRY_TIMEOUT,
                        "data": json_response
                }

            await asyncio.sleep(STREAM_DELAY)

    return EventSourceResponse(event_generator())