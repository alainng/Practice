Feature: Environment is setup to specifications
	Tests to validate that all the necessary components are installed

	@setup
    Scenario: Python is setup
        Given Python is installed
        Then Python can run