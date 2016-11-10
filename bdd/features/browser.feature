Feature: Browsers can launch

    @test
    Scenario: Launch Chrome
        Given Chrome is installed
        When I launch Chrome
        Then Chrome is open
        
    Scenario: Launch Firefox
        Given Firefox is installed
        When I launch Firefox
        Then Firefox is open
        
    Scenario: Launch IE
        Given IE is installed
        When I launch IE
        Then IE is open