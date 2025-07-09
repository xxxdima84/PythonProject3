def test_download(page) -> None:
    page.goto("https://demoqa.com/upload-download", wait_until="commit")
    with page.expect_download() as dl_info:
        page.locator("#downloadButton").click()
    download = dl_info.value
    file_name = download.suggested_filename
    destination_folder = './my_downloads/'
    os.makedirs(destination_folder, exist_ok=True)
    file_path = os.path.join(destination_folder, file_name)
    download.save_as(file_path)
