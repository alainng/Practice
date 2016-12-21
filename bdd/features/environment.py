from lib.driver import DriverFactory
import logging

# def before_all(context):
#     #setup logging
# 

def before_all(context):
    # Create logger
    #http://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
    context.logger = logging.getLogger('koolicar')
    logFormatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')    
    fileHandler = logging.FileHandler('./reports/REPLACENAME.log')   
    fileHandler.setFormatter(logFormatter)
    context.logger.addHandler(fileHandler)  
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    context.logger.addHandler(consoleHandler)   
    context.logger.setLevel(logging.DEBUG)

    context.logger.info("before_all")


def before_scenario(context,scenario):
    if 'browser' in scenario.tags:
        #isolate the browsername after "browser_" and ask for a driver with that name
        if any(tag.startswith("browser_") for tag in scenario.tags):
            indices=[matching_index for matching_index, compared_tag in enumerate(scenario.tags) if 'browser_' in compared_tag]
            browser_name=scenario.tags[indices[0]][len("browser_"):]
            context.browser=DriverFactory().create_driver(browser_name)
        else:
            raise ValueError('browser_ tag has a typo or is missing')


def after_scenario(context, scenario):

    context.logger.info("scenario status: " + scenario.status)
    
    #Screenshot example: http://stackoverflow.com/questions/3422262/take-a-screenshot-with-selenium-webdriver
#     if scenario.status == "failed":
#         if not os.path.exists("failed_scenarios_screenshots"):
#             os.makedirs("failed_scenarios_screenshots")
#         os.chdir("failed_scenarios_screenshots")
#         context.browser.save_screenshot(scenario.name + "_failed.png")

    if context.browser is not None:
        context.browser.quit()

def after_all(context):
    #todo archive screenshots
    context.logger.info("after_all")
    handlers = context.logger.handlers[:]
    for handler in handlers:
        handler.close()
        context.logger.removeHandler(handler)
    return True