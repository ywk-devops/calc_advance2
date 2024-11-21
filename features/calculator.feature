Feature: Calculator
  Validate all arithmetic and trigonometric operations provided by the calculator.

  Scenario: Addition
    Given the calculator is initialized
    When I add 10 and 5
    Then the result should be 15

  Scenario: Subtraction
    Given the calculator is initialized
    When I subtract 10 from 20
    Then the result should be 10

  Scenario: Multiplication
    Given the calculator is initialized
    When I multiply 6 and 7
    Then the result should be 42

  Scenario: Division
    Given the calculator is initialized
    When I divide 10 by 2
    Then the result should be 5.0

  Scenario: Sine
    Given the calculator is initialized
    When I calculate the sine of 30
    Then the result should be 0.5

  Scenario: Cosine
    Given the calculator is initialized
    When I calculate the cosine of 60
    Then the result should be 0.5

  Scenario: Tangent
    Given the calculator is initialized
    When I calculate the tangent of 45
    Then the result should be 1.0
