import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    while True:
        url=await asyncio.get_event_loop().run_in_executor(None,input,'URL:')
        
        try:
            async with sse_client('http://localhost:8000/sse') as streams:
                async with ClientSession(*streams) as session:
                    await session.initialize()
                    result=await session.call_tool('fetch',{'url':url})
                    print(result)
        except Exception as e:
            print('can not connect to mcpserver')

asyncio.run(main())