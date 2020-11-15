from ulauncher.api.client.EventListener import EventListener
from brotab_ulauncher.actions import RESULT_ITEM_ENTER, REFRESH_TABS
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    def on_event(self, event, extension):
        """ Handles the event """
        keyword = event.get_keyword() or ""
        valid_keywords = ["cltab","cl","clt"]
        if keyword in valid_keywords:
            extension.mode = "killer"
        else:
            extension.mode = "activator"

        argument = event.get_argument() or ""

        if argument.startswith(":"):
            return extension.show_commands(argument)
        return extension.search_tabs(event)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()
        if data["action"] == RESULT_ITEM_ENTER and data["mode"] == "activator":
            extension.brotab_client.activate_tab(data["tab"])
        if data["action"] == RESULT_ITEM_ENTER and data["mode"] == "killer":
            try:
                extension.brotab_client.close_tab(data["tab"])
            except Exception as error:
                print(error)
            extension.notify("Tab closed")
            print("Tab closed")
        if data["action"] == REFRESH_TABS:
            extension.brotab_client.index()
            print(extension.preferences.keys())
            dict_mode = {"activator": "kw", "killer": "kw_cl"}
            kw = extension.preferences[dict_mode[extension.mode]]
            extension.notify("Index Finished")
            return SetUserQueryAction("%s " % kw)
