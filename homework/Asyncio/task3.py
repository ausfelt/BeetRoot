import asyncio

async def handle_echo(reader, writer):
    """
    This function handles a single client connection, echoing back whatever it receives.
    """
    while True:
        data = await reader.read(1024)  # Wait for data from the client
        if not data:
            break
        writer.write(data)  # Echo back the data
        await writer.drain()  # Wait for the data to be sent to the client
    writer.close()  # Close the connection

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
