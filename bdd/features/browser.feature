Feature: Homepage tests


    @browser @browser_chrome
    Scenario: Later reservation
        When I launch home page
        #When I click on the company logo
        When I reserve later
        #When I close the browser
    
    @browser @browser_chrome
    Scenario: now reservation
        When I launch home page
        #When I click on the company logo
        When I reserve now
        #When I close the browser
    
