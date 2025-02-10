import pytest
from selene import browser


def pytest_addoption(parser):
    """Добавляем опции для изменения размера окна"""
    parser.addoption("--width", action="store", default=1280, help="Width of the browser window")
    parser.addoption("--height", action="store", default=720, help="Height of the browser window")


@pytest.fixture(scope="function", autouse=True)
def setup_browser(pytestconfig):
    """Фикстура для настройки размера окна браузера"""
    width = pytestconfig.getoption("--width")
    height = pytestconfig.getoption("--height")

    browser.config.window_width = int(width)
    browser.config.window_height = int(height)

    yield
    browser.quit()