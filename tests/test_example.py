
def test_abrir_google(page):
    page.goto("https://www.google.com")
    page.get_by_role("button", name="Google Search").click()
    assert "Google" in page.title()