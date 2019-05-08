import sys
import threading
import asyncio
import re
import time
import bisect

from ..broker import Broker


def _do_broker(args):
    broker = Broker(args.host, args.port)
    asyncio.run(broker.run())


def add_subparser(subparsers):
    subparser = subparsers.add_parser('broker',
                                      description='A simple broker.')
    subparser.add_argument('--host',
                           default='',
                           help="Broker host (default: '').")
    subparser.add_argument('--port',
                           type=int,
                           default=1883,
                           help='Broker port (default: 1883).')
    subparser.set_defaults(func=_do_broker)