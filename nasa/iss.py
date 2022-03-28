#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    leialist=resp.values()
    print(leialist)
    print(f"CURRENT LOCATION OF THE ISS:\n",resp["timestamp"])
if __name__ == "__main__":
    main()
