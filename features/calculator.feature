Feature: Verify calculator functionalities
    Scenario: Addition
		Given I have a calculator
		When I input + as the operation
		And I input 10 as the first number
		And I input 5 as the second number
		Then the result should be 15

    Scenario: Subtraction
		Given I have a calculator
		When I input - as the operation
		And I input 10 as the first number
		And I input 5 as the second number
		Then the result should be 5

    Scenario: Multiplication
		Given I have a calculator
		When I input * as the operation
		And I input 10 as the first number
		And I input 5 as the second number
		Then the result should be 50

    Scenario: Division
		Given I have a calculator
		When I input / as the operation
		And I input 10 as the first number
		And I input 5 as the second number
		Then the result should be 2		

    Scenario: Trigonometry - cos
		Given I have a calculator
		When I input cos as the operation
		And I input 0 as the first number
		Then the result should be 1

    Scenario: Trigonometry - sin
		Given I have a calculator
		When I input sin as the operation
		And I input 90 as the first number
		Then the result should be 1

    Scenario: Trigonometry - tan
		Given I have a calculator
		When I input tan as the operation
		And I input 45 as the first number
		Then the result should be 0.9999999999999999				