def get_public_ip():
    from requests import get
    return get('https://api.ipify.org').text