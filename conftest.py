"""Фикстуры для UI-тестов Stellar Burgers."""

import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from urls import BASE_URL, LOGIN_PATH
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from helpers.data_generator import generate_random_email


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
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


@pytest.fixture
def authorized_user(driver, login_page):
    """Создает пользователя через API и логинит в браузере."""
    email = generate_random_email()
    password = "password123"
    name = "TestUser"

    response = requests.post(
        f"{BASE_URL}api/auth/register",
        json={"email": email, "password": password, "name": name},
    )
    access_token = response.json().get("accessToken")

    driver.get(f"{BASE_URL.rstrip('/')}{LOGIN_PATH}")
    login_page.login(email, password)

    yield {"email": email, "token": access_token}

    if access_token:
        requests.delete(
            f"{BASE_URL}api/auth/user",
            headers={"Authorization": access_token},
        )