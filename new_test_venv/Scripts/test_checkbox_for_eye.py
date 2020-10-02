from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://csssr.github.io/qa-engineer/")
browser.maximize_window()

# Кликаем на текст "НАХОДИТЬ НЕСОВЕРШЕНСТВА"
browser.find_element_by_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА").click()
#time.sleep(15)
def test_checkbox_for_eye(): #проверка для "Идеальный глазомер"

    #Два раза кликаем на "Идеальный глазомер"
    #Первый клик снимает галочку, второй возвращает
    browser.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/aside/ul/li[1]/label").click()
    browser.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/aside/ul/li[1]/label").click()

    #проверяем, что  значение атрибута галочки вернулось в checked
    check_button_eye = browser.find_element_by_xpath('//*[@id="eye"]').get_attribute("checked")
    print ("check_button_eye", check_button_eye)
    browser.close()
    assert check_button_eye is not None
