def test_screenshot(page) -> None:
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="full_page.png", full_page=True)
    page.screenshot(path="screen/screenshot.png")

def test_screenshot2(page) -> None:
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="example.jpeg", type="jpeg", quality=80)