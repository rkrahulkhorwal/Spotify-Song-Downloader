import subprocess
import os

def download_spotify_song(song_url, output_dir, quality='best'):
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Construct the spotdl command with quality option
        command = [
            "spotdl",
            "--output", output_dir,
            "--bitrate", quality,
            "--format", "mp3",
            song_url
        ]

        # Run the spotdl command
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Check if the download was successful
        if "Downloaded" in result.stdout:
            print("Song downloaded successfully.")
            return True
        else:
            print("Download might have failed. Check the output directory.")
            return False

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while downloading: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Example usage
song_url = "https://open.spotify.com/track/2USlegnFJLrVLpoVfPimKB?si=773ed89435d94b58"
output_directory = "downloads"

# Download in best quality
success = download_spotify_song(song_url, output_directory, quality='320k')

if success:
    print(f"Check the '{output_directory}' folder for your high-quality downloaded song.")
else:
    print("Failed to download the song.")
