import win32com.client
import csv


outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")


with open ('calander.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter =',')
    for row in csv_reader:
        start_date = row['start_date']
        start_time = row['start_time']
        subject = row['subject']
        duration = row['duration_mins']
        appointment = outlook.CreateItem(1) # 1=outlook appointment item
        appointment.Start = start_date + ' '+start_time
        appointment.Subject = subject
        appointment.Duration = duration
        appointment.Save()