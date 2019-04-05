#coding = UTF-8
from behave import *
from features.lib.pages.register_page import RegisterPage

use_step_matcher('re')

@when('I open the register website "([^"]*)"')
def step_register(context,url):
    RegisterPage(context).get_url(url)
    #context.driver.get(url)

@Then('I except that the title is "([^"]*)"')
def step_register1(context,title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title

@When('I set with useremail "([^"]*)"')
def step_register2(context,useremail):
    #context.driver.find_element_by_id('register_email').send_keys(useremail)
    RegisterPage(context).send_user_email(useremail)

@When('I set with username "([^"]*)"')
def step_register3(context,username):
    RegisterPage(context).send_user_name(username)

@When('I set with password "([^"]*)"')
def step_register4(context,password):
    RegisterPage(context).send_user_password(password)

@When('I set with code "([^"]*)"')
def step_register5(context,password):
    RegisterPage(context).send_code(password)

@When('I click with registerbutton')
def step_register6(context):
    RegisterPage(context).click_button()

@Then('I except that text "([^"]*)"')
def step_register7(context,code_text):
    text = RegisterPage(context).get_code_text()
    assert code_text in text