import re
import requests
from pydub import AudioSegment


def download_file_from_curl(curl_command, output_filename):
    # parse the URL from the curl command
    url = re.search(r"curl '([^']+)'", curl_command).group(1)

    # parse headers
    headers = dict(re.findall(r"-H '([^:]+): ([^']+)'", curl_command))

    # send a GET request
    print(f"downloading to {output_filename}")
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        with open(output_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Download completed successfully. Saved as {output_filename}.")
        return True
    else:
        print(
            f"Failed to download file. Status code: {response.status_code}, Error: {response.text}"
        )
        return False


def convert_aac_to_mp3(input_filename, output_filename):
    # Load the .aac file
    audio = AudioSegment.from_file(input_filename, format="aac")
    # Export as .mp3
    audio.export(output_filename, format="mp3")
    print(f"Conversion completed successfully. Saved as {output_filename}.")
