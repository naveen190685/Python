@LinkedIn
Feature: Login to ConversationApp

Scenario: TC 001 : User is able to sign in and sign out of the app successfully
	Given I have launched the LinkedIn page
	And I go to Joining Page
	When I submit details "naveenK" and password "abcedfc#23"
	Then I get error "Please enter a valid email address or mobile number."
#	Then I get no error