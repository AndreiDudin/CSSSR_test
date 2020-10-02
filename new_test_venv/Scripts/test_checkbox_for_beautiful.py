from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://csssr.github.io/qa-engineer/")
browser.maximize_window()

# Кликаем на текст "НАХОДИТЬ НЕСОВЕРШЕНСТВА"
browser.find_element_by_link_text("НАХОДИТЬ НЕСОВЕРШЕНСТВА").click()

def test_checkbox_for_beautiful():

    #Два раза кликаем на "Чувство прекрасного"
    #Первый клик снимает галочку, второй возвращает
    browser.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/aside/ul/li[2]/label").click()
    browser.find_element_by_xpath("/html/body/div[1]/section[3]/div[2]/aside/ul/li[2]/label").click()

    #проверяем, что  значение атрибута галочки вернулось в checked
    check_button_beautiful = browser.find_element_by_xpath('//*[@id="beautiful"]').get_attribute("checked")
    browser.close()
    assert check_button_beautiful is not None
