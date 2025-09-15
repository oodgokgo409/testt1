from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as eyyetete:

    url = "https://kick.com/s3jl"
    eyyetete.uc_open_with_reconnect(url, 4)
    eyyetete.sleep(4)
    eyyetete.uc_gui_click_captcha()
    eyyetete.sleep(1)
    eyyetete.uc_gui_handle_captcha()
    eyyetete.sleep(4)
    if eyyetete.is_element_present('button:contains("Accept")'):
        eyyetete.uc_click('button:contains("Accept")', reconnect_time=4)
    if eyyetete.is_element_visible('#injected-channel-player'):
        sfauiojt2 = eyyetete.get_new_driver(undetectable=True)
        sfauiojt2.uc_open_with_reconnect(url, 5)
        sfauiojt2.uc_gui_click_captcha()
        sfauiojt2.uc_gui_handle_captcha()
        eyyetete.sleep(10)
        if sfauiojt2.is_element_present('button:contains("Accept")'):
            sfauiojt2.uc_click('button:contains("Accept")', reconnect_time=4)
        while eyyetete.is_element_visible('#injected-channel-player'):
            eyyetete.sleep(10)
        eyyetete.quit_extra_driver()
    eyyetete.sleep(1)
    if is_stream_online("s3jl"):
        url = "https://www.twitch.tv/s3jl"
        eyyetete.uc_open_with_reconnect(url, 5)
        if eyyetete.is_element_present('button:contains("Accept")'):
            eyyetete.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            sfauiojt2 = eyyetete.get_new_driver(undetectable=True)
            sfauiojt2.uc_open_with_reconnect(url, 5)
            eyyetete.sleep(10)
            if sfauiojt2.is_element_present('button:contains("Accept")'):
                sfauiojt2.uc_click('button:contains("Accept")', reconnect_time=4)
            while eyyetete.is_element_visible(input_field):
                eyyetete.sleep(10)
            eyyetete.quit_extra_driver()
    eyyetete.sleep(1)

