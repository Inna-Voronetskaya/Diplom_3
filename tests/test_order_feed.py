"""Тесты страницы Ленты заказов."""

import allure


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается при создании заказа")
    def test_total_orders_counter_increases(self, driver, authorized_user, main_page, order_feed_page):
        main_page.click_order_feed()
        initial_count = order_feed_page.get_total_orders_count()

        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.click_checkout_button()
        main_page.get_order_number_from_modal()

        main_page.click_order_feed()
        new_count = order_feed_page.get_total_orders_count()

        assert new_count > initial_count, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается при создании заказа")
    def test_today_orders_counter_increases(self, driver, authorized_user, main_page, order_feed_page):
        main_page.click_order_feed()
        initial_count = order_feed_page.get_today_orders_count()

        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.click_checkout_button()
        main_page.get_order_number_from_modal()

        main_page.click_order_feed()
        new_count = order_feed_page.get_today_orders_count()

        assert new_count > initial_count, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver, authorized_user, main_page, order_feed_page):
        main_page.click_constructor()
        main_page.drag_ingredient_to_basket()
        main_page.click_checkout_button()
        
        order_number = main_page.get_order_number_from_modal()

        main_page.click_order_feed()
        
        # Ждем появления нашего номера заказа на странице ленты
        order_feed_page.wait_for_order_on_page(order_number)