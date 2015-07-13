# Copyright 2015, Ioannis Mouratidis, All rights reserved.
__author__ = 'Ioannis'

import configparser
import os

verboseFlag = True


def default_values():
    config = configparser.ConfigParser()
    config['Syncing'] = {'forwardFlag': False, 'TCG_Browser_URL': ''}
    config['Options'] = {'colors': 'collectionMode', 'trimPrices': False}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_url():
    if not os.path.isfile('config.ini'):
        default_values()

    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        forwardFlag = config['Syncing'].getboolean('forwardFlag')
        TCG_Browser_URL = config['Syncing']['TCG_Browser_URL']
        if forwardFlag is None:
            raise KeyError
    except KeyError:
        default_values()
        read_url()

    return (forwardFlag, TCG_Browser_URL)

def set_url(url):
    if not os.path.isfile('config.ini'):
        default_values()

    config = configparser.ConfigParser()
    config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
    if not isinstance(url, str) or url == "":
        default_values()
    else:
        try:
            config['Syncing']['forwardFlag'] = 'True'
            config['Syncing']['TCG_Browser_URL'] = url
        except KeyError:
            config['Syncing'] = {'forwardFlag': True, 'TCG_Browser_URL': url}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

def set_color_mode(mode):
    if not os.path.isfile('config.ini'):
        default_values()

    config = configparser.ConfigParser()
    config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
    try:
        if mode not in ('collectionMode', 'thresholdMode'):
            raise KeyError
        config['Options']['colors'] = mode
    except KeyError:
            config['Options'] = {'colors': 'collectionMode'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_color_mode():
    if not os.path.isfile('config.ini'):
        default_values()

    config = configparser.ConfigParser()
    config.read('config.ini')                           # Doesn't throw an error even if config.ini doesn't exist
    try:
        colorMode = config['Options']['colors']
        if colorMode not in ('collectionMode', 'thresholdMode'):
            raise KeyError
    except KeyError:
        default_values()
        return read_color_mode()
    return colorMode

def read_price_mode():
    if not os.path.isfile('config.ini'):
        default_values()

    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        trimPrices = config['Options'].getboolean('trimPrices')
        if trimPrices not in (True, False):
            raise KeyError
    except KeyError:
        default_values()
        return read_price_mode()
    return trimPrices


if __name__ == '__main__':
    print(read_price_mode())



