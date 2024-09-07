# Spotify Song Downloader

This Python script allows you to download songs from Spotify using the `spotdl` library. It provides a simple interface to download individual tracks in various quality settings.

## Features

- Download individual Spotify tracks
- Specify output directory for downloaded songs
- Choose audio quality (e.g., 128k, 320k, or best)
- Error handling and logging

## Prerequisites

Before you can use this script, you need to have the following installed:

- Python 3.6 or higher
- `spotdl` library

You can install `spotdl` using pip:

```
pip install spotdl
```

## Usage

1. Clone this repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with Python:

```
python spotify_downloader.py
```

### Function: `download_spotify_song`

```python
def download_spotify_song(song_url, output_dir, quality='best'):
    # Function implementation...
```

Parameters:
- `song_url` (str): The Spotify URL of the song you want to download.
- `output_dir` (str): The directory where the downloaded song will be saved.
- `quality` (str, optional): The desired audio quality. Default is 'best'. Options include '128k', '320k', etc.

Returns:
- `bool`: True if the download was successful, False otherwise.

## Example

```python
song_url = "https://open.spotify.com/track/2USlegnFJLrVLpoVfPimKB?si=773ed89435d94b58"
output_directory = "downloads"

# Download in best quality
success = download_spotify_song(song_url, output_directory, quality='320k')

if success:
    print(f"Check the '{output_directory}' folder for your high-quality downloaded song.")
else:
    print("Failed to download the song.")
```

## Error Handling

The script includes error handling for various scenarios:
- If the `spotdl` command fails, it will capture and print the error message.
- If the output directory doesn't exist, it will be created automatically.
- Unexpected errors are caught and reported.

## Limitations

- This script relies on the `spotdl` library, which may have its own limitations or dependencies.
- Downloading copyrighted material without permission may be illegal in your jurisdiction. Use this script responsibly and only for content you have the right to download.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This script is for educational purposes only. Please respect copyright laws and Spotify's terms of service when using this script.
