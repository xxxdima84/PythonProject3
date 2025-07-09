def test_element(page) -> None:
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())

def test_element2(page) -> None:
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())