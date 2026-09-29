# Student Attendance Management System

A Python-based Student Attendance Management System developed for the CSE1021 – Introduction to Problem Solving and Programming course.

## Project Description

The Student Attendance Management System helps students calculate and monitor their attendance percentage. It also analyzes attendance status and calculates how many upcoming classes a student needs to attend to reach a desired attendance target.

The project is implemented as a console-based Python application using basic programming and problem-solving concepts.

## Features

- Calculate attendance percentage
- Analyze attendance status
- Calculate required upcoming classes to reach a target percentage
- Validate user input
- Save attendance records in a text file
- Provide basic attendance advice

## Attendance Status

- 90% and above – Excellent
- 75% to below 90% – Good
- 65% to below 75% – Warning
- Below 65% – Critical

## Project Modules

- `main.py` – Main menu and program control
- `attendance_calculator.py` – Calculates attendance percentage
- `attendance_analyzer.py` – Analyzes attendance and provides advice
- `required_classes.py` – Calculates required upcoming classes
- `validation.py` – Handles input validation
- `file_manager.py` – Saves attendance records

## Technologies Used

- Python
- Command Prompt
- Text file handling

## How to Run

1. Open Command Prompt.
2. Navigate to the project folder.
3. Run the following command:

```text
python main.py

## Input Validation 
 
The system handles: 
- Negative values 
- Invalid non-numeric input 
- Attended classes greater than total classes 
- Invalid target attendance percentages 
- Attendance percentages above 100% 
 
## Project Outcome 
 
The system provides a simple way for students to calculate, analyze, and manage their attendance using a modular Python program.
