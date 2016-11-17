Feature: Browsers can launch
	Validate that browsers work

    @browser @browser_chrome
    Scenario: Launch Chrome
        When I launch Chrome
        And I navigate to http://www.google.com
        Then Chrome is open
        When I close the browser
    
    @browser @browser_firefox
    Scenario: Launch Firefox
        When I launch Firefox
        And I navigate to http://www.google.com
        Then Firefox is open
        When I close the browser
    
    @browser @browser_ie  
    Scenario: Launch IE
        When I launch IE
        And I navigate to http://www.google.com
        Then IE is open
        When I close the browser
        
    @browser@browser_edge @wip
    Scenario: Launch Chrome
        When I launch Edge
        And I navigate to http://www.google.com
        Then Edge is open
        When I close the browser
