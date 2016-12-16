from behave import *
from features.lib.pages import *


#https://github.com/machzqcq/Python_Page_Object/blob/master/features/lib/pages/order_confirmation_page.py


    
@when('I launch google page')
def step_impl(context):
    googlepage=GooglePage(context.browser)
    googlepage.navigate()
    googlepage.query("ipad")

@when('I launch home page')
def step_impl(context):
    homepage=HomePage(context.browser)
    homepage.navigate()
    homepage.click_logo()


# def find_element_by_id_impl(context,input_id)
