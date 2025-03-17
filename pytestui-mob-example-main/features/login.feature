Feature: Login with credentials

  Background:
    Given user is on the home screen

  Scenario Outline: login validation for valid and invalid credentials
    When user tap on option 1
    Then user is on the login screen
    When user enters username as "<username>"
    When user enters email as "<email>"
    When user enters password as "<password>"
    When user taps submit button
    Then popup_message is "<popup_message>"
    Examples:
      | username    | email                | password       | popup_message |
      | exampleName | exampleMail@test.com | examplePwd123! | success       |
      | n           | exampleMail@test.com | examplePwd123! | username_err  |
      | exampleName | exampleMailtest.com  | examplePwd123! | email_err     |
      | exampleName | exampleMail@test.com | wrongPassword  | password_err  |