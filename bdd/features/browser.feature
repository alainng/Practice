Feature: Browsers can launch
	Validate that browsers work

    @browser_chrome @wip
    Scenario: Launch Chrome
        When I launch Chrome
        And I navigate to http://www.google.com
        Then Chrome is open
    
    @browser_firefox
    Scenario: Launch Firefox
        When I launch Firefox
        Then Firefox is open
    
    @browser_ie  
    Scenario: Launch IE
        When I launch IE
        Then IE is open