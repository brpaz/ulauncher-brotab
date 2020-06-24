import subprocess
import logging

logger = logging.getLogger(__name__)


class BrotabClient:
    """ Client to interact with Brotab Command line tool """

    clients = {}

    tabs = []

    def __init__(self):
        """ Constructor method """
        pass

    def is_installed(self):
        """ Checks if Brotab is installed """
        result = subprocess.run(['which', 'brotab'])

        if result.returncode == 0:
            return True

        return False

    def index(self):
        """ Index Clients and Tabs data """
        logger.info("Indexing tabs data")
        self.index_clients()
        self.index_tabs()

    def index_clients(self):
        """ Index the clients connected """
        self.clients = {}

        result = subprocess.run(['brotab', 'clients'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        output_text = result.stdout.decode("utf-8")
        for line in output_text.splitlines():
            client_info = line.rstrip().split("\t")
            self.clients[client_info[0][:1]] = client_info[3]

    def index_tabs(self):
        """ Index Tabs list """

        self.tabs = []

        result = subprocess.run(['brotab', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        output_text = result.stdout.decode("utf-8")
        if not output_text.strip():
            return

        for line in output_text.splitlines():
            tab = line.rstrip().split("\t")
            self.tabs.append({
                "prefix": tab[0],
                "name": tab[1],
                "url": tab[2],
                "icon": self.get_browser_icon_from_prefix(tab[0][:1])
            })

    def search_tabs(self, filter_term=None):
        """ Returns a list of tabs, optionally filtered by the filter_query parameter """

        if not filter_term:
            return self.tabs

        tabs = []
        for tab in self.tabs:
            if filter_term.lower() in tab["name"].lower() or filter_term.lower() in tab["url"].lower():
                tabs.append(tab)

        return tabs

    def activate_tab(self, prefix):
        """ Activates the tab with the specified prefix """
        subprocess.run(['brotab', 'activate', prefix, '--focused'])

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
