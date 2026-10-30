"""URL-адреса и пути приложения Stellar Burgers.

Все URL вынесены в константы, чтобы при смене окружения (dev/prod)
достаточно было изменить BASE_URL в одном месте.
"""

# Базовый URL приложения
BASE_URL = "https://qa-stellarburgers.education-services.ru/"

# Пути страниц
ORDER_FEED_PATH = "/feed"
LOGIN_PATH = "/login"
REGISTER_PATH = "/register"
FORGOT_PASSWORD_PATH = "/forgot-password"
RESET_PASSWORD_PATH = "/reset-password"
PROFILE_PATH = "/account/profile"
ORDERS_HISTORY_PATH = "/account/order-history"