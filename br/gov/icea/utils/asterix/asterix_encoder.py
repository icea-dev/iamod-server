#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016, ICEA
#
# This file is part of atn-sim
#
# atn-sim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# atn-sim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""@package adsb_asterix_encode
"""

import binascii
import socket
import threading
import time

from br.gov.icea.utils.asterix import asterix_utils
from br.gov.icea.utils.forwarders.ground_station import GroundStation

__author__ = "Ivan Matias"
__date__ = "2016/04"


class AdsBAsterixEncode(object):
    """This class encodes ADS-B data in ASTERIX.

    This class is responsible for encode ADS-B data in ASTERIX CAT 21.

    """

    # BUFFER_SIZE [int]: Maximum size of the data buffer.
    BUFFER_SIZE = 1024

    def __init__(self, sic):
        """The constructor.

            Args:
                sic (int): The system code identification of surveillance sensor.

        """
        ## ground_station [object]: The CNS/ATM Ground Station
        self.ground_station = GroundStation(sic)

        ## port [int]: Data receiving port.
        self.port = 0

        ## net [string]: IPv4 address.
        self.net = '127.0.0.1'

        ## time_service_message [number]: Time in seconds for sending service message
        self.time_service_message = 6

    def create_socket(self, port):
        """Creates the socket for receiving the ADS-B messages.

        Args:
            port (int): Data receiving port.

        """
        # sock (socket):  The end point to send ASTERIX CAT 21.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.port = port

    def set_net(self, net):
        """Sets Ipv4 address.

        Args:
            net (string): IPv4 address

        """
        self.net = net

    def set_queue(self, queue):
        """Sets the queue for exchanging data between threads.

        Args:
            queue: The queue object.

        """
        # queue (Queue.Queue): The queue to exchange data.
        self.queue = queue

    def send_message(self, asterix_record):
        """Sends message to the net

        Args:
            asterix_record (dictionary): A ASTERIX record in a dicitionary

        """
        # Encoding data to ASTERIX format
        data_bin = asterix_utils.encode(asterix_record)
        # print ("%x" % data_bin)
        msg = hex(data_bin).rstrip("L").lstrip("0x")
        self.sock.sendto(binascii.unhexlify(msg), (self.net, self.port))
        print msg

    def service_message(self):
        """
        Sends the service status message of the CNS/ATM Ground Station.

        """

        while True:
            # Gets the message delivery time
            time_utc = time.gmtime(time.time()+1)
            # Converts for second:
            time_of_day = int(time_utc.tm_hour) * 3600 + int(time_utc.tm_min) * 60 + int(time_utc.tm_sec)

            # Gets the ASTERIX record for Ground Station
            asterix_record = self.ground_station.to_asterix_record(GroundStation.SERVICE_STATUS_MESSAGE, time_of_day)

            if asterix_record is not None:
                self.send_message(asterix_record)

            time.sleep(self.time_service_message)

    def encode_data(self):
        """Receiving and encoding the ADS-B data in ASTERIX CAT 21.

        """
        while True:
            if not self.queue.empty():
                aircraft_table = self.queue.get()
                items = aircraft_table.iteritems()
                for k, v in items:
                    asterix_record = aircraft_table[k].to_asterix_record(k)
                    #print asterix_record
                    if asterix_record is not None:
                        self.send_message(asterix_record)

    def start_thread(self, time_service_message=2):
        """Starts processing.

        """
        encode_thread = threading.Thread(target=self.encode_data, args=())
        encode_thread.start()

        self.time_service_message = time_service_message

        service_message_thread = threading.Thread(target=self.service_message, args=())
        service_message_thread.start()

