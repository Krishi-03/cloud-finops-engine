import csv
import random
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)
services = ["EC2", "RDS", "S3"]
regions = ["ap-south-1", "us-east-1", "eu-west-1"]

output_file = "data/sample_usage.csv"

def generate_row(date, service, region):
    if service == "EC2":
        instances = random.randint(2, 10)
        cpu = random.randint(20, 85)
        cost = random.randint(80, 200) + (random.randint(300, 500) if random.random() < 0.05 else 0)
    elif service == "RDS":
        instances = random.randint(1, 5)
        cpu = random.randint(15, 70)
        cost = random.randint(60, 200)
    else:  # S3
        instances = 0
        cpu = 0
        cost = random.randint(10, 50)
    
    return [date.strftime("%Y-%m-%d"), service, region, cost, instances, cpu]

rows = []
current_date = start_date

while current_date <= end_date:
    for service in services:
        for region in regions:
            rows.append(generate_row(current_date, service, region))
    current_date += timedelta(days=1)

# Duplicate dataset to exceed 10K rows (365 * 3 * 3 = 3285 → 3285 * 3 ≈ 9855)
rows = rows * 4  # 13,140 rows

with open(output_file, mode="w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "service", "region", "cost", "instances", "cpu_utilization"])
    writer.writerows(rows)

print(f"Dataset generated with {len(rows)} rows.")