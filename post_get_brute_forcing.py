# post_get_brute_forcing.py

```python
import requests

def brute_force_post(url, data, dictionaries):
    for dictionary in dictionaries:
        for key in dictionary:
            data[key] = dictionary[key]
            response = requests.post(url, data=data)
            # Process the response

def brute_force_get(url, params, dictionaries):
    for dictionary in dictionaries:
        for key in dictionary:
            params[key] = dictionary[key]
            response = requests.get(url, params=params)
            # Process the response
```

This code defines two functions `brute_force_post` and `brute_force_get` that perform brute force attacks on POST and GET requests respectively. The `brute_force_post` function takes a URL, data dictionary, and a list of dictionaries as parameters. It iterates over each dictionary in the list and for each key-value pair in the dictionary, it updates the corresponding key in the data dictionary and sends a POST request to the specified URL. The `brute_force_get` function is similar but it sends GET requests instead. Both functions use the `requests` library to make the HTTP requests. You can add code to process the responses according to your specific requirements.