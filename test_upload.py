def test_select_multiple(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()