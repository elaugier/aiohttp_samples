from aiohttp import web
from controllers.sendfile import sendfile

app = web.Application()

sendfileCtrl = sendfile()

app.router.add_get("/sendfile", sendfileCtrl.get)

web.run_app(app,port=4563)

