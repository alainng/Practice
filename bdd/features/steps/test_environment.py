
@when("I print hi")
def simple_print(context):
    print ("hi")
    

@then("I should see hi")
def simple_truth(context):
    return True