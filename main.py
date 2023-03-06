from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
driver = webdriver.Chrome()
driver.get('https://monkeytype.com/')


print('starting!')

driver.execute_script("""
    function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
        currentDate = Date.now();
    } while (currentDate - date < milliseconds);
    }

   var l = document.getElementById("cookiePopup")
   l.parentNode.removeChild(l);

   sleep(0.5)

  var l = document.getElementById("cookiePopupWrapper")
  l.parentNode.removeChild(l);

   
""")


def TypeWords():
    words = driver.find_elements_by_class_name("word")
    for word in words:
        keyboard.type(word.text)   
        time.sleep(0.03)

        # Press space
        keyboard.press(Key.space)
        keyboard.release(Key.space) 


def ClickWordButton():
    elements = driver.find_elements_by_class_name("textButton")
    for element in elements:
        mode = element.get_attribute('mode')
        if (mode == "words"):
            element.click()
            break

def Click100Button():
    elements = driver.find_elements_by_class_name("textButton")
    for element in elements:
        wc = element.text
        if (wc == "100"):
            element.click()
            break

def Main():
    ClickWordButton()
    Click100Button()

    time.sleep(2)
    TypeWords()


Main()