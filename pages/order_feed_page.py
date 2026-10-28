"""Страница Ленты заказов Stellar Burgers."""

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    """Класс страницы Ленты заказов."""

    def get_total_orders_count(self):
        """Возвращает значение счётчика «Выполнено за все время»."""
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_orders_count(self):
        """Возвращает значение счётчика «Выполнено за сегодня»."""
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    def get_in_progress_order_number(self):
        """Возвращает номер заказа в разделе «В работе»."""
        return self.get_text(OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBER)