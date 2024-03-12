from celery import shared_task,Task
from time import sleep
import pandas as pd
import csv

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def read_csv(path):

  try:
    df = pd.read_csv(path)
    
    return "Successful"
       
  except FileNotFoundError:
    return "error reading file: File not found"
  except Exception as e:
    return f"error reading file: {e}"
  

@shared_task 
def display_csv(path):
  try:
    df = pd.read_csv(path)
    
    html_table = df.to_html(index=False)
    return html_table
       
  except FileNotFoundError:
    return "error reading file: File not found"
  except Exception as e:
    return f"error reading file: {e}"
  
