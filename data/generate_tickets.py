# =====================================================
# AI Campus Maintenance Helpdesk Agent
# Generate Synthetic Tickets Dataset
# =====================================================

import pandas as pd
import random

# =====================================================
# READ USERS DATASET
# =====================================================

users_df = pd.read_csv("users.csv")

users = list(
    zip(
        users_df["name"],
        users_df["role"]
    )
)

# =====================================================
# TICKET STATUS
# =====================================================

statuses = [
    "Open",
    "In Progress",
    "Resolved"
]

# =====================================================
# ISSUE TEMPLATES
# =====================================================

issues = [

# Technology Services

("WiFi connectivity issue in Computer Science Lab 204","B Building","Computer Science Lab 204","Technology Services"),
("Internet outage in Programming Lab 101","B Building","Programming Lab 101","Technology Services"),
("Projector not functioning in Civil Engineering Classroom 201","A Building","Civil Engineering Classroom 201","Technology Services"),
("Smart board display malfunction in MBA Classroom 302","C Building","MBA Classroom 302","Technology Services"),
("Printer not responding in Administration Office","Main Building","Administration Office","Technology Services"),
("Computer not starting in Biotechnology Laboratory","E Building","Biotechnology Laboratory","Technology Services"),
("Network connectivity issue in Faculty Room","Main Building","Faculty Room","Technology Services"),
("LAN cable port not working in Computer Science Lab","B Building","Computer Science Lab","Technology Services"),
("Online examination system inaccessible","Main Building","Examination Cell","Technology Services"),
("Server connectivity issue reported","Main Building","Server Room","Technology Services"),

# Electrical Maintenance

("Fan not working in Mechanical Engineering Classroom 203","A Building","Mechanical Engineering Classroom 203","Electrical Maintenance"),
("Tube light not functioning in Commerce Classroom 204","C Building","Commerce Classroom 204","Electrical Maintenance"),
("Power outage in Geography Classroom","D Building","Geography Classroom","Electrical Maintenance"),
("Electrical socket damaged in Library Reading Hall","Main Building","Library Reading Hall","Electrical Maintenance"),
("Switch board malfunction near Auditorium Entrance","Main Building","Auditorium Entrance","Electrical Maintenance"),
("Classroom lights flickering in English Department","D Building","English Department","Electrical Maintenance"),
("Emergency light not operational","Main Building","Corridor","Electrical Maintenance"),
("Ceiling fan making unusual noise","A Building","Civil Engineering Classroom","Electrical Maintenance"),

# Plumbing Maintenance

("Water leakage near Boys Washroom Ground Floor","D Building","Boys Washroom Ground Floor","Plumbing Maintenance"),
("Broken washroom commode in Girls Washroom","C Building","Girls Washroom","Plumbing Maintenance"),
("Flush system not working","A Building","Boys Washroom","Plumbing Maintenance"),
("Water tap damaged in Biotechnology Laboratory","E Building","Biotechnology Laboratory","Plumbing Maintenance"),
("Wash basin leakage reported","Main Building","Administration Block","Plumbing Maintenance"),

# Civil Maintenance

("Broken classroom chair reported","A Building","Civil Engineering Classroom 202","Civil Maintenance"),
("Broken classroom table reported","B Building","Computer Science Classroom 301","Civil Maintenance"),
("Broken cupboard in faculty cabin","D Building","Faculty Cabin","Civil Maintenance"),
("Window glass damaged","C Building","MBA Classroom 305","Civil Maintenance"),
("Door lock damaged","Main Building","Administration Office","Civil Maintenance"),

# Laboratory Equipment Support

("Microscope malfunction in Biotechnology Laboratory","E Building","Biotechnology Laboratory","Laboratory Equipment Support"),
("Pharmacy lab equipment not functioning","E Building","Pharmacy Laboratory","Laboratory Equipment Support"),
("Lab workstation not operational","B Building","Computer Science Lab","Laboratory Equipment Support"),
("Biotechnology analyzer error reported","E Building","Biotechnology Lab","Laboratory Equipment Support"),
("Digital weighing machine failure","E Building","Pharmacy Laboratory","Laboratory Equipment Support"),

# Air Conditioning & Ventilation Services

("AC not cooling in MBA Classroom 302","C Building","MBA Classroom 302","Air Conditioning & Ventilation Services"),
("AC water leakage reported","Main Building","Auditorium","Air Conditioning & Ventilation Services"),
("Ventilation issue in Biotechnology Lab","E Building","Biotechnology Laboratory","Air Conditioning & Ventilation Services"),
("Air circulation issue reported","Main Building","Library Reading Hall","Air Conditioning & Ventilation Services"),

# Security & Surveillance

("CCTV camera not working near Main Gate","Main Building","Main Gate","Security & Surveillance"),
("Parking area surveillance issue reported","Main Building","Parking Area","Security & Surveillance"),
("Security access system malfunction","Main Building","Administration Block","Security & Surveillance"),
("Camera lens damaged","B Building","Computer Science Entrance","Security & Surveillance"),

# Housekeeping Services

("Washroom unclean in Boys Washroom","A Building","Boys Washroom","Housekeeping Services"),
("Washroom foul smell reported","B Building","Girls Washroom","Housekeeping Services"),
("Broken washroom mirror reported","C Building","Girls Washroom Second Floor","Housekeeping Services"),
("Garbage accumulation near building entrance","D Building","Main Entrance","Housekeeping Services"),
("Laboratory cleaning required","E Building","Biotechnology Laboratory","Housekeeping Services"),
("Classroom cleaning required","A Building","Civil Engineering Classroom","Housekeeping Services"),
("Dust accumulation in library","Main Building","Library Reading Hall","Housekeeping Services"),
("Corridor cleaning required","B Building","Second Floor Corridor","Housekeeping Services")
]

# =====================================================
# STORE TICKETS
# =====================================================

tickets = []

# =====================================================
# GENERATE 2000 TICKETS
# =====================================================

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

# =====================================================
# CREATE DATAFRAME
# =====================================================

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

# =====================================================
# SAVE CSV
# =====================================================

df.to_csv(
    "tickets.csv",
    index=False
)

print("tickets.csv generated successfully!")
print("Total Tickets:", len(df))
