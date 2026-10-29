"""Страница авторизации."""

import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import BASE_URL


class LoginPage(BasePage):
    """Класс страницы авторизации."""

    @allure.step("Авторизоваться с email: {email}")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        # Используем js_click, чтобы оверлей не перекрывал кнопку
        self.js_click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url(BASE_URL)