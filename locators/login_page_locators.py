"""Локаторы страницы авторизации."""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы элементов на странице авторизации."""

    # Форма входа
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылки
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")