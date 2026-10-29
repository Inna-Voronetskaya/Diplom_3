"""Базовый класс Page Object с общими методами для всех страниц."""

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Поиск и взаимодействие ---

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        """Находит элемент с ожиданием его появления."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти список элементов по локатору: {locator}")
    def find_elements(self, locator):
        """Находит список элементов с ожиданием их появления."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        """Кликает по элементу с ожиданием его кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Совершить JS-клик по элементу: {locator}")
    def js_click(self, locator):
        """JS-клик по элементу (обход проблем с наложением)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def send_keys(self, locator, text):
        """Вводит текст в поле."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    # --- Получение данных ---

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        """Возвращает текущий URL."""
        return self.driver.current_url

    @allure.step("Получить атрибут '{attribute}' у элемента: {locator}")
    def get_attribute(self, locator, attribute):
        """Возвращает значение атрибута элемента."""
        return self.find_element(locator).get_attribute(attribute)

    # --- Ожидания и проверки ---

    @allure.step("Ожидать появления текста '{text}' в элементе: {locator}")
    def wait_for_text(self, locator, text):
        """Ожидает, что текст элемента станет равным указанному."""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Ожидать, что URL содержит: {url_part}")
    def wait_url_contains(self, url_part):
        """Ожидает, что URL содержит указанную подстроку."""
        return self.wait.until(EC.url_contains(url_part))

    @allure.step("Ожидать перехода на URL: {expected_url}")
    def wait_for_url(self, expected_url):
        self.wait.until(
            lambda driver: driver.current_url.rstrip('/') == expected_url.rstrip('/')
        )

    @allure.step("Проверить, что элемент {locator} виден")
    def is_element_visible(self, locator):
        """Проверяет, виден ли элемент."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Проверить, что элемент {locator} невидим")
    def is_element_invisible(self, locator):
        """Проверяет, что элемент невидим (или исчез)."""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except Exception:
            return False

    # --- Скролл ---

    @allure.step("Прокрутить страницу до элемента: {locator}")
    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента."""
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )