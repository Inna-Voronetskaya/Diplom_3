"""Локаторы главной страницы Stellar Burgers."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов на главной странице."""

    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Ингредиенты
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")

    # Область конструктора (для drag-and-drop)
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")

    # Заголовок модального окна (с названием ингредиента)
    MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")