
from aiohttp import web
import mimetypes
import os

class sendfile():
    def __init__(self):
        pass

    async def get(self, request):
        filename = os.path.abspath("test.csv")
        with open(filename, "rb") as f:
            resp = web.StreamResponse()
            resp.content_type, _ = mimetypes.guess_type(filename)

            disposition = 'filename="{}"'.format(filename)
            if 'text' not in resp.content_type:
                disposition = 'attachment; ' + disposition

            resp.headers['CONTENT-DISPOSITION'] = disposition

            data = f.read()
            resp.content_length = len(data)
            await resp.prepare(request)

            await resp.write(data)
            return resp

        
