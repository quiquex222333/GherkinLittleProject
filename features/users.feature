@users
Feature: Users

    This feature test the users response

    Scenario: Test GET users
        Given A "GET" request to "/users"
        When The request is sent
        Then The status code should be 200
        And The schema is validated with "users.json"

    Scenario: Test bad POST users
        Given A "POST" request to "/user"
        When The request is sent
        Then The status code should be 500