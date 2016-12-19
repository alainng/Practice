Feature: Homepage tests
#chrome has an ssl handshake bug..tests are ~1min
#firefox takes ~8s


    @browser @browser_firefox
    Scenario: Later reservation
        When I launch home page
        #When I click on the company logo
        When I reserve later
        #When I close the browser
    
    @browser @browser_firefox
    Scenario: now reservation
        When I launch home page
        #When I click on the company logo
        When I reserve now
        #When I close the browser
    
