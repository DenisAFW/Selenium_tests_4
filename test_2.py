# Условие: Добавить в проект тесты API, написанные в ходе первого семинара.
# Доработать эти тесты в едином стиле с тестами UI, добавив логирование и обработку ошибок.
# Должен получиться единый тестовый проект.
from testpage import OperationsHelper
import logging
import yaml
with open('testdata.yaml') as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Start 1 test")
    testpage = OperationsHelper(browser)
    assert "Молоко" in testpage.spell_the_word("Малоко"), "Test 1 FAIL"


def test_step2(browser):
    logging.info("Start 2 test")
    testpage = OperationsHelper(browser)
    testpage.click_alert()
    testpage.go_to_site()
    testpage.short_pause()
    assert "hw1" not in testpage.success_delete(), "Test 2 FAIL"

