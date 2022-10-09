Feature: User is able to search, filter and add products to cart
  Scenario: Search on Amazon site using the keyword Teddy bear, filter and add products to cart
    Given Launch Amazon on a browser
    When Search using the keyword "Teddy bear"
    Then Sorts the result according to Customer Review
    And Selects the Age range between 5 to 7 years old
    And Add first two products to cart
    And Validate presence of those products to cart