import os
from utils import download_file_from_curl, convert_aac_to_mp3

# define directories
curl_commands_dir = "curl_commands"
downloaded_dir = "downloaded"
output_dir = "output"

# create directories if they don't exist
os.makedirs(curl_commands_dir, exist_ok=True)
os.makedirs(downloaded_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


# read all curl files
curl_files = [
    f
    for f in os.listdir(curl_commands_dir)
    if os.path.isfile(os.path.join(curl_commands_dir, f))
]

for curl_file in curl_files:
    with open(os.path.join(curl_commands_dir, curl_file), "r") as file:
        curl_command = file.read()

        base_filename = os.path.splitext(curl_file)[0]

        output_filename_aac = os.path.join(output_dir, f"{base_filename}.aac")
        output_filename_mp3 = os.path.join(output_dir, f"{base_filename}.mp3")

        # download file
        if download_file_from_curl(curl_command, output_filename_aac):
            convert_aac_to_mp3(output_filename_aac, output_filename_mp3)
            # move curl file to downloaded directory
            os.rename(
                os.path.join(curl_commands_dir, curl_file),
                os.path.join(downloaded_dir, curl_file),
            )
