# Kawaii API

A REST API designed for anime enthusiasts to explore and interact with anime-related data.

## Overview

The Kawaii API allows users to access information about anime series, episodes, characters, and more. It is built to serve anime lovers who want to integrate anime data into their applications or simply fetch information for personal use.

## Features

- **Retrieve Anime Information:** Fetch details about specific anime series by ID.
- **Explore Episodes and Characters:** Get information about episodes and characters within a series.
- **Future Extensions:** The API is designed to be extensible, with potential for additional endpoints and features.


## Usage

Here's a simple example of how to use the Kawaii API to retrieve information about a specific anime series:

```python
import request

BASE_URL = "http://localhost:8000/api/v1/anime"
LocalSession = requests.Session()

def make_request(session: requests.Session,
                  method: Literal['GET', 'POST'],
                  url: str, **kwargs):
    response = session.request(method=method, url=url, **kwargs)
    print(f"{method} | {url} -> {response.status_code}")
    print("Response Back:")
    print(response.text)
    print("-------------------------------------")
    
def main():
    anime_id = 1
    make_request(session=session,
                    method="GET",
                    url=BASE_URL + f"/{anime_id}")
if __name__ == "__main__":
    main()
```