import requests


def test_check_status_code_equals_200_and_content_type_is_json():
    r = requests.get("http://api.zippopotam.us/de/bw/stuttgart")
    assert (r.status_code == 200 and r.headers['Content-Type'] == "application/json")


def test_response_time_is_less_than_1s():
    r = requests.get("http://api.zippopotam.us/de/bw/stuttgart")
    assert (r.elapsed.total_seconds() < 1)


def test_country_and_state_are_germany_and_bw():
    r = requests.get("http://api.zippopotam.us/de/bw/stuttgart")
    data = r.json()
    assert(data['country'] == 'Germany' and \
        data['state'] == 'Baden-Württemberg')


def test_stutgart_degerloch_70597():
    r = requests.get("http://api.zippopotam.us/de/bw/stuttgart")
    data = r.json()
    assert next(i for i in data['places'] \
        if i['place name'] == 'Stuttgart Degerloch' and i['post code'] == '70597')