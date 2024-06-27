import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video(url, save_path):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)
        
        # Filter streams to get only progressive mp4 formats
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        
        # Get the highest resolution stream
        highest_res_stream = streams.get_highest_resolution()
        
        # Download the video to the specified path
        highest_res_stream.download(output_path=save_path)
        
        # Print success message to console
        print("Video downloaded successfully!")
        
        # Show success message box in GUI
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        # Print any errors that occur to the console
        print(e)
        
        # Show error message box in GUI with the specific error message
        messagebox.showerror("Error", f"An error occurred: {e}")

def open_file_dialog():
    # Open a file dialog to select a directory for saving the video
    folder = filedialog.askdirectory()
    
    # If a folder is selected, print its path to console
    if folder:
        print(f"Selected folder: {folder}")
        
    # Return the selected folder path
    return folder

def main():
    # Create a Tkinter root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Prompt the user to enter a YouTube URL
    video_url = input("Please enter a YouTube URL: ")

    # Open a file dialog to select a folder for saving the video
    save_dir = open_file_dialog()

    # If a valid save directory is selected, proceed with download
    if save_dir:
        # Print download start message to console
        print("Started download...")
        
        # Call download_video function with the entered URL and save directory
        download_video(video_url, save_dir)
    else:
        # Print an error message if no valid save location is selected
        print("Invalid save location.")
        
        # Show warning message box in GUI about the invalid directory
        messagebox.showwarning("Directory Error", "Invalid save location.")

if __name__ == "__main__":
    main()

