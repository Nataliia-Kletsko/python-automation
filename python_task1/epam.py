from playwright.sync_api import sync_playwright

def test_epam(browser):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://epam.com")
    # Verify that title is correct
    assert page.title() == 'EPAM | Software Engineering & Product Development Services'

    # Verify site mode switcher
    page.locator('section.theme-switcher-ui').nth(1).click()
    page.wait_for_selector('body.light-mode')

    # Verify language switching
    page.click('button.location-selector__button')
    page.locator('text=Україна').nth(1).click()
    page.wait_for_timeout(1000)
    assert page.inner_text('button.location-selector__button') == 'Україна (UA)'

    # Verify policies list
    page.goto("https://epam.com")
    page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
    policies = ['INVESTORS', 'OPEN SOURCE', 'PRIVACY POLICY', 'COOKIE POLICY', 'APPLICANT PRIVACY NOTICE', 'WEB ACCESSIBILITY']
    assert page.get_by_text(policies)

    # Verify region location list
    regions = ['AMERICAS', 'EMEA', 'APAC']
    assert page.get_by_text(regions)
    page.click('a[data-item="2"]')

    # Verify search function
    page.click('button.header-search__button')
    page.fill('input[name="q"]', 'ai')
    page.click('button.custom-search-button')

    # Verify logo company navigation
    page.goto("https://www.epam.com/about")
    page.click('a.header__logo-container')
    page.wait_for_timeout(1000)

    context.close()

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox]:
        browser = browser_type.launch(headless=False)
        test_epam(browser)
        browser.close()