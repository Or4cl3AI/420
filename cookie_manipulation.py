# cookie_manipulation.py

```python
import requests

def manipulate_cookie(url, cookie):
    session = requests.Session()
    session.cookies.set('Cookie', cookie)
    response = session.get(url)
    return response.text
```

This code defines a function `manipulate_cookie` that takes in a `url` and a `cookie` as parameters. It uses the `requests` library to create a session and set the provided `cookie` in the session's cookies. It then sends a GET request to the `url` and returns the response text.

This function can be used to manipulate cookies by setting a specific cookie value and sending a request to a target URL.