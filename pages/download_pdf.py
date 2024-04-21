from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class SeleniumCheatSheetPage:
    PDF_LINK =(By.LINK_TEXT,'Download a Printable PDF of this Cheat Sheet')


    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)


    def open_pdf_and_switch_to_new_tab(self):
        original_tab = self.browser.current_window_handle
        wait = WebDriverWait(self.browser, 10)
        link = wait.until(EC.element_to_be_clickable(self.PDF_LINK))
        link.click()
        wait.until(EC.number_of_windows_to_be(2))
        for window_handle in self.browser.window_handles:
            if window_handle != original_tab:
                self.browser.switch_to.window(window_handle)
                break
        return self.browser.current_url


    def download_pdf(self,url,pdf_path):
        # pdf_path = "../the_downloaded_file.pdf"
        response = requests.get(url)
        if response.status_code == 200:
            # Write the content of the response to a PDF file
            try:
                with open(pdf_path, 'wb') as f:
                    f.write(response.content)
            except Exception as e:
                return "Failed"
            return "Success"
        else:
            return "Failed"









