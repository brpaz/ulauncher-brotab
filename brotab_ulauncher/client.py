import subprocess
import logging
from brotab_ulauncher.brotab import return_clients, return_tabs, activate_tab, close_tab
from asyncio import new_event_loop, set_event_loop
from memoization import cached
logger = logging.getLogger(__name__)


class BrotabClient:
    """ Client to interact with Brotab Command line tool """

    clients = {}

    def __init__(self):
        """ Constructor method """
        pass

    @cached(ttl=15)
    def is_installed(self):
        """ Checks if Brotab is installed """
        result = subprocess.run(['which', 'brotab'])

        if result.returncode == 0:
            return True

        return False

    def index_clients(self):
        """ Index the clients connected """
        self.clients = {}
        clients = return_clients()
        for client in clients:
            self.clients[client.__dict__["_prefix"].replace(".", "")] = client.__dict__["_browser"]

    @cached(ttl=5)
    def fetch_tabs(self):
        """ Index Tabs list """
        logger.info("Fetching tabs")
        self.index_clients()

        loop = new_event_loop()
        set_event_loop(loop)
        tabs_listed = return_tabs()

        tabs = []
        for tab in tabs_listed:
            tab = tab.split("\t")
            tabs.append({
                "prefix": tab[0],
                "name": tab[1],
                "url": tab[2],
                "icon": self.get_browser_icon_from_prefix(tab[0][:1])
            })

        return tabs

    def search_tabs(self, filter_term=None):
        """ Returns a list of tabs, optionally filtered by the filter_query parameter """

        allTabs = self.fetch_tabs()
        if not filter_term:
            return allTabs

        tabs = []
        for tab in allTabs:
            if filter_term.lower() in tab["name"].lower() or filter_term.lower() in tab["url"].lower():
                tabs.append(tab)

        return tabs

    def activate_tab(self, prefix):
        """ Activates the tab with the specified prefix """
        activate_tab(prefix)

    def close_tab(self, prefix):
        """ Closes the tab with the specified prefix """
        close_tab(prefix)

    def get_browser_icon_from_prefix(self, prefix):
        """ Returns the name of the icon to display as client """

        if prefix not in self.clients.keys():
            return 'icon.png'

        client = self.clients.get(prefix)
        if "chrome" in client:
            return 'icon-chrome.png'

        if "firefox" in client:
            return "icon-firefox.png"

        if "brave" in client:
            return "icon-brave.png"

        return "icon.png"
