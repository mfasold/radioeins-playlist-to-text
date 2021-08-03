# Radioeins Playlist To Text Downloader

Converts a Radioeins playlist to plain text, for example to create a Spotify playlist from this.

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

  
## Requirements / Installation

Simply clone the repo / download the the script and install Beautifulsoup4.

```bash
  pip install beautifulsoup4
```
    
## Usage / Example

```bash
  python3 get-playlist.py --url https://www.radioeins.de/musik/playlists.htm/from\=31-07-2021_00-00/to\=01-08-2021_00-00/sendung\=%21content%21rbb%21rad%21programm%21sendungen%21tanzhalle%21index.html
```

Results:
```
Stanley Black - Melodie D'amour
Eternals - R&R Cha Cha
Ronald Stein - Attack of the 50ft. Woman, Giant Footprint
Carol FRan - I'm Gonna Try
The Ventures - Hawaii Five-O
J.Ben & Toquinho - Carolina Carol Bella
Sugar Belly & The Canefields - Shake Up Adina
Shavora - Sweet Buns of Mine
Swingology - Radioactive Blood
MADNESS - One Step Beyon
...
```

## Creating a Spotify playlist from a Radioeins playlist

Go to [Spotlistr](https://www.spotlistr.com/search/textbox) and paste the Artist-Title list from above. HOWEVER, don't expect a great detection rate.
