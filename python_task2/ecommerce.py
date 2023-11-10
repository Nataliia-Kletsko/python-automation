from playwright.sync_api import sync_playwright

def test_ecommerce(browser, i):
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demowebshop.tricentis.com")

    email_prefix = 'nataliia.kletsko2'
    email_suffix = '@test.com'
    email = email_prefix + str(i) + email_suffix
    password = 'RandomPassword@'

    # Verify user register
    page.click('a[href="/register"]')
    page.wait_for_selector('form[action="/register"]')
    page.locator('input[value="F"]').set_checked(True)
    page.fill('input[name="FirstName"]', 'User First Name')
    page.fill('input[name="LastName"]', 'User Last Name')
    page.fill('input[name="Email"]', email)
    page.fill('input[name="Password"]', password)
    page.fill('input[name="ConfirmPassword"]', password)
    page.click('input[value="Register"]')
    page.wait_for_selector('.account')
    assert page.inner_text('.account') == email

    # Click the logout button
    page.click('a[href="/logout"]')
    page.wait_for_selector('.ico-login')

    # Verify user login
    page.click('a[href="/login"]')
    page.wait_for_selector('form[action="/login"]')
    page.fill('input[name="Email"]', email)
    page.fill('input[name="Password"]', password)
    page.click('input[value="Log in"]')
    page.wait_for_selector('.account')
    assert page.inner_text('.account') == email

    #Click to the computers link
    page.click('a[href="/computers"]')
    page.wait_for_selector('.sub-category-grid')

    # Verify that the computers category has 3 sub-categories
    assert page.locator('.item-box').count() == 3

    # Verify that the page has items
    assert page.get_by_text(['Desktops', 'Notebooks', 'Accessories'])

    page.click('a[title="Show products in category Desktops"]')

    # Check different sorting options
    page.select_option('select#products-orderby', 'Name: A to Z')
    page.select_option('select#products-orderby', 'Name: Z to A')

    # Check different number of items
    page.select_option('select#products-pagesize', '4')
    page.select_option('select#products-pagesize', '12')

    # Verify add item to the cart
    page.click('a[href="/build-your-own-expensive-computer-2"]')
    page.click('input[data-productid="74"]')
    page.wait_for_selector('.bar-notification')

    # Verify add item the to wishlist
    page.click('a[href="/gift-cards"]')
    page.click('a[href="/5-virtual-gift-card"]')
    page.fill('input[name="giftcard_1.RecipientName"]', 'Test receiver name')
    page.fill('input[name="giftcard_1.RecipientEmail"]', 'acasecdfawedacc@mail.com')
    page.fill('input[name="giftcard_1.SenderName"]', 'Test sender name')
    page.fill('input[name="giftcard_1.SenderEmail"]', 'acacsvsdrfv@mail.com')
    page.fill('textarea[name="giftcard_1.Message"]', 'Test message')
    page.click('input[value="Add to wishlist"]')
    page.wait_for_selector('.bar-notification')

    #Verify remove item from the cart
    page.click('a[href="/cart"]')
    page.wait_for_selector('.shopping-cart-page')
    page.set_checked('input[name="removefromcart"]', True)
    page.click('input[name="updatecart"]')
    assert page.inner_text('.order-summary-content') == 'Your Shopping Cart is empty!'

    # Verify proceed checkout
    page.click('a[href="/computers"]')
    page.wait_for_selector('.sub-category-grid')
    page.click('a[title="Show products in category Desktops"]')
    page.click('a[href="/build-your-own-expensive-computer-2"]')
    page.click('input[data-productid="74"]')
    page.wait_for_selector('.bar-notification')
    page.click('a[href="/cart"]')
    page.set_checked('input[name="termsofservice"]', True)
    page.click('button[name="checkout"]')
    page.wait_for_selector('.checkout-page')

    context.close()

with sync_playwright() as p:
    # Run the test on both Chrome and Firefox
    i = 1
    for browser_type in [p.chromium, p.firefox]:
        browser = browser_type.launch(headless=False)
        test_ecommerce(browser, i)
        i += 1
        # Increase iterator to avoid user has already exist warning message.
        browser.close()