
-- =====================================
-- AI Campus Maintenance Helpdesk Agent
-- Database Schema
-- =====================================

-- USERS TABLE

CREATE TABLE users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE,
role TEXT CHECK(role IN ('Student', 'Staff')) NOT NULL
);

-- DEPARTMENTS TABLE

CREATE TABLE departments (
department_id INTEGER PRIMARY KEY AUTOINCREMENT,
department_name TEXT NOT NULL
);

-- TECHNICIANS TABLE

CREATE TABLE technicians (
technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
skill TEXT NOT NULL,
workload INTEGER DEFAULT 0
);

-- TICKETS TABLE

CREATE TABLE tickets (
ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
issue_description TEXT NOT NULL,
location TEXT NOT NULL,
department_id INTEGER,
technician_id INTEGER,
priority TEXT,
status TEXT DEFAULT 'Open',
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

```
FOREIGN KEY (user_id) REFERENCES users(user_id),
FOREIGN KEY (department_id) REFERENCES departments(department_id),
FOREIGN KEY (technician_id) REFERENCES technicians(technician_id)
```

);

-- TICKET UPDATES TABLE

CREATE TABLE ticket_updates (
update_id INTEGER PRIMARY KEY AUTOINCREMENT,
ticket_id INTEGER NOT NULL,
update_message TEXT NOT NULL,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

```
FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
```

);
