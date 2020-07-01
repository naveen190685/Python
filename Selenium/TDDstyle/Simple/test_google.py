from Programs.Selenium.core.Helper import Helper

I = Helper()
I.open_chrome()

I.goTo("https://www.google.com")
I.write("taiko")
I.click("Google Search")
I.click("Taiko - Wikipedia")
print("RAN SUCCESSFULLY 'GOOGLE")


I.closeBrowser()
