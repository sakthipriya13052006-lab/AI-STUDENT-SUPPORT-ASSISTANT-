"""
CampusAssist - AI Student Support Assistant
Naan Mudhalvan - IBM Agentic AI Project - Phase 5
Agentic AI with Tool-Use (Claude Style)
"""

# ========== 1. KNOWLEDGE BASE (Mock College Data) ==========

REGULATIONS = [
    {"id": "R01", "title": "Attendance Policy", "content": "Minimum 75% attendance required per course to appear for exams. 65-75% can get condonation with medical certificate via HOD."},
    {"id": "R02", "title": "Exam Policy", "content": "Students must have hall ticket and ID card. Malpractice leads to debar."},
    {"id": "R03", "title": "Grading System", "content": "CGPA calculated. Pass mark is 50% in both internal and external."},
]

SYLLABUS = [
    {"code": "CS101", "subject": "Python Programming", "units": "Unit1: Basics, Unit2: OOP, Unit3: Files, Unit4: Libraries", "credits": 4},
    {"code": "CS102", "subject": "Data Structures", "units": "Unit1: Arrays, Unit2: LinkedList, Unit3: Stacks, Queue", "credits": 4},
]

FAQS = [
    {"question": "How to get bonafide certificate?", "answer": "Apply in student portal -> Certificate section -> Bonafide -> 2 working days."},
    {"question": "Fee due date?", "answer": "Semester fee due is 10th of every sem start month. Late fee Rs.100
