from Programs.Selenium.HelperClass import Helper

Lets = Helper()
Lets.open_chrome()

Lets.goTo("https://www.amazon.in")
Lets.click("Sign in")
Lets.write("naveen190685@gmail.com")
Lets.click("Continue")
Lets.write("kuchBhiDalu")
Lets.submit()
print("RAN SUCCESSFULLY 'AMAZON")


# Lets.goTo("https://www.google.com")
# Lets.write("taiko")
# Lets.click("Google Search")
# # Lets.click("Taiko - Wikipedia")
# print("RAN SUCCESSFULLY 'GOOGLE")


Lets.closeBrowser()