from aurochs.app import get_request

URL = "https://python.org/jobs"


def test_get_request():
    r = get_request(URL)
    assert r.status_code == 200
