from seleniumbase import SB
import random
import base64
import requests

proxy_ip = "127.0.0.1"
proxy_port = "18080"
proxy_str = False
proxies = {
    "http": proxy_str,
    #"https": proxy_url
}

try:
    geo_data = requests.get("http://ip-api.com/json/", proxies=proxies, timeout=10).json()
    print(geo_data)
except requests.exceptions.RequestException as e:
    print("Proxy request failed:", e)
    geo_data = requests.get("http://ip-api.com/json/").json()
    proxy_str = False
latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'


name = "YnJ1dGFsbGVz"

name_d = base64.b64decode(name)
fulln = name_d.decode("utf-8")
urlt = f"https://www.twitch.tv/{fulln}"

while True:
    with SB(uc=True, locale="en",ad_block=True,chromium_arg='--disable-webgl',proxy = proxy_str) as dregu:
        rnd = random.randint(450,800)
        
        dregu.activate_cdp_mode(urlt,tzone=f"{timezone_id}",geoloc=(latitude, longitude))
        dregu.sleep(2)
        if dregu.is_element_present('button:contains("Accept")'):
            dregu.cdp.click('button:contains("Accept")', timeout=4)
        dregu.sleep(2)    
        #dregu.cdp.gui_click_element('#page-manager > ytd-browse')
        #dregu.cdp.gui_click_element('#items > ytd-grid-video-renderer:nth-child(1)')
        dregu.sleep(12)
        if dregu.is_element_present('button:contains("Start Watching")'):
            dregu.cdp.click('button:contains("Start Watching")', timeout=4)
            dregu.sleep(10)
        if dregu.is_element_present('button:contains("Accept")'):
            dregu.cdp.click('button:contains("Accept")', timeout=4)
        if dregu.is_element_present("#live-channel-stream-information"):
        
            if dregu.is_element_present('button:contains("Accept")'):
                dregu.cdp.click('button:contains("Accept")', timeout=4)
            if True:
                dregu2 = dregu.get_new_driver(undetectable=True)
                dregu2.activate_cdp_mode(urlt,tzone=f"{timezone_id}",geoloc=(latitude, longitude))
                dregu2.sleep(10)
                if dregu2.is_element_present('button:contains("Start Watching")'):
                    dregu2.cdp.click('button:contains("Start Watching")', timeout=4)
                    dregu2.sleep(10)
                if dregu2.is_element_present('button:contains("Accept")'):
                    dregu2.cdp.click('button:contains("Accept")', timeout=4)
                dregu.sleep(10)
                dregu.sleep(rnd)
        else:
            break
