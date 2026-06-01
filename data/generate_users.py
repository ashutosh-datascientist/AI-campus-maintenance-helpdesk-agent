# =====================================================
# AI Campus Maintenance Helpdesk Agent
# Generate Synthetic Users Dataset
# =====================================================

import pandas as pd
import random

# Sample first names
first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Krishna",
    "Rohan", "Rahul", "Karan", "Vikas", "Siddharth",
    "Priya", "Anjali", "Neha", "Pooja", "Sneha",
    "Meera", "Riya", "Kavya", "Aditi", "Shreya"
]

# Sample last names
last_names = [
    "Sharma", "Patil", "Deshmukh", "Kulkarni",
    "More", "Joshi", "Pawar", "Jadhav",
    "Chavan", "Kale", "Mane", "Shinde"
]

users = []

# -----------------------------------------------------
# Generate 700 Students
# -----------------------------------------------------
for i in range(700):

    first = random.choice(first_names)
    last = random.choice(last_names)

    name = f"{first} {last}"

    email = (
        f"{first.lower()}."
        f"{last.lower()}"
        f"{i+1}@campus.edu"
    )

    users.append(
        [name, email, "Student"]
    )

# -----------------------------------------------------
# Generate 300 Staff
# -----------------------------------------------------
for i in range(300):

    first = random.choice(first_names)
    last = random.choice(last_names)

    name = f"{first} {last}"

    email = (
        f"{first.lower()}."
        f"{last.lower()}"
        f"{700+i+1}@campus.edu"
    )

    users.append(
        [name, email, "Staff"]
    )

# -----------------------------------------------------
# Create DataFrame
# -----------------------------------------------------
df = pd.DataFrame(
    users,
    columns=[
        "name",
        "email",
        "role"
    ]
)

# -----------------------------------------------------
# Save CSV
# -----------------------------------------------------
df.to_csv(
    "users.csv",
    index=False
)

print("users.csv generated successfully!")
print("Total Users:", len(df))
