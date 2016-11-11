
@given("Python is installed")
def python_is_installed_impl(context):
    print ("hi")
    

@then("Python can run")
def python_can_run_impl(context):
    return True