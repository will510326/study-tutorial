from bottle import route, default_app, run, request

from beaker.middleware import SessionMiddleware

session_opts = {
"session.type":"file",                                  # 以文件的方式保存session

"session.cookei_expires":300,                           # session過期時間爲3600秒

"session.data_dir":"./sessions",                        # session存放路徑

"sessioni.auto":True


@route("/test")

def test():

    s = request.environ.get("beaker.session")

    s["test"] = s.get("test", 0) + 1

    s.save()

    return "Test conter:",format(s["test"])

app = default_app()

app = SessionMiddleware(app, session_opts)



run(app=app)