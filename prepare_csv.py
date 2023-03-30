import os


for csv in os.listdir("data/"):
    if csv.endswith(".csv"):
        data = ""
        path = os.path.join("data/", csv)
        with open(path, "r") as f:
            # replace characters
            data = f.read()
            data = data.replace(";", " ")
            data = data.replace(",", ".")

        with open(path, "w") as f:
            f.write(data)

        
