import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    deriver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
