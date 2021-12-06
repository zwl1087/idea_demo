from selenium import webdriver
import pytest
import logging

@pytest.fixture(scope="class")
def open_browser():
    logging.info("pytest.fixture open_browser start now : open a new browser ")
    dirver = webdriver.Chrome()
    dirver.implicitly_wait(5)
    yield dirver
    logging.info("pytest.fixture open_browser end now : close browser ")
    dirver.close()
