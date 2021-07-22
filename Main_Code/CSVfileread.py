import csv
import webbrowser

class create:

    def __init__(self,data):
        self.data = data
        pass

    def run(self):
        print("bfbf")
        # field names
        fields = ['Student 1', 'Student 2', 'Plag %']

        # data rows of csv file
        rows=[]
        for i in self.data:
            x=i.split(":")+[self.data[i]]
            rows.append(x)

        # name of csv file
        filename = "plag_data.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)




