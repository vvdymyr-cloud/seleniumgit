import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = Options()
    # КРИТИЧНО ДЛЯ CI/CD: запуск без графічного вікна
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
