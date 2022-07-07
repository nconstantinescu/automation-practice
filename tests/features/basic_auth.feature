Feature: Basic Authentication


  Background:
    Given the Javascript login form appears upon loading "Basic Auth"

  Scenario Outline: Incorrect username and password combination
    When the user inputs the incorrect "<username>" and "<password>" combination
    Then the Javascript login form remains on the screen

    Examples: User Pass combo
      | username | password |
      | test     | admin    |
      | admin    | ADMIN    |


  Scenario: Correct user password combination
    When the user inputs the correct username and password combination
    Then a simple JavaScript alert is triggered and interacteble

  Scenario: Selecting the Cancel button
    When the cancel button from the login form is clicked
    Then the "Not authorized" message appears on the screen
