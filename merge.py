import os
import requests

def download_file(url, file_name):
    """
    Downloads a file from the given URL and saves it to the specified file name.

    Args:
        url (str): The URL of the file to download.
        file_name (str): The name of the file to save the downloaded file to.

    Returns:
        None
    """
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        # Write the response content to the file
        with open(file_name, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download file from {url}. Status code: {response.status_code}")
