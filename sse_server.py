from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route
import uvicorn
import httpx

from mcp.server import session

mcpserver=FastMCP(name='website fetcher') # handle session
sse_transport=SseServerTransport('/messages/') # handle io(sse,post)

@mcpserver.tool(name='fetch',description='Fetches a website and returns its content')
async def fetch_website(url: str):
    print('fetching....')
    if not url.startswith('http://') and not url.startswith('https://'):
        url='https://'+url
    async with httpx.AsyncClient(follow_redirects=True) as client:
        response=await client.get(url)
        if response.status_code!=200: 
            return f'Error fetching {url}: {response.status_code}'
        return response.text

async def sse_handler(request):
    async with sse_transport.connect_sse(request.scope,request.receive,request._send) as streams:
        await mcpserver._mcp_server.run(streams[0],streams[1],mcpserver._mcp_server.create_initialization_options()) # keep sse session

app=Starlette(
    debug=True,
    routes=[
        Route('/sse',endpoint=sse_handler),
        Mount('/messages/',app=sse_transport.handle_post_message)
    ]
)
uvicorn.run(app,host='0.0.0.0',port=8000)