import pytest
from selene import browser, config
import time


@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown():
    config.base_url = "https://demoqa.com"
    config.window_width = 1920
    config.window_height = 1080

    yield

    try:
        time.sleep(1)
        browser.driver().execute_script("""
            document.querySelectorAll('iframe, #fixedban, .adsbygoogle, .grippy-host')
                    .forEach(el => el.remove());
        """)
    except Exception as e:
        print(f"Ad removal failed: {e}")

    browser.quit()
