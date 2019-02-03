Feature: CPU cores count

Scenario: Count no of CPU cores
	Given I'm logged onto computer
	When I count no of CPU cores
	Then I have no of cores equal to 2.
