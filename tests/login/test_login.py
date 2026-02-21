import pytest
from playwright.sync_api import Page, expect

class TestLogin:
    """
    Login module tests against the-internet.herokuapp.com/login
    Covers: valid login, invalid credentials, empty fields, 
    error messages, and successful logout
    """

    def test_valid_login(self, page: Page, base_url, credentials):
        """Valid credentials should redirect to secure area"""
        page.goto(f"{base_url}/login")
        page.fill("#username", credentials["username"])
        page.fill("#password", credentials["password"])
        page.click("button[type='submit']")
        
        expect(page).to_have_url(f"{base_url}/secure")
        expect(page.locator(".flash.success")).to_be_visible()

    def test_invalid_username(self, page: Page, base_url):
        """Invalid username should show error message"""
        page.goto(f"{base_url}/login")
        page.fill("#username", "wronguser")
        page.fill("#password", "SuperSecretPassword!")
        page.click("button[type='submit']")
        
        expect(page.locator(".flash.error")).to_be_visible()
        expect(page.locator(".flash.error")).to_contain_text("Your username is invalid")

    def test_invalid_password(self, page: Page, base_url):
        """Invalid password should show error message"""
        page.goto(f"{base_url}/login")
        page.fill("#username", "tomsmith")
        page.fill("#password", "wrongpassword")
        page.click("button[type='submit']")
        
        expect(page.locator(".flash.error")).to_be_visible()
        expect(page.locator(".flash.error")).to_contain_text("Your password is invalid")

    def test_empty_credentials(self, page: Page, base_url):
        """Empty fields should show validation error"""
        page.goto(f"{base_url}/login")
        page.click("button[type='submit']")
        
        expect(page.locator(".flash.error")).to_be_visible()

    def test_successful_logout(self, page: Page, base_url, credentials):
        """After login, user should be able to logout successfully"""
        page.goto(f"{base_url}/login")
        page.fill("#username", credentials["username"])
        page.fill("#password", credentials["password"])
        page.click("button[type='submit']")
        
        page.click(".button.secondary")
        expect(page).to_have_url(f"{base_url}/login")
        expect(page.locator(".flash.success")).to_contain_text("You logged out")

    def test_login_page_elements_visible(self, page: Page, base_url):
        """Login page should have all required UI elements"""
        page.goto(f"{base_url}/login")
        
        expect(page.locator("#username")).to_be_visible()
        expect(page.locator("#password")).to_be_visible()
        expect(page.locator("button[type='submit']")).to_be_visible()