#coding = UTF-8
from selenium.webdriver.common.by import By
from features.lib.pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self,context):
        super(RegisterPage,self).__init__(context.driver)

    def send_user_email(self,useremail):
        self.find_element(By.ID,'register_email').send_keys(useremail)

    def send_user_name(self,username):
        self.find_element(By.ID,'register_nickname').send_keys(username)

    def send_user_password(self,password):
        self.find_element(By.ID,'register_password').send_keys(password)

    def send_code(self,code):
        self.find_element(By.ID,'captcha_code').send_keys(code)

    def click_button(self):
        self.find_element(By.ID,'register-btn').click()

    def get_code_text(self):
        return self.find_element(By.ID,'captcha_code-error').text