# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

from configobj import ConfigObj
from validate import Validator
import io
import os

default_ini = """[Default]

# collectionMode highlights cards red/green depending on whether you have 4 or more in your collection
# thresholdMode highlights cards depending on their shard colours
colours = collectionMode

# If trimprices is set to True non-legendary cards that sell at their respective price floor (4-5 plat for commons, 11-12 plat for uncommons and 30-32 plat for rares)
# will be ignored when calculating the total draft value
trimPrices = False

# Set your tcg_browser_url if you want Draft Analyzer to forward your data to hex tcg browser
# This is a legacy option from back when the API was horribly inefficient and would freeze the client for multiple seconds when connecting to a distant server
# If you prefer you can let Hex handle the syncing by adding an extra line (as per hex tcg browser instructions) to the api.ini
tcg_browser_url =

# Stores all Hex API output in a file with today's date in the API_logs folder
# WARNING: These files can take up quite a lot of space in the long run
API_logging = False

# This is a developer option - if you are running the python source from the command prompt (or an IDE), you can change this to True to show
# more information and some error messages for debugging
verboseFlag = False

# Stores the date of the last time cwik's API was polled for data to avoid spamming it with new requests
cardInfoCheck =
"""

valid_values = """[Default]
colours = option('collectionMode', 'thresholdMode', default = 'collectionMode')
trimPrices = boolean(default=False)
tcg_browser_url = string
API_logging = boolean(default=False)
verboseFlag = boolean(default=False)
cardInfoCheck = string
"""


# def default_values():
#     config = configparser.ConfigParser()
#     config['Syncing'] = {'forwardFlag': False, 'TCG_Browser_URL': ''}
#     config['Options'] = {'colors': 'collectionMode', 'trimPrices': False}
#     with open('config.ini', 'w') as configfile:
#         config.write(configfile)


verboseFlag = False

def default_values():
    with open('config.ini', 'w') as fp:
        print(default_ini, file=fp)


def getter(variable):
    if not os.path.isfile('config.ini'):
        default_values()

    text_buffer = io.StringIO(valid_values)
    config = ConfigObj('config.ini', configspec=text_buffer)
    text_buffer.close()

    validator = Validator()
    if not config.validate(validator):  # validates and returns True if file is ok, set copy= True if I want to add the default values to the ini
        default_values()
        getter(variable)

    return config['Default'][variable]


def setter(variable, value):
    if not os.path.isfile('config.ini'):
        default_values()

    text_buffer = io.StringIO(valid_values)                 # Creates a text stream, since configspec expects a file
    config = ConfigObj('config.ini', configspec=text_buffer)
    text_buffer.close()

    validator = Validator()
    if not config.validate(validator):  # validates and returns True if file is ok, set copy= True if I want to add the default values to the ini
        default_values()
        setter(variable, value)
    else:
        config['Default'][variable] = value
        config.write()



# def read_url():
#     if not os.path.isfile('config.ini'):
#         default_values()
#
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')
#     except configparser.ParsingError:
#         default_values()
#     try:
#         forwardFlag = config['Syncing'].getboolean('forwardFlag')
#         TCG_Browser_URL = config['Syncing']['TCG_Browser_URL']
#         if forwardFlag is None:
#             raise KeyError
#     except KeyError:
#         default_values()
#         read_url()
#
#     return (forwardFlag, TCG_Browser_URL)
#
#
# def set_url(url):
#     if not os.path.isfile('config.ini'):
#         default_values()
#
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
#     except configparser.ParsingError:
#         default_values()
#     if not isinstance(url, str) or url == "":
#         default_values()
#     else:
#         try:
#             config['Syncing']['forwardFlag'] = 'True'
#             config['Syncing']['TCG_Browser_URL'] = url
#         except KeyError:
#             config['Syncing'] = {'forwardFlag': True, 'TCG_Browser_URL': url}
#         with open('config.ini', 'w') as configfile:
#             config.write(configfile)
#
# def set_color_mode(mode):
#     if not os.path.isfile('config.ini'):
#         default_values()
#
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
#     except configparser.ParsingError:
#         default_values()
#     try:
#         if mode not in ('collectionMode', 'thresholdMode'):
#             raise KeyError
#         config['Options']['colors'] = mode
#     except KeyError:
#             config['Options'] = {'colors': 'collectionMode'}
#     with open('config.ini', 'w') as configfile:
#         config.write(configfile)
#
# def read_color_mode():
#     if not os.path.isfile('config.ini'):
#         default_values()
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
#     except configparser.ParsingError:
#         default_values()
#     try:
#         colorMode = config['Options']['colors']
#         if colorMode not in ('collectionMode', 'thresholdMode'):
#             raise KeyError
#     except KeyError:
#         default_values()
#         return read_color_mode()
#     return colorMode
#
# def read_price_mode():
#     if not os.path.isfile('config.ini'):
#         default_values()
#
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')
#     except configparser.ParsingError:
#         default_values()
#     try:
#         trimPrices = config['Options'].getboolean('trimPrices')
#         if trimPrices not in (True, False):
#             raise KeyError
#     except KeyError:
#         default_values()
#         return read_price_mode()
#     return trimPrices


if __name__ == '__main__':
    print(getter("colours"))
    # text_buffer = io.StringIO(valid_values)                 # Creates a text stream, since configspec expects a file
    # config = ConfigObj('config.ini', configspec=text_buffer)
    # text_buffer.close()
    #
    # validator = Validator()
    # if not config.validate(validator, copy=True):  # validates and returns True if file is ok
    #     default_values1()


