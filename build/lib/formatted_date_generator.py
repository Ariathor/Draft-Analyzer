# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import datetime

def date_generator():
    dt = datetime.date(2014, 12, 23) # First day of non-compiled data
    end = datetime.date.today() - datetime.timedelta(days=1)
    step = datetime.timedelta(days=1)

    result = [] # Old, compiled data ='AH-Data-2014-10-10-to-2014-12-22.csv'

    # Adds the dates to a list in the correct formatting
    while dt <= end:
        result.append('AH-Data-' + dt.strftime('%Y-%m-%d')+ '.csv')
        dt += step

    return result

