Feature: Login Module
  As a user of TestMu AI platform
  I want to securely log in and out
  So that I can access my test management dashboard

  Background:
    Given the user is on the login page

  Scenario: Valid login with correct credentials
    When the user enters valid username "tomsmith"
    And the user enters valid password "SuperSecretPassword!"
    And the user clicks the login button
    Then the user should be redirected to the secure area
    And a success message should be displayed

  Scenario: Invalid login with wrong username
    When the user enters invalid username "wronguser"
    And the user enters password "SuperSecretPassword!"
    And the user clicks the login button
    Then an error message "Your username is invalid" should be displayed
    And the user should remain on the login page

  Scenario: Invalid login with wrong password
    When the user enters username "tomsmith"
    And the user enters invalid password "wrongpassword"
    And the user clicks the login button
    Then an error message "Your password is invalid" should be displayed

  Scenario: Login with empty credentials
    When the user clicks the login button without entering credentials
    Then a validation error should be displayed

  Scenario: Successful logout after login
    Given the user is logged in
    When the user clicks the logout button
    Then the user should be redirected to the login page
    And a logout success message should be displayed

  Scenario: Session expiry redirects to login
    Given the user is logged in
    When the session expires
    Then the user should be redirected to the login page
    And a session expired message should be displayed

  Scenario: Brute force lockout after multiple failed attempts
    When the user enters wrong credentials 5 times consecutively
    Then the account should be temporarily locked
    And a lockout message should be displayed