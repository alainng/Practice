Feature: Browsers can launch
	Validate that browsers work

    @browser @browser_chrome
    Scenario: Launch Chrome
        When I launch Chrome
        Then Chrome is open
        When I navigate to http://www.google.com
        Then I find element with id lst-ib
        #When I close the browser
    
    @browser @browser_firefox
    Scenario: Launch Firefox
        When I launch Firefox
        Then Firefox is open
        When I navigate to http://www.google.com
        When I close the browser
    
    @browser @browser_ie  
    Scenario: Launch IE
        When I launch IE
        Then IE is open
        Then I navigate to http://www.google.com
        When I close the browser
        
    @browser @browser_edge @wip
    Scenario: Launch Edge
        When I launch Edge
        Then Edge is open
        When I navigate to http://www.google.com
        #When I close the browser
