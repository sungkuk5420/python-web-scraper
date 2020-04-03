import csv

def save_to_file(jobs):
  print("start save_to_file")
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","location","price","link"])
  for job in jobs:
    writer.writerow(list(job.values()))  
  print("end save_to_file")
  return 