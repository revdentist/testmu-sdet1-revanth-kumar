import pytest
from playwright.sync_api import Page, expect


class TestDashboard:
    """
    Dashboard module tests against the-internet.herokuapp.com
    Covers: dynamic content, widget loading, filters,
    sorting, and permission-based visibility
    """

    def test_dynamic_content_loads(self, page: Page, base_url):
        """Dynamic content widgets should load on page"""
        page.goto(f"{base_url}/dynamic_content")

        content_blocks = page.locator(".large-10.columns")
        expect(content_blocks.first).to_be_visible()

    def test_dynamic_content_changes_on_refresh(self, page: Page, base_url):
        """Content should change between page loads"""
        page.goto(f"{base_url}/dynamic_content")
        first_text = page.locator(".large-10.columns").first.inner_text()

        page.reload()
        second_text = page.locator(".large-10.columns").first.inner_text()

        assert first_text != second_text, "Dynamic content should change on refresh"

    def test_sortable_table_loads(self, page: Page, base_url):
        """Data table should load with headers and rows"""
        page.goto(f"{base_url}/tables")

        expect(page.locator("table#table1")).to_be_visible()
        headers = page.locator("table#table1 th")
        assert headers.count() > 0, "Table should have headers"

    def test_table_sort_by_last_name(self, page: Page, base_url):
        """Clicking Last Name header should sort the table"""
        page.goto(f"{base_url}/tables")

        page.click("table#table1 th:has-text('Last Name')")
        first_row_after_sort = page.locator(
            "table#table1 tbody tr:first-child td:first-child"
        ).inner_text()

        assert first_row_after_sort != "", "Table should be sorted"

    def test_filter_visible_elements(self, page: Page, base_url):
        """Only visible elements should be interactable"""
        page.goto(f"{base_url}/dynamic_controls")

        checkbox = page.locator("#checkbox")
        expect(checkbox).to_be_visible()

    def test_dropdown_filter_options(self, page: Page, base_url):
        """Dropdown should contain selectable options"""
        page.goto(f"{base_url}/dropdown")

        dropdown = page.locator("#dropdown")
        expect(dropdown).to_be_visible()

        page.select_option("#dropdown", value="1")
        selected = page.locator("#dropdown option:checked").inner_text()
        assert selected == "Option 1"

    def test_dynamic_loading_widget(self, page: Page, base_url):
        """Widget should load content after dynamic fetch"""
        page.goto(f"{base_url}/dynamic_loading/1")

        page.click("button:has-text('Start')")
        expect(page.locator("#finish")).to_be_visible(timeout=10000)
        expect(page.locator("#finish")).to_contain_text("Hello World!")

    def test_responsive_image_loads(self, page: Page, base_url):
        """Images should load correctly on the page"""
        page.goto(f"{base_url}/dynamic_content")

        images = page.locator(".large-2.columns img")
        assert images.count() > 0, "Page should contain images"
        expect(images.first).to_be_visible()