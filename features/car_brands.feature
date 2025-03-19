Feature: Check if car brands are sorted alphabetically

  Background:
    Given user is on the home screen

  @list
  Scenario: Check if car brands are sorted alphabetically
    When user tap on option 2
    Then user is on list screen
    Then verify list is displayed in alphabetical order
