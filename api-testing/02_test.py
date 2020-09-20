import requests
import pytest

test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("us", "12345", "Schenectady"),
    ("ca", "B2R", "Waverley")
]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_data_object_check_place_name(country_code, zip_code, expected_place_name):
    r = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    data = r.json()
    assert (r.status_code == 200 and \
        r.headers['Content-Type'] == "application/json" and \
        r.elapsed.total_seconds() < 1 and \
            data["places"][0]["place name"] == expected_place_name)