"""Страница Ленты заказов Stellar Burgers."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.order_feed_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    """Класс страницы Ленты заказов."""

    @allure.step("Получить счетчик «Выполнено за все время»")
    def get_total_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить счетчик «Выполнено за сегодня»")
    def get_today_orders_count(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Ожидать появления заказа {order_number} в ленте")
    def wait_for_order_on_page(self, order_number):
        # Ищем текст с номером заказа на всей странице (в общей ленте)
        locator = (By.XPATH, f"//*[contains(text(), '{order_number}')]")
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))