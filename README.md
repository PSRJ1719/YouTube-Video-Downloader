# YouTube Video Downloader

This Python script allows you to download YouTube videos in the highest resolution available using a simple graphical interface for selecting the download location. The script utilizes the `pytube` library to handle the YouTube video extraction and downloading process.

## Features

- **Simple Interface:** Uses the Tkinter library to provide a simple file dialog for selecting the download location.
- **Highest Resolution:** Automatically downloads the video in the highest available resolution in MP4 format.
- **Error Handling:** Displays error messages in both the console and a graphical message box if something goes wrong during the download.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python packages: `pytube`, `tkinter`

You can install the required packages using pip:


pip install pytube3


## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   git clone https://github.com/PSRJ1719/YouTube-Video-Downloader.git
   

2. **Navigate to the Script Directory:**

   Navigate to the directory where the script is located:

   cd YouTube-Video-Downloader
   
4. **Run the Script:**

   You can run the script using the following command:

   python youtube_downloader.py

5. **Download a Video:**

   - Enter the URL of the YouTube video you wish to download.
   - Select a folder where you want to save the downloaded video using the file dialog that appears.
   - The script will download the video in the highest available resolution and notify you once the download is complete.

## Example

Here's a brief example of how the script works:

- Run the script.
- Enter the YouTube video URL when prompted (e.g., `https://www.youtube.com/watch?v=example`).
- Select the folder where you want to save the video.
- The video will be downloaded to the selected folder.

## Error Handling

If the script encounters any issues during the download process, it will display an error message in both the console and a graphical message box, providing details about the problem.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
