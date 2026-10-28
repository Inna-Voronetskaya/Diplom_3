"""Локаторы страницы Ленты заказов."""

from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    """Локаторы элементов на странице Ленты заказов."""

    # Заголовок страницы
    PAGE_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # Счётчики выполненных заказов (гибкий поиск)
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за') and contains(text(), 'время')]/following-sibling::p"
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Выполнено за') and contains(text(), 'сегодня')]/following-sibling::p"
    )

    # Список заказов в работе
    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")