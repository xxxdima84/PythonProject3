def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()

def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()