Feature: Product Search

  Scenario: User can search for a product and see results
    Given the user is on the Target homepage
    When the user searches for "tea"
    Then Verify that every product has a name and an image