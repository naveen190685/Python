from Programs.Selenium.core.Helper import Helper

I = Helper()
I.open_chrome()

I.goTo("https://www.amazon.in")
I.click("Sign in")
I.write("naveen190685@gmail.com")
I.click("Continue")
I.write("kuchBhiDalu")
I.submit()
print("RAN SUCCESSFULLY 'AMAZON")

# Lets.goTo("https://www.google.com")
# Lets.write("taiko")
# Lets.click("Google Search")
# # Lets.click("Taiko - Wikipedia")
# print("RAN SUCCESSFULLY 'GOOGLE")


I.closeBrowser()
