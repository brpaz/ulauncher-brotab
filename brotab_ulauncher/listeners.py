from ulauncher.api.client.EventListener import EventListener
from brotab_ulauncher.actions import RESULT_ITEM_ENTER, REFRESH_TABS
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    def on_event(self, event, extension):
        """ Handles the event """
        argument = event.get_argument() or ""

        if argument.startswith(":"):
            return extension.show_commands(argument)
        print("RENDER")
        return extension.search_tabs(event)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()
        print("hola listen", data)
        if data["action"] == RESULT_ITEM_ENTER:
            print(data["action"])
            print(data["tab"])
            extension.brotab_client.activate_tab(data["tab"])

        if data["action"] == REFRESH_TABS:
            extension.brotab_client.index()
            kw = extension.preferences["kw"]
            extension.notify("Index Finished")
            return SetUserQueryAction("%s " % kw)
