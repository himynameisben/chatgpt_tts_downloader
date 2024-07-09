import os
from utils import download_file_from_curl

# Replace this curl command with your own
curl_command = """
curl 'https://chatgpt.com/backend-api/synthesize?message_id=msg_id&conversation_id=con_id&voice=cove&format=aac' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer my_token \
  -H 'cookie: my_cookie' \
  -H 'oai-device-id: 1dc9cc46-7add' \
  -H 'oai-language: en-US' \
  -H 'priority: u=1, i' \
  -H 'referer: https://chatgpt.com/c/chat_id' \
  -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
"""

output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
output_filename = f'{output_dir}/output.aac'

if download_file_from_curl(curl_command, output_filename):
    print(f"Downloaded file saved as {output_filename}.")
else:
    print("Failed to download file.")
