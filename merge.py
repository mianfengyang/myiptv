import os
import requests

def download_file():
    fmm_url = "https://live.fanmingming.com/tv/m3u/ipv6.m3u"
    fmm_file = "FMM.m3u"
    """
    Downloads a file from the given URL and saves it to the specified file name.

    Args:
        url (str): The URL of the file to download.
        fmm_file (str): The name of the file to save the downloaded file to.

    Returns:
        None
    """
    # Send a GET request to the URL
    response = requests.get(fmm_url)

    # Check if the response is successful
    if response.status_code == 200:
        # Write the response content to the file
        with open(fmm_file, 'w') as f:
            f.write(response.content.decode("utf-8"))
    else:
        print(f"Failed to download file from {fmm_url}. Status code: {response.status_code}")

def write_fh():
    src_file = "FMM.m3u"
    dest_file = "fh.txt"
    results = []
    with open(src_file, 'r') as srcf:
        line = srcf.readline()
        while line:
            line = srcf.readline()
            if "第一财经" in line or "东方财经" in line or "求索" in line:
                channel_name = line.split(",")[1].replace("\n","")
                channel_url = next(srcf)
                results.append((channel_name, channel_url))

    with open(dest_file, 'w', encoding='utf-8') as destf:
        for line in results:
            channel_name, channel_url = line
            destf.write(f"{channel_name},{channel_url}")

