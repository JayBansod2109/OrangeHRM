import re
from playwright.sync_api import Page

def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    # Wait for dashboard
    page.wait_for_url("**/dashboard/index")

    # Open user dropdown
    page.locator(".oxd-userdropdown-tab").click()

    # Click Logout
    page.get_by_role("menuitem", name="Logout").click()

    # Verify logout
    page.wait_for_url("**/auth/login")

    assert "auth/login" in page.url

