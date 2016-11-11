Feature: Browsers can launch
	Validate that browsers work

    @browser_chrome @wip
    Scenario: Launch Chrome
        Given Chrome is installed
        When I launch Chrome
        Then Chrome is open
    
    @browser_firefox
    Scenario: Launch Firefox
        Given Firefox is installed
        When I launch Firefox
        Then Firefox is open
    
    @browser_ie  
    Scenario: Launch IE
        Given IE is installed
        When I launch IE
        Then IE is open