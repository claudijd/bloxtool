#!/usr/bin/env python
"""bloxtool

Usage:
  bloxtool globalsearch <search_string> [--objtype=""][--exact][--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress search mac <mac_address> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress search address <ipv4addr> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress create <name> <ipv4addr> <mac_address> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress delete mac <mac_address> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress delete address <ipv4addr> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool fixedaddress option <option> value <value> address <ipv4addr>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool network list [-6][--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--extattrs]
  bloxtool network fixedaddresses <network> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool network get <network> [-6][--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool network delete <network> [-6][--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool network search name <name> [-6][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool network search site <site> [-6][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool network search attribute <attribute> value <value>[-6][--network=""][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool network create name <name> network <network> [--members=[]][--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool network create range name <name> start <start> end <end>[--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool network option create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool network attr create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool networkcontainer create name <name> network <network> [--members=[]][--comment=" "][--disable=True][--config=~/.bloxtool.cfg]
  bloxtool networkcontainer delete <network> [--config=~/.bloxtool.cfg][--delimeter=" "][--format=text]
  bloxtool networkcontainer option create <option> value <value> network_block <network_block>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool host search mac <mac_address>[--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool host search network <network>[--type=''][--status=''][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool host search attribute <attribute> value <value> network <network>[--type=''][--status=''][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool host create mac <mac_address> ipv4addrs <ipv4addrs> name <name>[--network-block=""][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool host get name <name>[--network-block=""][--delimeter=" "][--format=text][--config=~/.bloxtool.cfg][--extattrs]
  bloxtool host list [--delimeter=" "][--format=text][--config=~/.bloxtool.cfg]
  bloxtool host attr set <option> value <value> hostname <hostname>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool host attr delete <option> hostname <hostname>[--config=~/.bloxtool.cfg][--delimeter=" "][--format=text][--delete]
  bloxtool member list [--config=~/.bloxtool.cfg]

Options:
  -h --help     Show this screen.
  members is a comma separated list of members
  ipv4addrs can be an ipv4 address or nextavailableip to choose one
"""  # nopep8
import sys
import os
from docopt import docopt
from fixedaddress_process_cli import fixedaddress_process_cli
from network_process_cli import network_process_cli
from networkcontainer_process_cli import networkcontainer_process_cli
from host_process_cli import host_process_cli
from global_search_process_cli import global_search_process_cli
from config import get_config


def main():
    opt = docopt(__doc__, version='bloxtool version 0.1.0')
    if opt['--config']:
        config_path = opt['--config']
    else:
        config_path = os.path.join(os.environ["HOME"], ".bloxtool.cfg")
    config = get_config(config_path)
    auth = (config.username, config.password,)
    if opt['fixedaddress']:
        fixedaddress_process_cli(config, auth, opt)
    elif opt['network'] and not opt['networkcontainer'] and not opt['host']:
        network_process_cli(config, auth, opt)
    elif opt['networkcontainer']:
        networkcontainer_process_cli(config, auth, opt)
    elif opt['host']:
        host_process_cli(config, auth, opt)
    elif opt['globalsearch']:
        global_search_process_cli(config, auth, opt)

if __name__ == '__main__':
    main()
