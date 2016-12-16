Feature: Browsers can launch
	Validate that browsers work

    @browser @browser_chrome
    Scenario: Launch Chrome
        When I launch google page
#        Then I find element with id lst-ib
        #When I close the browser
    
    @browser @browser_firefox
    Scenario: Launch Firefox
        When I navigate to http://www.google.com
    
    @browser @browser_ie  
    Scenario: Launch IE
        Then I navigate to http://www.google.com
        
    @browser @browser_edge @wip
    Scenario: Launch Edge
        When I navigate to http://www.google.com
        #When I close the browser
