"""
Extension event listeners
"""
from ulauncher.api.client.EventListener import EventListener


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """
    def on_event(self, event, extension):
        """ Handles the event """
        keyword = event.get_keyword() or ""
        valid_keywords = ["cltab", "cl", "clt"]
        if keyword in valid_keywords:
            extension.mode = "killer"
        else:
            extension.mode = "activator"

        return extension.search_tabs(event)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()
        if data["mode"] == "activator":
            extension.brotab_client.activate_tab(data["tab"])
        if data["mode"] == "killer":
            try:
                extension.brotab_client.close_tab(data["tab"])
            except Exception as error:
                extension.logger.error(error)

            extension.logger.info("Tab closed")
