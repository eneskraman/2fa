import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from data import cache_purge, prod_cache, setting_screen, add_2fa, email_control, sms_control, edit_2fa_button, username_field_hub, password_field_hub, login_button_hub, preferences_hub, add_party_id


## Genel tanimlama yapilacak ornek asagida ki gibi

## burada `browser` degiskenine google chrome driver ini tanittim. 
browser = webdriver.Chrome()

## burada daha once tanimlama yaptigim `browser` degiskeninde admin.gamingtec.com u actim
browser.get ('https://admin.gamingtec.com/system/login')

time.sleep (1)


def login(user,passwd):
    # browser uzerinde username'yi buldu. datadan usernameyi alip yazdi.passwd'e atladi
    username = browser.find_element_by_xpath(username_field_hub)
    username.send_keys(user)
    #browser uzerinden password'u buldu. datadan sifreyi alip yazdi. login'e atladi
    password = browser.find_element_by_xpath(password_field_hub)
    password.send_keys(passwd)
    #browser uzerinden login'i buldu.Giris yap butonuna tikladi
    login = browser.find_element_by_xpath(login_button_hub)
    login.click()
    print('Basari ile giris yapildi!')
    time.sleep(2)

def setPartyID(party_id):
    #browser uzerinden preferences'i buldu ve tikladi.
    preferences = browser.find_element_by_xpath(preferences_hub)
    preferences.click()
    time.sleep(1)
    #partyID'yi yazacak alani aradi ve array'den aldigi ilk partID'yi ekledi, enter tusuna tikladi.
    input_party_id = browser.find_element_by_xpath(add_party_id)
    input_party_id.send_keys(party_id,Keys.ENTER)
    #cikan sonuctaki partyID'yi editle butonunu buldu ve tikladi
    edit2fa = browser.find_element_by_xpath(edit_2fa_button)
    edit2fa.click()
    time.sleep(1)
    #sms'i ortamda aradi, tikladi
    check_sms = browser.find_element_by_xpath(sms_control)
    check_sms.click()
    time.sleep(1)
    #email'i ortamda aradi, tikladi
    check_email = browser.find_element_by_xpath(email_control)
    check_email.click()
    time.sleep(1)
    # email, sms'i bulup isaretledi, ok tusuna basti
    submit_2fa = browser.find_element_by_xpath(add_2fa)
    submit_2fa.click()
    print(party_id + " 'li kullaniciya basari ile 2fa tanimlandi")
    time.sleep(2)

def purgeCache():
    #setings'i aradi, tikladi
    open_settings = browser.find_element_by_xpath(setting_screen)
    open_settings.click()
    time.sleep(1) 
    #cikan sonuclardan prod'u aradi, tikladi
    choose_env = browser.find_element_by_xpath(prod_cache)
    choose_env.click()
    time.sleep(1) 
    #prod islemini yaptiktan sonra ok tusunu aradi, tikladi ve islem sonucunu yazdi
    cache_purged = browser.find_element_by_xpath(cache_purge)
    cache_purged.click()
    print('Bahsegel prod sitesinin cerezleri temizlendi!')
    time.sleep(1)
    print('ISLEM BASARI ILE TAMAMLANDI!')



