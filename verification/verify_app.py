
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Since we are using CDNs, we need to bypass CSP or allow them if needed, but file:// should be fine
        # We need to use absolute path
        cwd = os.getcwd()
        page.goto(f'file://{cwd}/index.html')

        # Click 'Get Started' on Welcome Modal if it appears
        # Note: LocalStorage might be empty in headless, so it should appear
        try:
            page.click('button.swal2-confirm', timeout=2000)
            print('Clicked Get Started')
        except:
            print('Welcome modal not found or already closed')

        # Check if #qr-container exists
        if page.query_selector('#qr-container'):
            print('QR container found')
        else:
            print('QR container NOT found')

        # Instead of canvas, wait for the container content to update or just screenshot the container
        # The library might render SVG or Canvas depending on options. We set 'svg'.
        # appState.qrOptions.type = 'svg'
        page.wait_for_selector('#qr-container svg', timeout=5000)

        # Take screenshot of the full app
        page.screenshot(path='verification/app_screenshot.png', full_page=True)

        # Switch to WiFi mode and take screenshot
        page.click('button[data-mode="wifi"]')
        page.wait_for_selector('#input-wifi', state='visible')
        page.screenshot(path='verification/wifi_mode.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    run()
