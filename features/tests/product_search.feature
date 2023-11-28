Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


	Scenario Outline: User can search for an empty cart
		Given Open Target main page
		When click on cart icon
		Then Verify “Your cart is empty” message is shown
