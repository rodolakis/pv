import os
import time

from epics import PV
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from pv import log


def onChanges(pvname=None, value=None, char_value=None, **kw):
    log.info('PV Changed! %s %s %s', pvname, char_value, time.ctime())
    bot_token = os.environ.get("BOT_TOKEN")
    app_token = os.environ.get("APP_TOKEN") 

    # WebClient insantiates a client that can call API methods
    # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
    client = WebClient(token=bot_token)
    # ID of channel you want to post message to
    channel_id = "automated"
    message = pvname + ': ' + char_value
    try:
        # Call the conversations.list method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id,
            text=message
            # You could also use a blocks[] array to send richer content
        )
 
    except SlackApiError as e:
        log.error(f"Error: {e}")

def check_pvs_connected(epics_pvs):
    """Checks whether all EPICS PVs are connected.
    Returns
    -------
    bool
        True if all PVs are connected, otherwise False.
    """

    slack_messages = ()
    all_connected = True
    for key in epics_pvs:
        if not epics_pvs[key].connected:
            log.error('PV %s is not connected', epics_pvs[key].pvname)
            slack_messages += ('\nPV ' + epics_pvs[key].pvname + ' is not connected', )
            all_connected = False
        else:
            log.info('%s: %s' % (key, epics_pvs[key].get(as_string=True)))
            slack_messages += ('\n' + key + ': ' + epics_pvs[key].get(as_string=True), )

    return all_connected, slack_messages
