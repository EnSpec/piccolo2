#!/usr/bin/env python

# Copyright 2014-2016 The Piccolo Team
#
# This file is part of piccolo2-player.
#
# piccolo2-player is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# piccolo2-player is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with piccolo2-player.  If not, see <http://www.gnu.org/licenses/>.

import player
import argparse
import logging

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u','--piccolo-url',metavar='URL',help='set the URL of the piccolo server')
    group.add_argument('-x','--xbee-address',metavar='ADR',help="the address of the xbee radio")
    group.add_argument('-n','--xbee-network',metavar='BAUD',help="the baudrate of the xbee network")
    parser.add_argument('-d','--debug', action='store_true',default=False,help="enable debugging output")

    args = parser.parse_args()

    log = logging.getLogger("piccolo")
    if args.debug:
        log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(name)s: %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    
    if args.xbee_address != None:
        connection = ('xbee',args.xbee_address)
    elif args.xbee_network != None:
        connection = ('xbee auto',args.xbee_network)
    elif args.piccolo_url != None:
        connection = ('http',args.piccolo_url)
    else:
        connection = None

    player.main(connection)

if __name__ == '__main__':
    main()
