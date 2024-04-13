import pytest
from playwright.sync_api import sync_playwright, Playwright
from playwright.sync_api import expect
import os



@pytest.fixture()
def page():
    """Браузер и контекст"""
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True,slow_mo=1)
    context = browser.new_context(viewport={"height":1920,"width":1080},locale="ru-RU")
    page_data = context.new_page()
    yield page_data


class TestAvitoScreenshots:


    @pytest.fixture(autouse=True)
    def setup_test(self,page):
        """"""
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.check_dir()
        self.url = "https://www.avito.ru/avito-care/eco-impact"
        self.locator_1 = "xpath=//html/body/div[1]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]"
        self.locator_2 = "xpath=//html/body/div[1]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]"
        self.locator_3 = "xpath=//html/body/div[1]/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]"
        self.page = page
        


    def check_dir(self):
        """Проверка наличия директории output, создание директории при ее отсутствии"""
        if not os.path.exists(os.path.join(self.base_dir,"output")):
            os.mkdir(os.path.join(self.base_dir,"output"))

    
   
    def test(self):
        """Обнаружение локатора на странице, скриншот элемента и сохранение скриншота в директории output"""
        self.page.goto(self.url)
        element_1 = self.page.locator(self.locator_1)
        expect(element_1).to_be_visible()
        element_1.screenshot(path=os.path.join(self.base_dir,"output",f"screenshot_test_1.png"))
        element_2=self.page.locator(self.locator_2)
        expect(element_2).to_be_visible()
        element_2.screenshot(path=os.path.join(self.base_dir,"output",f"screenshot_test_2.png"))
        element_3 = self.page.locator(self.locator_3)
        expect(element_3).to_be_visible()
        element_3.screenshot(path=os.path.join(self.base_dir,"output",f"screenshot_test_3.png"))

















