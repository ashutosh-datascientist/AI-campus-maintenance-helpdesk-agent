# =====================================================
# AI Campus Maintenance Helpdesk Agent
# Generate Synthetic Tickets Dataset
# =====================================================

import pandas as pd
import random

# -----------------------------------------------------
# Sample Users
# (Later we'll read from users.csv)
# -----------------------------------------------------

users = [
    ("Rahul Patil", "Student"),
    ("Priya Sharma", "Student"),
    ("Aarav Deshmukh", "Student"),
    ("Anita Kulkarni", "Staff"),
    ("Vikas More", "Staff")
]

# -----------------------------------------------------
# Ticket Status
# -----------------------------------------------------

statuses = [
    "Open",
    "In Progress",
    "Resolved"
]

# -----------------------------------------------------
# Sample Complaints
# -----------------------------------------------------

issues = [

    ("WiFi connectivity issue in Computer Science Lab 204",
     "B Building",
     "Computer Science Lab 204",
     "Technology Services"),

    ("Projector not functioning in Civil Engineering Classroom 201",
     "A Building",
     "Civil Engineering Classroom 201",
     "Technology Services"),

    ("Broken washroom mirror in Girls Washroom Second Floor",
     "C Building",
     "Girls Washroom - Second Floor",
     "Housekeeping Services"),

    ("Fan not working in Mechanical Engineering Classroom 203",
     "A Building",
     "Mechanical Engineering Classroom 203",
     "Electrical Maintenance"),

    ("Water leakage near Boys Washroom Ground Floor",
     "D Building",
     "Boys Washroom - Ground Floor",
     "Plumbing Maintenance"),

    ("Broken classroom chair in Law Classroom 205",
     "D Building",
     "Law Classroom 205",
     "Civil Maintenance"),

    ("Microscope malfunction in Biotechnology Laboratory",
     "E Building",
     "Biotechnology Laboratory",
     "Laboratory Equipment Support"),

    ("AC not cooling in MBA Classroom 302",
     "C Building",
     "MBA Classroom 302",
     "Air Conditioning & Ventilation Services"),

    ("CCTV camera not working near Main Gate",
     "Main Building",
     "Main Gate",
     "Security & Surveillance"),

    ("Washroom foul smell reported in Boys Washroom",
     "B Building",
     "Boys Washroom",
     "Housekeeping Services")
]

# -----------------------------------------------------
# Store Tickets
# -----------------------------------------------------

tickets = []

# -----------------------------------------------------
# Generate 2000 Tickets
# -----------------------------------------------------

for i in range(2000):

    user_name, user_role = random.choice(users)

    issue, building, location, department = random.choice(issues)

    status = random.choice(statuses)

    ticket_id = f"TKT{i+1:06d}"

    tickets.append([
        ticket_id,
        user_name,
        user_role,
        issue,
        building,
        location,
        department,
        status
    ])

# -----------------------------------------------------
# Create DataFrame
# -----------------------------------------------------

df = pd.DataFrame(
    tickets,
    columns=[
        "ticket_id",
        "user_name",
        "user_role",
        "issue_description",
        "building",
        "location",
        "department",
        "status"
    ]
)

# -----------------------------------------------------
# Save CSV
# -----------------------------------------------------

df.to_csv(
    "tickets.csv",
    index=False
)

print("tickets.csv generated successfully!")
print("Total Tickets:", len(df))
