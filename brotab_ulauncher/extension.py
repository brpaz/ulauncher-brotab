"""
Extension Class
"""
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.item.ExtensionSmallResultItem import ExtensionSmallResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from brotab_ulauncher.client import BrotabClient
from brotab_ulauncher.listeners import KeywordQueryEventListener, ItemEnterEventListener

DISPLAY_MAX_RESULTS = 20


class BrotabExtension(Extension):
    """ Main Extension Class  """
    def __init__(self):
        """ Initializes the extension """
        super(BrotabExtension, self).__init__()

        self.logger.info("Initializing Brotab Extension")

        self.brotab_client = BrotabClient()
        self.mode = "activator"

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def show_no_results_message(self):
        """ Shows empty list results """
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name='No tabs found matching your criteria',
                                highlightable=False,
                                on_enter=HideWindowAction())
        ])

    def search_tabs(self, event):
        """ Search tabs """

        if not self.brotab_client.is_installed():
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='Brotab is not installed on your system',
                                    description='Press enter to open install instructions.',
                                    highlightable=False,
                                    on_enter=OpenUrlAction('https://github.com/balta2ar/brotab#installation'))
            ])

        items = []
        tabs = self.brotab_client.search_tabs(event.get_argument())

        for tab in tabs[:DISPLAY_MAX_RESULTS]:
            data = {'tab': tab['prefix'], 'mode': self.mode}

            items.append(
                ExtensionSmallResultItem(icon='images/%s' % tab["icon"],
                                         name=tab["name"],
                                         description=tab['url'],
                                         on_enter=ExtensionCustomAction(data),
                                         on_alt_enter=CopyToClipboardAction(tab["url"])))

        if not items:
            return self.show_no_results_message()

        return RenderResultListAction(items)
