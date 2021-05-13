
# Cisco DNA Center Client Connectivity Info


This application will return the client connectivity info by MAC address.

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
 
This app is to be used only in demo or lab environments, it is not written for production


**Cisco Products & Services:**

- Cisco DNA Center
- Cisco Network Devices managed by Cisco DNA Center
- Clients

**Tools & Frameworks:**

- Python environment to run the application

**Usage**

Sample Output for connected client:

~~~

Client Info App Start,  2021-05-12 16:52:55
Enter the client MAC address in the colon hexadecimal notation xx:xx:xx:xx:xx:xx : 40:A6:B7:1D:81:14

Client Status: Connected
Last Updated: 2021-05-12 16:52:00
Client Connection: WIRED
Connected to device: PDX-M
Connected to switchport: TenGigabitEthernet1/1/4
Building/Floor: OR/PDX-1/Floor 2

Client Info App Run End,  2021-05-12 16:53:01

~~~

Sample Output for disconnected client:

~~~

Client Info App Start,  2021-05-12 15:59:03
Enter the client MAC address in the colon hexadecimal notation xx:xx:xx:xx:xx:xx : 54:8A:BA:EE:82:28

Client Status: Disconnected
Last Updated: 2021-05-12 14:18:00
Client Connection: WIRED
Connected to device: PDX-M
Connected to switchport: GigabitEthernet1/0/10
Building/Floor: OR/PDX-1/Floor 2

Client Info App Run End,  2021-05-12 15:59:08

~~~

Sample output for wireless client:

~~~

Client Info App Start,  2021-05-12 17:09:19
Enter the client MAC address in the colon hexadecimal notation xx:xx:xx:xx:xx:xx : F0:8A:76:25:18:72

Client Status: Connected
Last Updated: 2021-05-12 17:06:00
Client Connection: WIRELESS
Connected to device: C9120.B9B4
Building/Floor: San Jose/SJ04/Fl3

Client Info App Run End,  2021-05-12 17:09:25

~~~

This sample code is for proof of concepts and labs

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).


