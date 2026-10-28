"""Главная страница Stellar Burgers (Конструктор)."""

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Класс главной страницы (Конструктор)."""

    def click_constructor(self):
        """Клик по кнопке «Конструктор»."""
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        """Клик по кнопке «Лента Заказов»."""
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        """Клик по первому ингредиенту."""
        self.js_click(MainPageLocators.INGREDIENT_ITEM)

    def is_ingredient_modal_visible(self):
        """Проверяет, что модальное окно открыто."""
        return self.is_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def is_ingredient_modal_invisible(self):
        """Проверяет, что модальное окно закрыто."""
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    def close_modal(self):
        """Закрывает модальное окно."""
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def get_ingredient_counter(self):
        """Возвращает значение счётчика ингредиента."""
        ingredient = self.find_element(MainPageLocators.INGREDIENT_ITEM)
        counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)