"""Тесты основной функциональности."""

import allure
from urls import BASE_URL, ORDER_FEED_PATH


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        # Проверяем видимость элемента конструктора, а не просто URL
        assert main_page.is_constructor_visible(), "Конструктор не отображается"

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_go_to_order_feed(self, main_page):
        main_page.click_order_feed()
        assert ORDER_FEED_PATH in main_page.get_current_url()

    @allure.title("Клик на ингредиент открывает всплывающее окно")
    def test_ingredient_modal_appears(self, main_page):
        main_page.click_ingredient()
        assert main_page.is_ingredient_modal_visible()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_closes(self, main_page):
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.is_ingredient_modal_invisible()

    @allure.title("Счётчик ингредиента увеличивается при добавлении")
    def test_ingredient_counter_increases(self, main_page):
        counter_before = main_page.get_ingredient_counter()
        main_page.drag_ingredient_to_basket()
        counter_after = main_page.get_ingredient_counter()
        assert counter_after > counter_before, "Счетчик ингредиента не увеличился"