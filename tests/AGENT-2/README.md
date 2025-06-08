# AGENT-2: OrangeHRM Login Test

This test automates the login functionality of the OrangeHRM portal as specified in JIRA ticket AGENT-2.

## Test Description

Tests the login functionality of OrangeHRM Portal with both valid and invalid credentials.

## Test Steps

1. Navigate to the OrangeHRM demo site: https://opensource-demo.orangehrmlive.com/
2. Attempt login with credentials from the MongoDB Atlas (users.credentials collection)
3. Verify successful login for valid credentials by checking for the dashboard
4. Verify failed login for invalid credentials by checking for the error message

## Credentials Used

The test uses two sets of credentials:
1. Valid credentials: Username: "Admin", Password: "admin123" (base64 encoded)
2. Invalid credentials: Username: "Admin", Password: "wrongPassword" (base64 encoded)

## Running the Test

```bash
# Install required dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

# Run the specific test
pytest tests/AGENT-2/test_login_orangehrm.py -v
```
