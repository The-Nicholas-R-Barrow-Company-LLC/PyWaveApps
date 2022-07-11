from SECRETS import WAVE_APPS_BEARER_TOKEN, WAVE_APPS_BUSINESS_ID
from pywaveapps import WaveApps

if __name__ == "__main__":
    wave = WaveApps(WAVE_APPS_BEARER_TOKEN)
    CUSTOMER = "QnVzaW5lc3M6YzRmNzkzYmItMTQ0OS00NGM2LWEwNGUtYmViODk2OWMzOTRkO0N1c3RvbWVyOjQ4OTI2NjY0"

    res = wave.query.customers(WAVE_APPS_BUSINESS_ID, page_size=1,  list_only=False, return_all=True)
    print(res)
