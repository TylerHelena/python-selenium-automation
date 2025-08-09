Feature: Terms & Conditions from Sign In

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target sign in page
    When Store original window
    And Click on Terms & Conditions link
    And Switch to the newly opened window
    Then Verify Terms & Conditions page is opened
    And Close new window and switch back to original

    