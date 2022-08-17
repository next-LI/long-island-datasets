import unicodedata
import re
import requests


def slugify(value, allow_unicode=False):
    # Taken from https://github.com/django/django/blob/master/django/utils/text.py
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = unicodedata.normalize("NFKD", value).encode(
            "ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-\s]+", "-", value).strip("-_")

# wrapper currently does nothing
def grab_data(url, params=None):
  r = requests.get(url, params)
  return r
