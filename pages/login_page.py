"""Страница авторизации Stellar Burgers."""

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import BASE_URL


class LoginPage(BasePage):
    """Класс страницы авторизации."""

    def login(self, email, password):
        """Авторизует пользователя и ждет перехода на главную."""
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        
        # Ждем, пока произойдет редирект на главную страницу
        self.wait.until(lambda driver: driver.current_url.rstrip('/') == BASE_URL.rstrip('/'))