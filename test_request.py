
def test_listen_network(page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
    page.goto('https://osinit.ru/')