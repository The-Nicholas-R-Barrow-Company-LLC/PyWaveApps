from SECRETS import WAVE_APPS_BEARER_TOKEN, WAVE_APPS_BUSINESS_ID
from pywaveapps import WaveApps

if __name__ == "__main__":
    wave = WaveApps(WAVE_APPS_BEARER_TOKEN)
    CUSTOMER = "QnVzaW5lc3M6YzRmNzkzYmItMTQ0OS00NGM2LWEwNGUtYmViODk2OWMzOTRkO0N1c3RvbWVyOjQ4OTI2NjY0"

    res = wave.query.invoices_by_customer(
        WAVE_APPS_BUSINESS_ID,
        CUSTOMER,
        page=1,
        page_size=5,
        list_only=False,
        return_all=True
    )
    ids = [edge['node']['id'] for edge in res['business']['invoices']['edges']]
    unique_ids = []
    [unique_ids.append(id) for id in ids if id not in unique_ids]
    print(len(unique_ids))
