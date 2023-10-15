# proxy_support.py

```python
import requests

class ProxySupport:
    def __init__(self, proxies):
        self.proxies = proxies

    def send_request(self, url):
        try:
            response = requests.get(url, proxies=self.proxies)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
```

This code defines a `ProxySupport` class that takes a `proxies` parameter in its constructor. The `proxies` parameter should be a dictionary containing the proxy settings. The `send_request` method sends a GET request to the specified `url` using the provided proxies. If the request is successful, it returns the response text. If an error occurs, it prints the error message and returns `None`.