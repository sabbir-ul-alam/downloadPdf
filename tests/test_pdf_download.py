from pages.download_pdf import SeleniumCheatSheetPage
import os


def test_pdf_download(path,browser):
    url,pdf_path=path
    page = SeleniumCheatSheetPage(browser)
    page.load(url)
    pdf_url = page.open_pdf_and_switch_to_new_tab()
    result = page.download_pdf(pdf_url,pdf_path)
    assert result == 'Success'
    if os.path.exists(pdf_path):
        assert True
    else:
        assert False
