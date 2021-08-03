#!/usr/bin/python
#
# Fetch playlist contents from radioeins website and export it to plain text
#
# Requirements:
#  - python 3.6 and up
#  - BeautifulSoup
#
import argparse
import pathlib
import requests
import pprint
from bs4 import BeautifulSoup
import re


class RadioeinsPlaylist:
    def get_radioeins_playlist(self, url, print_album=False):
        """
        Fetches the actual playlist from the given URL and prints it to stdout
        """
        # Step 1: Get the HTML page and extract link to actual playlist element
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        links = soup.findAll("a")
        pl_loader_link = next((a["href"] for a in links if "playList" in a["href"]), None)

        # To avoid making more requests, we modify the link slightly
        # from this: https://mein.radioeins.de/playList.do?action=searching&remote=1&version=2&from=24-07-2021_19-00&to=24-07-2021_21-00
        # to this:   https://playlist.funtip.de/playList.do?action=searching&remote=1&version=2&from=24-07-2021_19-00&to=24-07-2021_21-00&jsonp_callback=jQuery2240002052305759852935_1
        pl_loader_link = pl_loader_link.replace("mein.radioeins.de", "playlist.funtip.de")
        pl_loader_link += "&jsonp_callback=jQuery2240002"

        # Step 2: Get playlist fragment and extract information
        r = requests.get(pl_loader_link)

        matches = re.findall(r"\"(.+)\"", r.text)  # greedy extraction within quotes
        unescaped_html = (
            matches[0].replace("&mdash;", "|").encode("latin-1", "backslashreplace").decode("unicode-escape")
        )
        soup = BeautifulSoup(unescaped_html, "html.parser")

        tracks = soup.findAll("td", class_="trackInterpret")

        for t in tracks:
            line1 = t.div.contents[0].string
            line2 = t.div.span

            artist = line1.split("|")[0].strip()
            title = line1.split("|")[1].strip()
            album = ""
            if line2 is not None:
                album = line2.contents[0].strip()
            if print_album:
                print(" - ".join([artist, title, album]))
            else:
                print(" - ".join([artist, title]))

    def cli(self, cmd_args=None):
        """
        The commandline interface
        """
        parser = argparse.ArgumentParser(description="Get Radio1 playlist for given URL")
        parser.add_argument("--url", dest="url", help="The URL of the playlist")
        parser.add_argument("--print-album", dest="print_album", action="store_true")
        args = parser.parse_args(cmd_args)
        self.get_radioeins_playlist(args.url, args.print_album)


rep = RadioeinsPlaylist()
if __name__ == "__main__":
    rep.cli()
