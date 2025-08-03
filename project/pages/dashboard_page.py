# project/pages/dashboard_page.py
from playwright.sync_api import Page, expect

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.profile = page.locator('#usernameDisplay')
        self.logout = page.locator('#logout')


    def assert_welcome_message(self, message):
        expect(self.profile).to_have_text(message)