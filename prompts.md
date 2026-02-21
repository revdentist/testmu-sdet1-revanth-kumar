# Prompts Used for Test Case Generation
## Task 2 — Prompt Engineering Log

All prompts are recorded exactly as written, including failed attempts.

---

## Module 1: Login

### Attempt 1 (Too Vague — Did Not Work Well)
```
Write test cases for a login page.
```
**What went wrong:** Output was too generic. Covered only happy path.
No edge cases, no error message validation, no session handling.

### Attempt 2 (Better Structure — Partially Worked)
```
Write Gherkin test cases for a login module. 
Include valid login, invalid credentials, and empty fields.
```
**What went wrong:** Still missing brute force lockout and session expiry.
Error message text was not specific enough to be usable in assertions.

### Attempt 3 (Final — Used This)
```
You are a senior QA engineer working on a web-based test management platform.

Write comprehensive Gherkin test cases for the Login module.
The app uses standard username/password authentication.

Cover ALL of the following scenarios:
1. Valid login with correct credentials
2. Invalid login with wrong username
3. Invalid login with wrong password  
4. Login with empty credentials
5. Successful logout
6. Session expiry redirecting to login
7. Brute force lockout after 5 failed attempts

For each scenario:
- Use realistic test data
- Include specific error message text in Then steps
- Follow Given/When/Then format strictly
- Add a Background block for shared preconditions

Output only the .feature file content, no explanation.
```
**What worked:** All 7 scenarios covered. Error messages specific.
Background block kept scenarios clean. Output was directly usable.

---

## Module 2: Dashboard

### Attempt 1 (Too Vague — Did Not Work Well)
```
Generate test cases for a dashboard page.
```
**What went wrong:** Only generated 3 generic test cases.
No dynamic content, no sorting, no permission-based visibility.

### Attempt 2 (Added Context — Partially Worked)
```
Write Gherkin test cases for a dashboard with widgets,
tables, filters and dropdowns.
```
**What went wrong:** Better but scenarios were shallow.
No responsive layout testing, no dynamic loading scenarios.
Then steps were not assertable — too vague.

### Attempt 3 (Final — Used This)
```
You are a senior QA engineer on an AI test management platform.

Write Gherkin test cases for the Dashboard module.
The dashboard contains: dynamic content widgets, sortable data tables,
filter dropdowns, dynamic loading elements, and permission-based UI.

Cover ALL of the following:
1. Widget loading on page visit
2. Dynamic content changing on refresh
3. Data table displaying with correct headers and rows
4. Sorting table by column header click
5. Filter dropdown selecting correct option
6. Dynamic widget loading after user trigger
7. Permission-based visibility (restricted vs permitted content)
8. Responsive layout at 768px viewport

Requirements:
- Each scenario must have specific, assertable Then steps
- Use Background block for shared login precondition
- Keep scenarios independent of each other

Output only the .feature file, no explanation.
```
**What worked:** All 8 scenarios generated correctly.
Then steps were specific and assertable. Background kept it DRY.

---

## Module 3: REST API

### Attempt 1 (Too Vague — Did Not Work Well)
```
Write API test cases for a REST API.
```
**What went wrong:** Generated only GET and POST.
No schema validation, no error handling, no response time checks.

### Attempt 2 (Added Scenarios — Partially Worked)
```
Write Gherkin test cases for REST API including CRUD operations
and error handling.
```
**What went wrong:** CRUD was covered but schema validation
was missing. 4xx error handling only covered 404, not others.
No response time or content-type validation.

### Attempt 3 (Final — Used This)
```
You are a senior QA engineer validating a REST API.
Base URL: https://jsonplaceholder.typicode.com

Write Gherkin test cases covering:
1. GET all resources — status 200, correct schema
2. GET single resource — status 200, correct data
3. POST create resource — status 201, returns created object with id
4. PUT update resource — status 200, reflects changes
5. DELETE resource — status 200
6. GET nonexistent resource — status 404
7. Response Content-Type header validation
8. Response time under 3 seconds threshold
9. Schema validation on nested endpoint (comments)

Requirements:
- Include expected status codes in Then steps
- Include schema field names in assertions
- Add Background block with base URL
- Each scenario must be independently runnable

Output only the .feature file content, no explanation.
```
**What worked:** All 9 scenarios covered with specific assertions.
Schema field names included. Status codes explicit in every Then step.