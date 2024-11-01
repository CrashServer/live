#!/usr/bin/env python

import asyncio
import websockets

async def hello(websocket):
    msg = await websocket.recv()
    print(f"<<<Receive: {msg}")

    await websocket.send(msg)
    
async def main():
    async with websockets.serve(hello, "localhost", 20000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())