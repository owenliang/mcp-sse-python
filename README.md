# mcp-sse-python

## 本地测试运行

```
$ python sse_server.py
?[32mINFO?[0m:     Started server process [?[36m20456?[0m]
?[32mINFO?[0m:     Waiting for application startup.
?[32mINFO?[0m:     Application startup complete.
?[32mINFO?[0m:     Uvicorn running on ?[1mhttp://0.0.0.0:8000?[0m (Press CTRL+C to quit)
```

```
$ python sse_client.py
URL:http://baidu.com
meta=None content=[TextContent(type='text', text='<html>\n<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">\n</html>\n', annotations=None)] isError=False
```

## 开源客户端配置

```
{
  "mcpServers": {
    "website-fetcher": {
      "url": "http://localhost:8000/sse",
      "disabled": false,
      "autoApprove": [
        "fetch"
      ]
    }
  }
}
```