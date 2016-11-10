


@given("Chrome is installed"):
def is_chrome_installed(context):
    return True



@when("I print hi")
def simple_print(context):
    print ("hi")
    

@then("I should see hi")
def simple_truth(context):
    return True