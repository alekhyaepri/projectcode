import csv
import glob
import os
from itertools import islice

directory = "/home/ubuntu/Downloads/single actor IP theft/data/dhcp"
output = "/home/ubuntu/output"


log_files = os.path.join(directory, '*.log')
csv_files = os.path.join(output, '*.csv')

for log_file in glob.glob(log_files):
	with open(log_file, "rb") as input_file:
		in_log = '\n'.join(islice(input_file,33,))
		in_log = csv.reader(input_file, delimiter=',')
		filename = os.path.splitext(os.path.basename(log_file))[0] + '.csv'
		with open(os.path.join(output, filename), 'wb') as output_file:
			out_csv = csv.writer(output_file)
			out_csv.writerows(in_log)

with open("result.csv", "w") as outfile:
	writer = csv.DictWriter(outfile, fieldnames = ["ID","Date","Time","Description","IP Adress","Host Name","MAC Address","User Name","TransactionID","QResult","PartitionTime","CorrelationID","Dhcid"])
	writer.writeheader()
	for files in  glob.glob(csv_files):
		with open(files, "rb") as infile:
			outfile.write(infile.read())
	

			
