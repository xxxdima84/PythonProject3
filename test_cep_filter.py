def test_login(page):
    page.goto('https://exaltedplushadware.antonzimaiev.repl.co/?')
    page.locator("#exampleInputEmail1").fill("admin@example.com")
