# ******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ******************************************************************************

import pytest
from appium import webdriver


class SimpleCalculatorTests:
    def __init__(self):
        print("driver will be created")
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps)

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is ")
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


# Arrange
@pytest.fixture
def calc():
    opened_drivers = []

    def _calc():
        operatie = SimpleCalculatorTests()
        opened_drivers.append(operatie)
        return operatie

    yield _calc
    for drv in opened_drivers:
        drv.driver.quit()


def test_subtract(calc):
    # Act
    calc = calc()
    button_list  = ["Seven", "Seven", "Minus", "One", "Zero", "Zero", "Equals"]
    for button in button_list:
        calc.driver.find_element_by_name(button).click()

    # Assert
    print(calc.getresults())
    assert calc.getresults() == "-23"


def test_addition(calc):
    # Act
    calc = calc()
    calc.driver.find_element_by_name("One").click()
    calc.driver.find_element_by_name("Plus").click()
    calc.driver.find_element_by_name("Seven").click()
    calc.driver.find_element_by_name("Equals").click()
    # Assert
    print(calc.getresults())
    assert calc.getresults() == "8"
