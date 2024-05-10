# validating email and adding it to a dictionary as the key, with an empty dictionary as the value
import re 


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9À-ÿ._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", text)
print(emails)

