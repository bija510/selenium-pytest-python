import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#py.test -v -s TestCases/S21_MouseEvent.py::test_slider
###############################################################################################
@pytest.fixture()
def setUp():
    global driver  # yield driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()

    yield
    time.sleep(2)
    driver.quit()
###############################################################################################
def test_mouseHovering(setUp):
    driver.get("https://letskodeit.teachable.com/pages/practice")
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)
    element = driver.find_element(By.ID, "mousehover")
    itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        topLink = driver.find_element(By.XPATH, itemToClickLocator)
        actions.move_to_element(topLink).click().perform()
        print("Item Clicked")
    except:
        print("Mouse Hover failed on element")
###############################################################################################
def test_dragAndDrop(setUp):
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(0)

    fromElement = driver.find_element(By.ID, "draggable")
    toElement = driver.find_element(By.ID, "droppable")
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.drag_and_drop(fromElement, toElement).perform()
        # actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
        print("Drag And Drop Element Successful")
        time.sleep(2)
    except:
        print("Drag And Drop failed on element")
###############################################################################################
def test_slider(setUp):
    driver.get("https://jqueryui.com/slider/")
    driver.switch_to.frame(0)

    element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(element, 100, 0).perform() #100=x-offset and 0=Y-offset
        print("Sliding Element Successful")
        time.sleep(2)
    except:
        #raise ValueError("Sliding failed on element") # throw ==> raise
        raise Exception("Sliding failed on element")

