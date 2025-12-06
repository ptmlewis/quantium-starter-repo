import csv

import_files = ['/Users/peterlewis/Desktop/Quantium/quantium-starter-repo/data/daily_sales_data_0.csv','/Users/peterlewis/Desktop/Quantium/quantium-starter-repo/data/daily_sales_data_1.csv','/Users/peterlewis/Desktop/Quantium/quantium-starter-repo/data/daily_sales_data_2.csv']
output_file = '/Users/peterlewis/Desktop/Quantium/quantium-starter-repo/ new-file.csv'

with open(output_file, mode='w',newline='') as outfile:
    csv_writer = csv.writer(outfile)
    
    csv_writer.writerow(['Sales','Date','Region'])

    for file_path in import_files:
        with open(file_path, mode='r') as infile:
            csv_reader = csv.reader(infile)
            header = next(csv_reader)

            for row in csv_reader:
                if row[0] == "pink morsel":
                    sales_price = float(row[1][1:])
                    quantity = int(row[2])
                    sale = sales_price * quantity
                    date = row[3]
                    region = row[4]
            
                csv_writer.writerow([sale,date,region])
