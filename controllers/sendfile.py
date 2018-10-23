
from aiohttp import web
import mimetypes
import os
import tempfile

class sendfile():
    def __init__(self):
        pass

    async def get(self, request):
        fh = tempfile.NamedTemporaryFile(delete=False)
        fh.write(bytes("test;test2" + os.linesep, 'UTF-8'))
        fh.close()
        filename = os.path.abspath(fh.name)
        with open(filename, "rb") as f:
            resp = web.StreamResponse()
            resp.content_type, _ = mimetypes.guess_type(filename)

            disposition = 'filename="{}"'.format(filename)
            if 'text' not in resp.content_type:
                disposition = 'attachment; ' + disposition

            resp.headers['CONTENT-DISPOSITION'] = disposition

            data = f.read()
            f.close()
            os.remove(fh.name)
            resp.content_length = len(data)
            await resp.prepare(request)

            await resp.write(data)
            return resp

        
