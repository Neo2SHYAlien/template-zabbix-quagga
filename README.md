### About:

This is a template to monitor peerings BGP Quagga with Zabbix.

### Requirements:

  Python + Zabbix

### What I used:

- FreeBSD 11
- Quagga 1.2.2
- Python 2.7.14
- Zabbix 3.4

### How it works:

Using this template, Zabbix Server can discovery the BGP peerings and monitor them. I'm using Zabbix Agent on FreeBSD with Quagga running BGP.

### Configuration:

- Copy the scripts bgpdiscovery.py and bgpmon.py to directory /usr/bin/.

- Set execute permission for both scripts:
  chmod +x /usr/bin/bgpdiscovery.py
  chmod +x /usr/bin/bgpmon.py

- On the end of zabbix_agentd.conf file put the lines below:

  # BGP Discovery
  UserParameter=bgpdiscovery,/usr/bin/bgpdiscovery.py

  # Session BGP monitore
  UserParameter=bgpmon[*],/usr/bin/bgpmon.py $1

- Grant permission to user Zabbix run vtysh commands:

  pw usermod zabbix -G quagga (in my case was FreeBSD)

- Import the template on Zabbix Server and configure on host.
