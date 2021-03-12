@books
Feature: Books

    This feature test the books response

    Scenario: Test GET books
        Given A "GET" request to "/books"
        When The request is sent
        Then The status code should be 200
        And The schema is validated with "books.json"

    Scenario: Test bad POST book
        Given A "POST" request to "/book"
        When The request is sent
        Then The status code should be 500