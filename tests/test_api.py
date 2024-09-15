import time
import logging
import requests
from typing import Literal
from functools import wraps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test")

def performance_monitor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error during API call: {e}")
            raise
        finally:
            end_time = time.time()
            duration = end_time - start_time
            logger.info(f"Took {duration:.4f} seconds")
        return response
    return wrapper

BASE_URL = "http://localhost:8000/api/v1/anime"
LocalSession = requests.Session()

@performance_monitor
def make_request(session: requests.Session,
                  method: Literal['GET', 'POST'],
                  url: str, **kwargs):
    response = session.request(method=method, url=url, **kwargs)
    logger.info(f"{method} | {url} -> {response.status_code}")
    # logger.info("Response Back:")
    # logger.info(response.text)
    logger.info("-------------------------------------")
    
def main():
    session = LocalSession
    for i in range(1, 50):
        make_request(session=session,
                     method="GET",
                     url=BASE_URL + f"/{i}")
    
if __name__ == "__main__":
    main()
