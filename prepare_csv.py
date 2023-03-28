import os

for csv in os.listdir("data/"):
    if csv.endswith(".csv"):
        with open(os.path.join("data/", csv), "r+") as f:
            # replace characters
            data = f.read()
            data = data.replace(";", " ")
            data = data.replace(",", ".")
            f.write(data)
