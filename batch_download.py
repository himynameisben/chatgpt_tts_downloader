import os
from utils import download_file_from_curl

# define directories
curl_commands_dir = 'curl_commands'
downloaded_dir = 'downloaded'
output_dir = 'output'

# create directories if they don't exist
os.makedirs(curl_commands_dir, exist_ok=True)
os.makedirs(downloaded_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)


# read all curl files
curl_files = [f for f in os.listdir(curl_commands_dir) if os.path.isfile(os.path.join(curl_commands_dir, f))]

for curl_file in curl_files:
    with open(os.path.join(curl_commands_dir, curl_file), 'r') as file:
        curl_command = file.read()
        
        output_filename = os.path.join(output_dir, f"{curl_file}.aac")

        # download file
        if download_file_from_curl(curl_command, output_filename):
            # move curl file to downloaded directory
            os.rename(os.path.join(curl_commands_dir, curl_file), os.path.join(downloaded_dir, curl_file))
