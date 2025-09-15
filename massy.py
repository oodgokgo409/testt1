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

from dataclasses import dataclass
from typing import List, Optional
@dataclass
class Resolution:
    width: int
    height: int
    bits_per_pixel: Optional[int] = None

def get_random_resolution(bits_per_pixel_options: List[int] = [16, 24, 32]) -> Resolution:
    """
    Generate a random screen resolution with random variations.
    
    Args:
        bits_per_pixel_options (List[int]): List of possible color depths. Defaults to [16, 24, 32].
        
    Returns:
        Resolution: A Resolution object containing width, height, and bits per pixel.
    """
    # 1) Define base resolutions up to 4K
    base_resolutions = [
        Resolution(1280, 800),   # WXGA
        Resolution(1366, 768),   # HD+
    ]
    
    # 2) Choose a random base resolution
    base = random.choice(base_resolutions)
    
    # 3) Choose a random bits-per-pixel
    bpp = random.choice(bits_per_pixel_options)
    
    # 4) Compute random offsets between -10% and +10%
    w_offset = random.randint(-10, 10) / 100.0
    h_offset = random.randint(-10, 10) / 100.0
    
    # 5) Apply offsets and round
    new_width = round(base.width * (1 + w_offset))
    new_height = round(base.height * (1 + h_offset))
    
    # 6) Return a Resolution object
    return Resolution(new_width, new_height, bpp)

#unlock_expired_documents()
resolution = get_random_resolution()
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

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

with SB(uc=True, test=True,locale=f"{language_code.upper()}") as eyyetete:
    eyyetete.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    eyyetete.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    eyyetete.set_window_size(resolution.width, resolution.height)
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
            while is_stream_online("s3jl"):
                eyyetete.sleep(10)
            eyyetete.quit_extra_driver()
    eyyetete.sleep(1)

