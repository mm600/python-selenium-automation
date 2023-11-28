# Created by maria at 11/27/2023
Feature: Test Scenarios for Search functionality

  Scenario: User can search for an empty cart
		Given Open Target main page
		When click on cart icon
		Then Verify “Your cart is empty” message is shown