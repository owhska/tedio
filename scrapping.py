# from playwright.sync_api import sync_playwright
# 
# with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
# 
    # page = browser.new_page()
# 
    # page.goto("https://quotes.toscrape.com")
# 
# 
    # quotes = page.locator(".text").all()
# 
    # for quote in quotes:
        # print(quote.inner_text())
# 
# 
    # browser.close()

# from playwright.sync_api import sync_playwright
# 
# with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False)
# 
    # page = browser.new_page()
# 
    # page.goto("https://quotes.toscrape.com")
# 
# 
    # links = page.locator("a").all()
# 
    # for link in links:
        # print(link.get_attribute("href"))
# 
# 
    # browser.close()
# 
# from playwright.sync_api import sync_playwright
# 
# with sync_playwright() as p:
    # browser = p.chromium.launch()
# 
    # page = browser.new_page()
# 
    # page.goto("https://books.toscrape.com")
# 
    # books = page.locator(".product_pod").all()
# 
    # for book in books:
        # title = book.locator("h3 a").get_attribute("title")
        # price = book.locator(".price_color").inner_text()
# 
        # print(title, price)
# 
    # browser.close()


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://docs.python.org/3/")
    
    # page.wait_for_selector("a") abre o navegador e espera interacao com "a"

    links = page.locator("a").all()

    dados = []

    for link in links:
        texto = link.inner_text().strip()

        href = link.get_attribute("href")

        if texto and href:
            dados.append({"texto": texto, "link": href})
    
    for item in dados:
        print(item)

    browser.close()


