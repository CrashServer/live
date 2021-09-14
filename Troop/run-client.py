#!/usr/bin/env python3
"""
    Troop-Client
    ------------
    Real-time collaborative Live Coding.

    - Troop is a real-time collaborative tool that enables group live
      coding within the same document. To run the client application it
      must be able to connect to a running Troop Server instance on
      your network. Running `python run-client.py` will start the process
      of connecting to the server by asking for a host and port (defaults
      are localhost and port 57890).

    - Using other Live Coding Languages:

        Troop is designed to be used with FoxDot (http://foxdot.org) but
        is also configured to work with Tidal Cycles (http://tidalcycles.org).
        You can run this file with the `--mode` flag followed by "tidalcycles"
        to use the Tidal Cycles language. You can also use any other application
        that can accept code commands as strings via the stdin by specifying
        the path of the interpreter application, such as ghci in the case of
        Tidal Cycles, in place of the "tidalcycles" string when using the
        `--mode` flag.
"""

# import argparse
# from src.config import langnames

# parser = argparse.ArgumentParser(
#     prog="Troop Client",
#     description="Collaborative interface for Live Coding")

# parser.add_argument('-i', '--cli', action='store_true', help="Use the command line to enter connection info")
# parser.add_argument('-p', '--public', action='store_true', help="Connect to public Troop server")
# parser.add_argument('-H', '--host', action='store', help="IP Address of the machine running the Troop server")
# parser.add_argument('-P', '--port', action='store', help="Port for Troop server (default 57890)")
# parser.add_argument('-n', '--name', action='store', help="Display name to use")
# parser.add_argument('-m', '--mode', action='store', default='foxdot',
#                     help='Name of live coding language ({}) or a valid executable'.format(', '.join(langnames.keys())))
# parser.add_argument('-s', '--syntax', action='store',
#                     help='Name of live coding language syntax to use when selecting "No Interpreter" option.')
# parser.add_argument('-a', '--args', action='store', help="Add extra arguments to supply to the interpreter", nargs=argparse.REMAINDER, type=str)
# parser.add_argument('-c', '--config', action='store_true', help="Load connection info from 'client.cfg'")
# parser.add_argument('--hub', help="Connect to a named Troop server running on the Troop Hub Service")

# args = parser.parse_args()

# Set up client

from src.client import Client
#from src.config import readin
#from getpass import getpass
from src.crashconfig import *

# # Language and syntax

#options = { 'lang': args.mode }
options = {}

# if args.syntax:

#     options['syntax'] = args.syntax

# # Server address

# if args.hub:

#     from src.hub import HubClient, HubParser

#     print("Troop Hub Service | Collecting details for '{}'".format(args.hub))

#     hub = HubParser(args.hub)
#     address = HubClient(**hub).query(hub.get('name'))

#     print("Troop Hub Service | Success.")

#     options['host'], options['port'] = address

# elif args.public:

#     from src.config import PUBLIC_SERVER_ADDRESS
#     options['host'], options['port'] = PUBLIC_SERVER_ADDRESS

# else:

#     if args.host:

#         options['host'] = args.host

#     if args.port:

#         options['port'] = args.port

# # User name

# if args.name:

#     options['name'] = args.name

# # Non-gui startup

# if args.cli:

#     if 'host' not in options:

#         options['host'] = readin("Troop Server Address", default="localhost")

#     if 'port' not in options:

#         options['port'] = readin("Port Number", default="57890")

#     if 'name' not in options:

#         options['name'] = readin("Enter a name")

#     options['password'] = getpass()
#     options['get_info'] = False # Flag to say we don't need the GUI

# elif args.config:

#     import os.path

#     if os.path.isfile('client.cfg'):

#         """
#         You can set a configuration file if you are connecting to the same
#         server on repeated occasions. A password should not be stored. The
#         file (client.cfg) should look like:

#         host=<host_ip>
#         port=<port_no>

#         """

#         options.update(Client.read_configuration_file('client.cfg'))

#     else:

#         print("Unable to load configuration from 'client.cfg'")

# # Store any extra arguments to supply to the interpreter

# if args.args:

#     options['args'] = args.args

options['host'] = crashHost
options['port'] = crashPort
options['name'] = crashName
options['password'] = crashPassword
options['get_info'] = False

myClient = Client(**options)
