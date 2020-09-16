import json

import pandas as pd

OWGR_URL = "http://www.owgr.com/ranking?pageNo=1&pageSize=All&country=All"

# Form dictionary of OWGR
owgr_df = pd.read_html(OWGR_URL)[0].set_index("Name").drop(columns="Ctry")
owgr_dict = owgr_df.to_dict()["This Week"]

# Dump as json
with open("current_owgr.json", "w") as outfile:
    json.dump(owgr_dict, outfile)
