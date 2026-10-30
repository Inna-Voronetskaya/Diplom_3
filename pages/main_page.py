"""Главная страница Stellar Burgers (Конструктор)."""

import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Кликнуть по кнопке «Конструктор»")
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть по кнопке «Лента Заказов»")
    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

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
        self.drag_and_drop(MainPageLocators.INGREDIENT_ITEM, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step("Нажать кнопку «Оформить заказ»")
    def click_checkout_button(self):
        self.js_click(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        self.wait_for_text_in_element(MainPageLocators.ORDER_NUMBER_MODAL)
        order_number_text = self.get_text(MainPageLocators.ORDER_NUMBER_MODAL)
        
        self.close_modal()
        self.is_element_invisible(MainPageLocators.MODAL_OVERLAY)
        
        return ''.join(filter(str.isdigit, order_number_text))