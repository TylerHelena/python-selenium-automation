Feature: Add product to cart

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for "tea" from header
    And Open first product from results
    And Add product to cart
    Then Verify cart has at least one item
