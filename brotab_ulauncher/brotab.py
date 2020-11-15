import logging
from string import ascii_lowercase

from typing import Tuple, List

from brotab.inout import is_port_accepting_connections
from brotab.inout import get_mediator_ports
from brotab.inout import in_temp_dir
from brotab.api import SingleMediatorAPI, MultipleMediatorsAPI

FORMAT = '%(asctime)-15s %(levelname)-10s %(message)s'
logging.basicConfig(format=FORMAT, filename=in_temp_dir('brotab.log'), level=logging.DEBUG)
logger = logging.getLogger('brotab')
logger.info('Logger has been created')


def parse_target_hosts(target_hosts: str) -> Tuple[List[str], List[int]]:
    """
    Input: localhost:2000,127.0.0.1:3000
    Output: (['localhost', '127.0.0.1'], [2000, 3000])
    """
    hosts, ports = [], []
    for pair in target_hosts.split(','):
        host, port = pair.split(':')
        hosts.append(host)
        ports.append(int(port))
    return hosts, ports


def create_clients(target_hosts=None) -> List[SingleMediatorAPI]:
    if target_hosts is None:
        ports = list(get_mediator_ports())
        hosts = ['localhost'] * len(ports)
    else:
        hosts, ports = parse_target_hosts(target_hosts)

    result = [
        SingleMediatorAPI(prefix, host=host, port=port) for prefix, host, port in zip(ascii_lowercase, hosts, ports)
        if is_port_accepting_connections(port, host)
    ]
    logger.info('Created clients: %s', result)
    return result


def return_tabs():
    logger.info('Listing tabs')
    api = MultipleMediatorsAPI(create_clients())
    tabs = api.list_tabs([])
    return tabs


def activate_tab(prefix):
    api = MultipleMediatorsAPI(create_clients())
    api.activate_tab([prefix], True)


def close_tab(prefix):
    # Try stdin if arguments are empty
    logger.info('Closing tabs: %s', prefix)
    api = MultipleMediatorsAPI(create_clients())
    api.close_tabs([prefix])


def return_clients():
    logger.info('Showing clients')
    return create_clients()
