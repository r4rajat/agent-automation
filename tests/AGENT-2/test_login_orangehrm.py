"""
AGENT-2: Test the Login Functionality of OrangeHRM Portal

Steps to Reproduce:
* Go to https://opensource-demo.orangehrmlive.com
* Login using Credentials from MongoDB (users.credentials collection)
* Make Sure after successful login user should be able to see the dashboard
* In case of invalid credentials, verify the error message is displayed
"""

import pytest
import sys
import os
from pathlib import Path

# Add the parent directory to sys.path to import utils module
sys.path.append(str(Path(__file__).parent.parent))
from tests.utils import decode_base64


class TestOrangeHRMLogin:
    """Test cases for OrangeHRM Login functionality."""
    
    # URL of OrangeHRM portal
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    
    # User credentials fetched from MongoDB Atlas (users.credentials collection)
    CREDENTIALS = [
        {"username": "Admin", "password": "YWRtaW4xMjM="},  # Valid credentials (admin123 in base64)
        {"username": "Admin", "password": "d3JvbmdQYXNzd29yZA=="}  # Invalid credentials (wrongPassword in base64)
    ]
    
    @pytest.mark.parametrize("cred", CREDENTIALS)
    def test_login_functionality(self, page, cred):
        """
        Test login functionality with different sets of credentials.
        
        Args:
            page: Playwright page fixture
            cred: Credential dictionary with username and password
        """
        # Extract and decode credentials
        username = cred["username"]
        password = decode_base64(cred["password"])
        
        # Navigate to OrangeHRM login page
        page.goto(self.BASE_URL)
        
        # Verify login page is loaded
        assert page.title() == "OrangeHRM", "Login page title is incorrect"
        
        # Fill login form
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        
        # Click login button
        page.click('button[type="submit"]')
        
        # Check for expected outcomes based on credential validity
        if password == "admin123":  # Valid password
            # Wait for dashboard to load
            page.wait_for_selector('.oxd-topbar-header', timeout=10000)
            
            # Verify successful login by checking dashboard elements
            assert page.is_visible('.oxd-topbar-header-title'), "Dashboard not visible after login"
            assert "Dashboard" in page.text_content('.oxd-topbar-header-title'), "Dashboard title not found"
            
            print(f"✅ Successfully logged in with username: {username}")
            
        else:  # Invalid password
            # Wait for error message
            page.wait_for_selector('.oxd-alert-content', timeout=10000)
            
            # Verify error message for invalid credentials
            error_message = page.text_content('.oxd-alert-content')
            assert "Invalid credentials" in error_message, "Error message for invalid credentials not displayed"
            
            print(f"✅ Invalid login correctly rejected for username: {username}")
