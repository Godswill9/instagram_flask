from pyinsta import Instagram

# Initialize an Instagram instance
instagram = Instagram()

# Replace 'instagram_post_url' with the URL of the Instagram video you want to download
post_url = "https://www.instagram.com/reel/CzQbn7wIoyV/"

# Specify the target directory where you want to save the downloaded video
target_directory = "downloaded_videos"

# Download the video
instagram.download_post(post_url, target=target_directory)

# The downloaded video will be saved in the 'downloaded_videos' folder in the current directory
