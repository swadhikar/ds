"""
Fetch the aircraft fueling info from transtats website and store them in
python object

https://www.transtats.bts.gov/fuel.asp?pn=1
"""
import requests
import os

url = 'https://www.transtats.bts.gov/fuel.asp?pn=1'
out = '/home/swadhi/Desktop'


def disable_warnings():
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass


disable_warnings()

if __name__ == '__main__':
    _session = requests.Session()
    airlines = 'AA: American Airlines'
    _payload = {"Carrier": airlines, "Service": "Scheduled"}
    response = _session.post(url, data=_payload)

    print(f'Request completed for: {airlines}')

    if response.status_code == 200:
        with open(os.path.join(out, 'response.html'), 'w') as f:
            f.write(response.text)
    else:
        raise Exception(response.status_code)
