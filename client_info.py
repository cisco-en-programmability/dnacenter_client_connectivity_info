#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""

__author__ = "Gabriel Zapodeanu TME, ENB"
__email__ = "gzapodea@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

import datetime
import logging
import os
import time
from datetime import datetime

import urllib3
from dnacentersdk import DNACenterAPI
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth  # for Basic Auth
from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings

load_dotenv('environment.env')

DNAC_URL = os.getenv('DNAC_URL')
DNAC_USER = os.getenv('DNAC_USER')
DNAC_PASS = os.getenv('DNAC_PASS')


os.environ['TZ'] = 'America/Los_Angeles'  # define the timezone for PST
time.tzset()  # adjust the timezone, more info https://help.pythonanywhere.com/pages/SettingTheTimezone/

urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings


def main():
    """
    This application will return the client connection info by MAC address.
    The user will be asked to enter a client MAC address in the colon hexadecimal format.
    It will collect the current, or last known, client connection info from Cisco DNA Center.
     - Client Status: connected or disconnected
     - Last Updated: local time zone timestamp
     - Client Connection: wired or wireless
     - Connected to device: device hostname
     - Connected to switchport: interface name if available
     - Building/Floor: location
    This script is using environment variables for the Cisco DNA Center URL, username and password.
    It has been developed using the Cisco DNA Center Python SDK
    """

    # logging, debug level, to file {application_run.log}
    logging.basicConfig(
        filename='application_run.log',
        level=logging.DEBUG,
        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('\nClient Info App Start, ', current_time)

    # Create a DNACenterAPI "Connection Object"
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.1.2', verify=False)

    # ask user to input the client MAC address

    client_mac = input('Enter the client MAC address in the colon hexadecimal notation xx:xx:xx:xx:xx:xx : ')

    # create a DNACenterAPI "Connection Object", to avoid token expiration after 60 minutes
    dnac_api = DNACenterAPI(username=DNAC_USER, password=DNAC_PASS, base_url=DNAC_URL, version='2.1.2',
                            verify=False)

    # receive the client detail info for the client with the MAC address at a specific timestamp
    client_info = dnac_api.clients.get_client_detail(mac_address=client_mac)

    # parse the client info:
    # Client Status: connected or disconnected
    # Last Updated: local time zone timestamp
    # Client Connection: wired or wireless
    # Connected to device: device hostname
    # Connected to switchport: interface name if available
    # Building/Floor: location

    try:
        connection_type = client_info['detail']['hostType']
        last_updated_epoch = client_info['detail']['lastUpdated']
        connection_info = client_info['detail']['healthScore']
        connection_status = 'Connected'
        for connection in connection_info:
            if connection['healthType'] == 'CONNECTED' and connection['score'] == 0:
                connection_status = 'Disconnected'
        device_name = client_info['detail']['clientConnection']
        location = client_info['detail']['location']
        port = client_info['detail']['port']
        last_updated = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(last_updated_epoch/1000)))
        client_connection_info = '\nClient Status: ' + connection_status
        client_connection_info += '\nLast Updated: ' + last_updated
        client_connection_info += '\nClient Connection: ' + connection_type
        client_connection_info += '\nConnected to device: ' + device_name
        if port:
            client_connection_info += '\nConnected to switchport: ' + port
        client_connection_info += '\nBuilding/Floor: ' + location
        print(client_connection_info)

    except:
        print('\nUnable to collect the client info, client not in the Cisco DNA Center inventory')

    current_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('\nClient Info App Run End, ', current_time)


if __name__ == '__main__':
    main()
