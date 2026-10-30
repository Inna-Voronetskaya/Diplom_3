"""Базовый класс Page Object с общими методами для всех страниц."""

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент по локатору: {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти список элементов по локатору: {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Совершить JS-клик по элементу: {locator}")
    def js_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверить, что элемент {locator} виден")
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Проверить, что элемент {locator} невидим")
    def is_element_invisible(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except Exception:
            return False

    @allure.step("Ожидать перехода на URL: {expected_url}")
    def wait_for_url(self, expected_url):
        self.wait.until(lambda driver: driver.current_url.rstrip('/') == expected_url.rstrip('/'))

    @allure.step("Ожидать появления элемента в DOM: {locator} (таймаут {timeout} сек)")
    def wait_for_element_presence(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидать видимости элемента: {locator} (таймаут {timeout} сек)")
    def wait_for_visibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать появления текста в элементе: {locator}")
    def wait_for_text_in_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать выполнения условия (таймаут {timeout} сек)")
    def wait_for_condition(self, condition, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Перетащить элемент {source_locator} в {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const event = new DragEvent('dragstart', {bubbles: true});
            source.dispatchEvent(event);
            const drop = new DragEvent('drop', {bubbles: true});
            target.dispatchEvent(drop);
            """,
            source,
            target,
        )