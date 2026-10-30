"""Локаторы страницы Ленты заказов."""

from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за') and contains(text(), 'время')]/following-sibling::p"
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за') and contains(text(), 'сегодня')]/following-sibling::p"
    )
    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    
    # Используем точку (.), чтобы найти текст на любом уровне вложенности li
    ORDER_IN_PROGRESS_TEMPLATE = "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{}')]"