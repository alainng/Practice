Feature: Requests are tested
	Trigger different types of calls
	
	@api
    Scenario: Simple webpage request and response test
        When I request get "https://api.github.com/events"
        Then I expect a good response
    
#    Scenario: Get request
#        When I request post https://api.github.com/events
#        Then I expect a 200 response
#        
	@api
    Scenario: Post request
    	Given url parameters
    		| key  | value  |
    		| key1 | value1 |
    		| key2 | value2 |    		
        When I request post "https://api.github.com/events"
        Then I expect a good response