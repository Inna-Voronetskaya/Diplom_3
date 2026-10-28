"""Фикстуры для UI-тестов Stellar Burgers."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from urls import BASE_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура браузера с параметризацией Chrome + Firefox."""
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)