# tor_support.py

```python
import requests
import socks
import socket

def enable_tor():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

def disable_tor():
    socks.set_default_proxy()
    socket.socket = socks.socksocket

def check_tor_status():
    try:
        response = requests.get("https://check.torproject.org/")
        if "Congratulations. This browser is configured to use Tor." in response.text:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False
```

This code provides the necessary functions to enable and disable Tor support in the AI assistant. The `enable_tor()` function sets the default proxy to use Tor's SOCKS5 proxy on `localhost` port `9050`, while the `disable_tor()` function resets the default proxy to the system default. The `check_tor_status()` function sends a request to the Tor Project's check page and checks if the response indicates that Tor is successfully configured.