"""
Extension Class
"""
from threading import Timer
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from brotab_ulauncher.client import BrotabClient
from brotab_ulauncher.listeners import KeywordQueryEventListener, ItemEnterEventListener
from brotab_ulauncher.actions import RESULT_ITEM_ENTER, REFRESH_TABS
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

DISPLAY_MAX_RESULTS = 20
INDEX_REFRESH_TIME_SECONDS = 60


class BrotabExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(BrotabExtension, self).__init__()

        self.logger.info("Initializing Brotab Extension")
        Notify.init(__name__)

        self.brotab_client = BrotabClient()

        if not self.brotab_client.is_installed():
            raise EnvironmentError("Brotab is not installed on your system. \
                    Please see https://github.com/balta2ar/brotab for instructions.")

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        self.index_tabs()

    def index_tabs(self):
        """ Index brotab tabs """
        self.brotab_client = BrotabClient()
        self.brotab_client.index()
        Timer(INDEX_REFRESH_TIME_SECONDS, self.index_tabs).start()

    def show_commands(self, arg):
        """ Show Extension commands """
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name='Refresh Tabs',
                                highlightable=False,
                                on_enter=ExtensionCustomAction({
                                    "action": REFRESH_TABS,
                                }, keep_app_open=True))
        ])

    def show_no_results_message(self):
        """ Shows empty list results """
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name='No tabs found matching your criteria',
                                highlightable=False,
                                on_enter=HideWindowAction())
        ])

    def notify(self, text):
        """ Shows Notification """
        Notify.Notification.new("Brotab", text).show()

    def search_tabs(self, event):
        """ Search tabs """
        items = []
        tabs = self.brotab_client.search_tabs(event.get_argument())

        for tab in tabs[:DISPLAY_MAX_RESULTS]:
            data = {"action": RESULT_ITEM_ENTER, 'tab': tab['prefix']}

            items.append(
                ExtensionSmallResultItem(icon='images/%s' % tab["icon"],
                                         name=tab["name"],
                                         description=tab['url'],
                                         on_enter=ExtensionCustomAction(data),
                                         on_alt_enter=CopyToClipboardAction(tab["url"])))

        if not items:
            return self.show_no_results_message()

        return RenderResultListAction(items)
