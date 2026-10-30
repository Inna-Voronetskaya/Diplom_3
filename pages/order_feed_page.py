"""Страница Ленты заказов Stellar Burgers."""

import allure
from selenium.webdriver.common.by import By
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Получить счетчик «Выполнено за все время»")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить счетчик «Выполнено за сегодня»")
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Ожидать, что счетчик «Выполнено за все время» увеличится")
    def wait_for_total_orders_counter_increase(self, initial_count, timeout=10):
        self.wait_for_condition(lambda driver: self.get_total_orders_count() > initial_count, timeout)

    @allure.step("Ожидать, что счетчик «Выполнено за сегодня» увеличится")
    def wait_for_today_orders_counter_increase(self, initial_count, timeout=10):
        self.wait_for_condition(lambda driver: self.get_today_orders_count() > initial_count, timeout)

    @allure.step("Получить список заказов в разделе «В работе»")
    def get_in_progress_orders(self):
        elements = self.find_elements(OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBER)
        return [element.text.strip() for element in elements]

    @allure.step("Ожидать появления заказа {order_number} в разделе «В работе»")
    def wait_for_order_in_progress(self, order_number, timeout=60):
        locator = (
            By.XPATH, 
            OrderFeedPageLocators.ORDER_IN_PROGRESS_TEMPLATE.format(order_number)
        )
        self.wait_for_visibility(locator, timeout)