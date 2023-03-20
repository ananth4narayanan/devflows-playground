
# importing csv module
import csv
 
# csv file name
filename = "Onyx - Incident Table - Sheet1.csv"

filename2 = "Combined1.csv"
filehandle2 = open(filename2,'w');
writer = csv.writer(filehandle2);
        
# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        for i in range(2):
            writer.writerow(row);
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

filehandle2.close();
