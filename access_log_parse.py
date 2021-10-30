import re
from collections import Counter

import csv
import argparse

logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open("access_log") as f:
    fread = f.read()
    ip_list = re.findall(logreg, fread)
    for k, v in Counter(ip_list).items():
        print(k,v)