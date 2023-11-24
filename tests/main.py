"""Test website in selenium"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

options = Options()
options.add_argument("--remote-debugging-port=9222")

class GoogleTestCase(unittest.TestCase):
    """Testing class for testing the website in selenium"""

    def setUp(self):
        self.browser = webdriver.Chrome(options=options)
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """Test the title is set correctly"""
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

    def test_search(self):
        self.browser.get('http://www.google.com')
        assert 'Google' in self.browser.title
        elem = self.browser.find_element(By.NAME, 'q')
        elem.send_keys('seleniumhq' + Keys.RETURN)
        self.assertIn('seleniumhq - Google Search', self.browser.title)

if __name__ == '__main__':
    with Display(visible=0, size=(1600, 1200)):
        unittest.main(verbosity=2)
