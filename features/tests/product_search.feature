Feature: Target Product Search

  Scenario Outline: Search for a product on Target
    Given the user is on the Target homepage
    When the user searches for "<product>"
    Then they should see results for "<product>"

  Examples:
    | product |
    | shoes   |
    | laptop  |
    | makeup  |

