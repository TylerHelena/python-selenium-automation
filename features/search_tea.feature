Feature: Search for tea on Target website

  Scenario: User searches for tea
    Given the user is on the Target homepage
    When the user searches for "tea"
    Then Verify search results contain the word "tea"
    And Verify that every product has a name and an image
