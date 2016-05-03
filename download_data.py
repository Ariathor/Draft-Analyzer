# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import urllib.request
import shutil
import os
import os.path

from formatted_date_generator import date_generator


def main():
    dates = date_generator()

    os.makedirs('AH-Data', exist_ok=True)

    for date in dates:
        url = 'http://dl.hex.gameforge.com/auctionhouse/' + date
        filePath = 'AH-Data/' + date
        if not os.path.isfile(filePath):
            try:
                # Download the file from `url` and save it locally under `file_name`:
                with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
            except (urllib.error.HTTPError, LookupError):
                pass

def replace_day(day):
    url = 'http://dl.hex.gameforge.com/auctionhouse/' + day
    filePath = 'AH-Data/' + day
    # os.remove(filePath) Unecessary and causes trouble
    try:
        # Download the file from `url` and save it locally under `file_name`:
        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except (urllib.error.HTTPError, LookupError):
        pass



if __name__== '__main__':
    main()