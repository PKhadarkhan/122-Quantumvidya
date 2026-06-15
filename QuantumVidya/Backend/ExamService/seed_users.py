import sqlite3
import json

def seed_users():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    try:
        cur.execute("ALTER TABLE students ADD COLUMN Department TEXT")
    except sqlite3.OperationalError:
        pass

    cur.execute("DELETE FROM students")

    departments = [
        'Computer', 'Electrical', 'ECE', 'Mechanical', 'Civil',
        'Aerospace', 'Chemical', 'Biomedical', 'Information Technology',
        'Metallurgical', 'Mechatronics', 'Instrumentation', 'Production',
        'Marine', 'Mining'
    ]

    students_data = [
        # Admins
        ('Admin 1', 'admin1@admin.com', 'admin', 'ADMIN', ''),
        ('Admin 2', 'admin2@admin.com', 'admin', 'ADMIN', ''),
        ('Admin 3', 'admin3@admin.com', 'admin', 'ADMIN', ''),
        ('Admin 4', 'admin4@admin.com', 'admin', 'ADMIN', ''),
        ('Admin 5', 'admin5@admin.com', 'admin', 'ADMIN', ''),
    ]

    for i, dept in enumerate(departments):
        students_data.append(
            (f'Student {i+1} ({dept})', f'student{i+1}@student.com', 'student', 'STUDENT', dept)
        )

    for data in students_data:
        cur.execute("INSERT INTO students (Name, Email, Password, Role, Department) VALUES (?, ?, ?, ?, ?)", data)
    
    conn.commit()

    cur.execute("SELECT ID, Name FROM students WHERE Role='STUDENT'")
    db_students = cur.fetchall()
    conn.close()

    results = []
    
    for i, st in enumerate(db_students):
        results.append({
            "Id": len(results) + 1,
            "Name": st[1],
            "TotalMark": 100,
            "TrustScore": 100.0,
            "Status": "Pass",
            "Date": "2026-06-14",
            "StId": st[0],
            "Link": f"Student_{st[0]:03d}Profile.jpg"
        })
        results.append({
            "Id": len(results) + 1,
            "Name": st[1],
            "TotalMark": 100,
            "TrustScore": 100.0,
            "Status": "Pass",
            "Date": "2026-06-15",
            "StId": st[0],
            "Link": f"Student_{st[0]:03d}Profile.jpg"
        })

    with open('result.json', 'w') as f:
        json.dump(results, f, indent=4)

    print("Users seeded with explicit Departments and results updated!")

if __name__ == '__main__':
    seed_users()
