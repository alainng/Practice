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
    if not hasattr(context, "homepage"):
        context.homepage=HomePage(context.browser)
    context.homepage.navigate()

@when('I click on the company logo')
def step_impl(context):
    context.homepage.click_logo()

@when('I test the reservation form')
def step_impl(context):
    context.homepage.test_reservation_form()

@when('I reserve now')
def step_impl(context):
    context.homepage.now_reservation()
    
@when('I reserve later')
def step_impl(context):
    context.homepage.later_reservation()

@when('I launch header footer page')
def step_impl(context):
    if not hasattr(context, "headerfooterpage"):
        context.headerfooterpage=HeaderFooterPage(context.browser)
    context.headerfooterpage.navigate()
    
@when('I test all the header buttons')
def step_impl(context):
    #context.headerfooterpage.test_header()
    context.headerfooterpage.main_logo()
    context.headerfooterpage.comment_ca_marche()
#     context.headerfooterpage.tarifs()
#     context.headerfooterpage.se_connecter()
#     context.headerfooterpage.sinscrire()
#     context.headerfooterpage.proposer_ma_voiture()
#     