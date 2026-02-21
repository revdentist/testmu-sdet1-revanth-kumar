Feature: Dashboard Module
  As a logged-in user
  I want to view and interact with my dashboard
  So that I can manage and monitor my test results

  Background:
    Given the user is logged in and on the dashboard

  Scenario: Dashboard widgets load on page visit
    When the dashboard page loads
    Then all content widgets should be visible
    And no loading errors should be present

  Scenario: Dynamic content changes on refresh
    When the user refreshes the dashboard
    Then the dynamic content should update
    And new data should be displayed

  Scenario: Data table displays with correct headers
    When the user navigates to the data table
    Then the table should display headers
    And rows should be populated with data

  Scenario: Sort table by column
    When the user clicks on the "Last Name" column header
    Then the table should be sorted alphabetically
    And the first row should reflect the sorted order

  Scenario: Filter dropdown selects correct option
    When the user selects "Option 1" from the dropdown
    Then "Option 1" should be shown as selected
    And the view should update accordingly

  Scenario: Dynamic widget loads after trigger
    When the user clicks the Start button
    Then the loading spinner should appear
    And the content should load within 10 seconds

  Scenario: Permission-based visibility
    Given the user has restricted permissions
    When the dashboard loads
    Then restricted widgets should not be visible
    And only permitted content should be displayed

  Scenario: Responsive layout on smaller viewport
    When the viewport is resized to 768px width
    Then the dashboard layout should adapt responsively
    And no content should overflow or be hidden