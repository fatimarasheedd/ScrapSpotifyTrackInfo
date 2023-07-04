# Spotify Track Analysis

This project aims to fill missing values in a CSV file containing track information by utilizing the Spotify API. It retrieves track features, such as energy and valence, based on the track name and artist. Additionally, it downloads album covers for the tracks.

I created this project as an intermediate step for building a VR music visualiser (Work in progress). I am getting the album cover to display in the UI, and the valence and energy (in place of arousal value) to determine the colour the visualiser should be set to. 

## Prerequisites

To run this project, make sure you have the following:

- Required packages listed in the `requirements.txt` file

## Installation

1. Clone this repository to your local machine.
2. Install the required packages by running the following command: pip install -r requirements.txt
3. Create a `.env` file in the project directory and set the following environment variables:
CLIENT_ID=<your_spotify_client_id>
CLIENT_SECRET=<your_spotify_client_secret>
(do this by loging into a spotify web developer account and creating an application to get the keys - this tutorial was helpful https://www.youtube.com/watch?v=q5uM4VKywbA)


## Usage

1. Add the track information to the `trackanalysis.csv` file, leaving the ID, Valence, and Energy columns empty for the tracks you want to analyze.
2. Run the `read-csv.py` script to retrieve missing values and album covers. The script will update the `trackanalysis.csv` file with the retrieved information.


## File Descriptions

- `main.py`: Contains functions to interact with the Spotify API and retrieve track information.
- `read-csv.py`: Reads the `trackanalysis.csv` file, fills missing values, and downloads album covers.
- `trackanalysis.csv`: The CSV file containing track information. Ensure the column names are `Track`, `Artist`, `ID`, `Valence`, and `Energy`.

## Notes

- Make sure to set the environment variables `CLIENT_ID` and `CLIENT_SECRET` in the `.env` file before running the scripts.
- The `read-csv.py` script uses the `main.py` module to retrieve track information and album covers.
- If a track is not found on Spotify or doesn't have an associated ID, the script will print an error message and skip that track.




