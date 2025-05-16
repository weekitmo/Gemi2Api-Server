from datetime import datetime
from time import strftime
import browser_cookie3

cj = browser_cookie3.edge(domain_name="google.com")

special_keys = ["__Secure-1PSID", "__Secure-1PSIDTS"]

matched_cookies = [cookie for cookie in cj if cookie.name in special_keys]
for cookie in matched_cookies:
    if cookie.domain == ".google.com":
        print(
            f"{cookie.name}: {cookie.value}, {cookie.domain}, {cookie.path}, {datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')}"
        )
