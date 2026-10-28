"""Базовый класс Page Object с общими методами для всех страниц."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц.

    Содержит общие методы для работы с элементами.
    Тесты НЕ должны обращаться к driver напрямую — только через методы пейджей.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Поиск и взаимодействие ---

    def find_element(self, locator):
        """Находит элемент с ожиданием его появления."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Находит список элементов с ожиданием их появления."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """Кликает по элементу с ожиданием его кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def js_click(self, locator):
        """JS-клик по элементу (обход проблем с наложением)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        """Вводит текст в поле."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    # --- Получение данных ---

    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    def get_current_url(self):
        """Возвращает текущий URL."""
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        """Возвращает значение атрибута элемента."""
        return self.find_element(locator).get_attribute(attribute)

    # --- Ожидания и проверки ---

    def wait_for_text(self, locator, text):
        """Ожидает, что текст элемента станет равным указанному."""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_url_contains(self, url_part):
        """Ожидает, что URL содержит указанную подстроку."""
        return self.wait.until(EC.url_contains(url_part))

    def is_element_visible(self, locator):
        """Проверяет, виден ли элемент."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def is_element_invisible(self, locator):
        """Проверяет, что элемент невидим (или исчез)."""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except Exception:
            return False

    # --- Скролл ---

    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента."""
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )