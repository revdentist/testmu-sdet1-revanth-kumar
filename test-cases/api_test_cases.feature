Feature: REST API Module
  As a developer
  I want to validate all API endpoints
  So that the platform data layer is reliable and secure

  Background:
    Given the API base URL is "https://jsonplaceholder.typicode.com"

  Scenario: GET all posts returns 200 with correct schema
    When the client sends GET request to "/posts"
    Then the response status should be 200
    And the response should contain a list of 100 posts
    And each post should have "id", "title", "body", "userId" fields

  Scenario: GET single post returns correct data
    When the client sends GET request to "/posts/1"
    Then the response status should be 200
    And the response "id" should equal 1

  Scenario: POST creates a new resource
    When the client sends POST request to "/posts" with valid payload
    Then the response status should be 201
    And the response should contain the created resource with an "id"

  Scenario: PUT updates an existing resource
    When the client sends PUT request to "/posts/1" with updated data
    Then the response status should be 200
    And the response should reflect the updated values

  Scenario: DELETE removes a resource
    When the client sends DELETE request to "/posts/1"
    Then the response status should be 200

  Scenario: GET nonexistent resource returns 404
    When the client sends GET request to "/posts/99999"
    Then the response status should be 404

  Scenario: Response content type is JSON
    When the client sends any GET request
    Then the response Content-Type header should contain "application/json"

  Scenario: API response time is within threshold
    When the client sends GET request to "/posts"
    Then the response time should be under 3 seconds

  Scenario: Schema validation on comments endpoint
    When the client sends GET request to "/posts/1/comments"
    Then each comment should have "id", "email", "body" fields