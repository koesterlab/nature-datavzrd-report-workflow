import pandas as pd

input_file = "pan310739-sup-0004-appendixs4.xlsx"
df = pd.read_excel(input_file, dtype=str)

df.columns = df.columns.str.strip()

df["Attribute"] = df["Attribute"].replace("Willingess to invest ($) ($)", "Willingness to invest ($)")
df["Attribute"] = df["Attribute"].replace("Willingess to invest ($)", "Willingness to invest ($)")
df["Block"] = "B" + df["Block"].str.split("B").str[1]
df["Status quo"] = df["Status quo"].str.replace("Zero", "0")

attributes = df["Attribute"].unique()
tables = {attr: df[df["Attribute"] == attr] for attr in attributes}

for attr, table in tables.items():
    output_file = f"{attr}.csv"
    table.to_csv(output_file, index=False, sep=";")
    print(f"Saved {output_file}")
