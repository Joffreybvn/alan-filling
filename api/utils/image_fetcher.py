
import random
from requests import get
from config import config


class RandomImageFetcher:

    def __init__(self):
        """
        Fetch a random image of Alan Turing from the data API,
        and save the file returned by this URL.
        """
        self.url = self.__generate_random_image_url()

    @staticmethod
    def __generate_random_image_url() -> str:
        """
        Generate a random image URL.
        :return: The generated URL
        """

        # Generate an image id between 1 and 5 (both included)
        image_id = random.randint(1, 5)

        # Return the URL
        return f"{config.data_api_baseurl}/images/{image_id}.jpg"

    def download(self) -> bytes:
        """
        Download and return the file linked to this class self.url.
        """

        # Fetch the given URL
        response = get(self.url)

        # Stop the execution if the file was not found.
        if response.status_code != 200:
            raise FetchError

        # Return the file
        return response.content


class FetchError(Exception):
    """Base class for exceptions in this module."""
    pass
