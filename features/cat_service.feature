Feature: Cat service

  Scenario: Get all cats
    Given I have initialized the cat service
    When I request all cats
    Then I should receive a list of cats

  Scenario: Get a specific cat by ID
    Given I have initialized the cat service
    When I request a cat with ID abys
    Then I should receive the details for that cat
