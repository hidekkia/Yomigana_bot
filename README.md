# Description

Yomigana Retriever is a Python script designed to automate the retrieval of Japanese readings (yomigana) for song titles and artist names. By providing a list of songs and artists in an Excel file, the script uses Selenium to search for each entry on a specified website and collects the yomigana, which is then saved in another Excel file for easy reference. This tool is particularly useful for music enthusiasts, language learners, or anyone interested in Japanese music who needs to know the correct pronunciation of song titles and artist names.

# Usage:
1. Prepare the input Excel file named requested_song_list.xlsx. This file should contain at least two columns:
<peg>- Song Title: The title of the song.
<peg>- Artist: The name of the artist or band.
<peg>Ensure that the file is saved in a format that can be read by pandas, such as .xlsx.
2. Place the input file in the same directory as the yomigana_get.py script.
3. Run the script using Python (yomigana_get.py)
4. The script will process the input file, search for each song and artist on the specified website using Selenium, retrieve the yomigana, and save the results in yomigana.xlsx. The output file will include the original data along with an additional column for the yomigana.
