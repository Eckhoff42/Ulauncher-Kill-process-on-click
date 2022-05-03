import json
import logging
import os
from time import sleep
from unicodedata import name
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        devices = {}
        logger.info('preferences %s' % json.dumps(extension.preferences))

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Kill process',
                                         description='Click on the process you want to kill',
                                         on_enter=ExtensionCustomAction()))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):

    def on_event(self, event, extension):

        ret = os.system(
            f"bash -c 'xkill'")

        return RenderResultListAction([ExtensionResultItem(icon='images/icon.png',
                                                           name=prompt,
                                                           on_enter=HideWindowAction())])


if __name__ == '__main__':
    DemoExtension().run()
