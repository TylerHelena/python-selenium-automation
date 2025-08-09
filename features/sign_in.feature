Feature: Sign In access

  Scenario: Logged out user can access Sign In
    Given Open Target main page
    When Click Sign In from header menu
    Then Verify Sign In form opened

