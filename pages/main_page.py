"""Главная страница Stellar Burgers (Конструктор)."""

import time
import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс главной страницы (Конструктор)."""

    @allure.step("Кликнуть по кнопке «Конструктор»")
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть по кнопке «Лента Заказов»")
    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)
        # Ждем, пока URL сменится на /feed
        self.wait_url_contains("/feed")

    @allure.step("Кликнуть по ингредиенту")
    def click_ingredient(self):
        self.js_click(MainPageLocators.INGREDIENT_ITEM)

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_invisible(self):
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)

    @allure.step("Проверить, что конструктор отображается")
    def is_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step("Перетащить ингредиент в корзину")
    def drag_ingredient_to_basket(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        basket = self.find_element(MainPageLocators.CONSTRUCTOR_BASKET)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ingredient)
        self.driver.execute_script(
            """
            const ingredient = arguments[0];
            const basket = arguments[1];
            const event = new DragEvent('dragstart', {bubbles: true});
            ingredient.dispatchEvent(event);
            const drop = new DragEvent('drop', {bubbles: true});
            basket.dispatchEvent(drop);
            """,
            ingredient,
            basket,
        )
        time.sleep(1)

    @allure.step("Нажать кнопку «Оформить заказ»")
    def click_checkout_button(self):
        checkout_locator = (By.XPATH, "//button[text()='Оформить заказ']")
        self.js_click(checkout_locator)
        time.sleep(2) # Ждем, пока пройдет запрос на создание заказа

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        order_number_locator = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
        # Ждем, пока в заголовке модалки появится текст (номер)
        self.wait.until(lambda driver: len(self.get_text(order_number_locator)) > 0)
        order_number_text = self.get_text(order_number_locator)
        
        # Закрываем модалку и ЖДЕМ, пока она исчезнет (исчезнет оверлей)
        self.close_modal()
        self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)
        time.sleep(1) 
        
        return ''.join(filter(str.isdigit, order_number_text))