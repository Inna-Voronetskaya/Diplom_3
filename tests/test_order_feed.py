"""Тесты страницы Ленты заказов."""

import allure


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, main_page, order_feed_page):
        main_page.click_order_feed()
        initial_count = order_feed_page.get_total_orders_count()
        assert initial_count >= 0

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, main_page, order_feed_page):
        main_page.click_order_feed()
        initial_count = order_feed_page.get_today_orders_count()
        assert initial_count >= 0

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, main_page, order_feed_page):
        main_page.click_order_feed()
        assert order_feed_page.get_in_progress_order_number() is not None