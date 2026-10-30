"""Генерация тестовых данных."""

import uuid


def generate_random_email():
    """Генерирует уникальный email."""
    return f"test_{uuid.uuid4().hex[:8]}@yandex.ru"