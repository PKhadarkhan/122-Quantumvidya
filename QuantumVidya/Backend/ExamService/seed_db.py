import sqlite3
import random

def seed():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    try:
        cur.execute("ALTER TABLE subjects ADD COLUMN Department TEXT NOT NULL DEFAULT 'Computer'")
    except sqlite3.OperationalError:
        pass

    departments = ['Computer', 'Mechanical', 'Electrical', 'ECE', 'Civil']
    
    # 20 Generic realistic sounding subjects per department
    dept_subject_templates = {
        'Computer': ['Data Structures', 'Algorithms', 'Operating Systems', 'Database Management', 'Computer Networks', 'Software Engineering', 'Artificial Intelligence', 'Machine Learning', 'Computer Vision', 'Cryptography', 'Cloud Computing', 'Distributed Systems', 'Web Development', 'Mobile Computing', 'Cyber Security', 'Compiler Design', 'Computer Architecture', 'Human Computer Interaction', 'Data Mining', 'Big Data Analytics'],
        'Mechanical': ['Thermodynamics', 'Fluid Mechanics', 'Heat Transfer', 'Solid Mechanics', 'Manufacturing Processes', 'Machine Design', 'Kinematics', 'Dynamics of Machinery', 'Control Systems', 'Robotics', 'Automobile Engineering', 'Power Plant Engineering', 'Refrigeration', 'Mechatronics', 'CAD/CAM', 'Material Science', 'Industrial Engineering', 'Finite Element Analysis', 'Aerodynamics', 'Renewable Energy'],
        'Electrical': ['Circuit Theory', 'Electromagnetic Fields', 'Power Systems', 'Control Systems', 'Electrical Machines', 'Power Electronics', 'Signals and Systems', 'Microprocessors', 'Digital Signal Processing', 'High Voltage Engineering', 'Renewable Energy Systems', 'Smart Grid', 'Electric Drives', 'Switchgear and Protection', 'Electrical Measurements', 'Network Analysis', 'Linear Integrated Circuits', 'Embedded Systems', 'Industrial Automation', 'Electric Vehicles'],
        'ECE': ['Digital Electronics', 'Analog Circuits', 'Signals and Systems', 'Communication Systems', 'Microprocessors', 'VLSI Design', 'Digital Signal Processing', 'Antennas and Wave Propagation', 'Microwave Engineering', 'Optical Communication', 'Embedded Systems', 'Wireless Communication', 'Information Theory', 'Control Systems', 'Network Theory', 'Electronics Devices', 'Satellite Communication', 'Radar Systems', 'Telecommunication Networks', 'Biomedical Instrumentation'],
        'Civil': ['Structural Analysis', 'Fluid Mechanics', 'Surveying', 'Geotechnical Engineering', 'Transportation Engineering', 'Environmental Engineering', 'Construction Management', 'Concrete Technology', 'Steel Structures', 'Hydraulics', 'Water Resources', 'Highway Engineering', 'Railway Engineering', 'Bridge Engineering', 'Town Planning', 'Earthquake Engineering', 'Estimation and Costing', 'Solid Waste Management', 'Irrigation Engineering', 'Pavement Design']
    }

    # Clean existing data to avoid duplicates piling up infinitely
    cur.execute("DELETE FROM questions")
    cur.execute("DELETE FROM subjects")

    for dept in departments:
        subjects = dept_subject_templates[dept]
        for idx, sub_name in enumerate(subjects):
            cur.execute("INSERT INTO subjects (Name, Timer, Department) VALUES (?, ?, ?)", (sub_name, 600, dept))
            sub_id = cur.lastrowid
            
            # Generate 10 questions for this subject
            for q_idx in range(1, 11):
                title = f"Which of the following is a key concept in {sub_name} (Question {q_idx})?"
                c1 = f"Concept A for {sub_name}"
                c2 = f"Concept B for {sub_name}"
                c3 = f"Concept C for {sub_name}"
                c4 = f"Concept D for {sub_name}"
                
                # Pick a random answer
                choices = [c1, c2, c3, c4]
                answer = random.choice(choices)
                
                cur.execute('''INSERT INTO questions 
                               (Subject_ID, Title, Choice1, Choice2, Choice3, Choice4, Answer) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                            (sub_id, title, c1, c2, c3, c4, answer))

    conn.commit()
    conn.close()
    print("Database seeded with 20 subjects per department and 10 questions per subject successfully!")

if __name__ == '__main__':
    seed()
