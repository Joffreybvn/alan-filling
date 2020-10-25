
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

        config.data_api_baseurl

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
