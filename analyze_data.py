import csv
import os.path

class AnalyzeData():
    def __init__(self):
        with open("HeroList.txt") as file_list:
            self.hero_list = file_list.readlines()
            self.list_length = len(self.hero_list)
            self.clean_list = []
            self.file_path = "data.csv"
            for i in range(0, self.list_length):
                self.hero_list[i] = self.hero_list[i].replace("\n", "")
            for i in range(0, self.list_length):
                self.clean_list.append(self.hero_list[i].lower().replace(" ", "-").translate(None,"'"))

    # reads the data file and saves it in a dictionary
    def read_table(self):
        # Checks for existence of settings file
        rows = {}
        if not os.path.isfile(self.file_path):
            print "data does not exist yet. Please write the table before analyzing."
        else:
            with open(self.file_path) as file_in:
                reader = csv.DictReader(file_in, delimiter = ',')
                i = 0
                for row in reader:
                    current_row = []
                    for key, val in row.items():
                        current_row.append((key, val))

                    current_row = dict(current_row)
                    rows[self.clean_list[i]] = current_row
                    i = i + 1
                    print i, "/", self.list_length
        return rows

    def analyze(self, values, rows, hero):
        val = values
        for check in self.clean_list:
            if rows[check][hero] == "":
                val[check] = 0
            else:
                val[check] = float(val[check])+float(rows[check][hero])
        return val


analysis = AnalyzeData()
rows = analysis.read_table()
values = {}
for i in range(0,analysis.list_length):
    values[analysis.clean_list[i]] = 0
print values
values = analysis.analyze(values, rows, "meepo")
values = analysis.analyze(values, rows, "chaos-knight")
values = analysis.analyze(values, rows, "naga-siren")
values = analysis.analyze(values, rows, "terrorblade")
print values
