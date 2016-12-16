from lib.driver import DriverFactory

# def before_all(context):
#     #setup logging
# 
def before_scenario(context,scenario):
    if 'browser' in scenario.tags:
        if 'browser_ie' in scenario.tags:
            context.browser=DriverFactory().getDriver('ie')
        elif 'browser_edge' in scenario.tags:
            context.browser=DriverFactory().getDriver('edge')
        elif 'browser_firefox' in scenario.tags:
            context.browser=DriverFactory().getDriver('firefox')
        elif 'browser_chrome' in scenario.tags:
            context.browser=DriverFactory().getDriver('chrome')
        else:
            raise ValueError('browser_ tag has a typo')

# def after_scenario(context,scenario):
# #     if hasattr(context, 'browser'):
# #         context.browser.close()

# def before_all(context):
#     #do logging stuff
# 