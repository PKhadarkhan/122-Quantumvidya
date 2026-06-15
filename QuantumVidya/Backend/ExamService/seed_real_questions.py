import sqlite3
import json

def seed():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM questions")
    cur.execute("DELETE FROM subjects")

    # Real questions for each department
    real_data = {
        'Computer': {
            'Data Structures': [
                {'q': 'What is the time complexity of binary search?', 'options': ['O(n)', 'O(n log n)', 'O(log n)', 'O(1)'], 'ans': 'O(log n)'},
                {'q': 'Which data structure uses LIFO principle?', 'options': ['Queue', 'Stack', 'Tree', 'Graph'], 'ans': 'Stack'},
                {'q': 'What is the worst-case time complexity of QuickSort?', 'options': ['O(n log n)', 'O(n^2)', 'O(n)', 'O(log n)'], 'ans': 'O(n^2)'},
                {'q': 'Which traversal of a BST gives elements in sorted order?', 'options': ['Pre-order', 'In-order', 'Post-order', 'Level-order'], 'ans': 'In-order'},
                {'q': 'What data structure is used for Breadth First Search?', 'options': ['Stack', 'Queue', 'Priority Queue', 'Linked List'], 'ans': 'Queue'}
            ]
        },
        'Electrical': {
            'Circuit Theory': [
                {'q': 'What is Ohms Law?', 'options': ['V = I/R', 'V = I*R', 'P = V*I', 'I = V*R'], 'ans': 'V = I*R'},
                {'q': 'What is the unit of capacitance?', 'options': ['Henry', 'Ohm', 'Farad', 'Tesla'], 'ans': 'Farad'},
                {'q': 'In a purely inductive circuit, the current:', 'options': ['Leads voltage by 90 degrees', 'Lags voltage by 90 degrees', 'Is in phase with voltage', 'Lags voltage by 45 degrees'], 'ans': 'Lags voltage by 90 degrees'},
                {'q': 'Kirchhoffs Current Law is based on the conservation of:', 'options': ['Energy', 'Momentum', 'Charge', 'Mass'], 'ans': 'Charge'},
                {'q': 'The superposition theorem is applicable to:', 'options': ['Linear circuits only', 'Non-linear circuits only', 'Both linear and non-linear', 'None of the above'], 'ans': 'Linear circuits only'}
            ]
        },
        'ECE': {
            'Digital Electronics': [
                {'q': 'Which logic gate is known as the universal gate?', 'options': ['AND', 'OR', 'NAND', 'XOR'], 'ans': 'NAND'},
                {'q': 'How many bits make a byte?', 'options': ['4', '8', '16', '32'], 'ans': '8'},
                {'q': 'A multiplexer has:', 'options': ['One input, many outputs', 'Many inputs, many outputs', 'Many inputs, one output', 'One input, one output'], 'ans': 'Many inputs, one output'},
                {'q': 'De Morgans theorem states that (A.B)\' is equal to:', 'options': ['A\'.B\'', 'A\' + B\'', 'A + B', 'A.B'], 'ans': 'A\' + B\''},
                {'q': 'A flip-flop stores:', 'options': ['1 bit of data', '2 bits of data', '4 bits of data', '8 bits of data'], 'ans': '1 bit of data'}
            ]
        },
        'Mechanical': {
            'Thermodynamics': [
                {'q': 'What is the first law of thermodynamics?', 'options': ['Conservation of Mass', 'Conservation of Energy', 'Entropy always increases', 'Absolute zero is unreachable'], 'ans': 'Conservation of Energy'},
                {'q': 'In an isothermal process, what remains constant?', 'options': ['Pressure', 'Volume', 'Temperature', 'Heat'], 'ans': 'Temperature'},
                {'q': 'Which cycle is the most efficient heat engine cycle?', 'options': ['Otto cycle', 'Diesel cycle', 'Carnot cycle', 'Rankine cycle'], 'ans': 'Carnot cycle'},
                {'q': 'What is the unit of pressure in SI units?', 'options': ['Pascal', 'Bar', 'Atmosphere', 'Torr'], 'ans': 'Pascal'},
                {'q': 'An adiabatic process is one in which:', 'options': ['Volume is constant', 'Pressure is constant', 'No heat is transferred', 'Temperature is constant'], 'ans': 'No heat is transferred'}
            ]
        },
        'Civil': {
            'Structural Analysis': [
                {'q': 'What is the bending moment at a simply supported end of a beam?', 'options': ['Maximum', 'Minimum', 'Zero', 'Depends on load'], 'ans': 'Zero'},
                {'q': 'Hookes law states that within elastic limit:', 'options': ['Stress is inversely proportional to strain', 'Stress is directly proportional to strain', 'Strain is constant', 'Stress is zero'], 'ans': 'Stress is directly proportional to strain'},
                {'q': 'Poisson\'s ratio is the ratio of:', 'options': ['Lateral strain to linear strain', 'Linear strain to lateral strain', 'Shear stress to shear strain', 'Volumetric strain to linear strain'], 'ans': 'Lateral strain to linear strain'},
                {'q': 'A cantilever beam has:', 'options': ['Both ends fixed', 'Both ends hinged', 'One end fixed, one end free', 'One end hinged, one end free'], 'ans': 'One end fixed, one end free'},
                {'q': 'The point of contraflexure is where:', 'options': ['Shear force is zero', 'Bending moment changes sign', 'Deflection is maximum', 'Slope is zero'], 'ans': 'Bending moment changes sign'}
            ]
        },
        'Aerospace': {
            'Aerodynamics': [
                {'q': 'Which principle explains the generation of lift on an airfoil?', 'options': ['Archimedes Principle', 'Bernoullis Principle', 'Pascals Law', 'Newtons First Law'], 'ans': 'Bernoullis Principle'},
                {'q': 'What is the speed of sound at sea level under standard conditions?', 'options': ['~343 m/s', '~300 m/s', '~150 m/s', '~1000 m/s'], 'ans': '~343 m/s'},
                {'q': 'Drag caused by the generation of lift is called:', 'options': ['Parasite drag', 'Profile drag', 'Induced drag', 'Wave drag'], 'ans': 'Induced drag'},
                {'q': 'The Mach number is the ratio of:', 'options': ['Velocity to speed of light', 'Velocity to speed of sound', 'Density to pressure', 'Lift to drag'], 'ans': 'Velocity to speed of sound'},
                {'q': 'An aircraft controls pitch using:', 'options': ['Ailerons', 'Rudder', 'Elevators', 'Flaps'], 'ans': 'Elevators'}
            ]
        },
        'Chemical': {
            'Chemical Kinetics': [
                {'q': 'The rate of a chemical reaction generally:', 'options': ['Increases with temperature', 'Decreases with temperature', 'Is independent of temperature', 'Fluctuates randomly'], 'ans': 'Increases with temperature'},
                {'q': 'What is a catalyst?', 'options': ['A substance that slows down a reaction', 'A substance that speeds up a reaction without being consumed', 'A product of a reaction', 'A reactant that is fully consumed'], 'ans': 'A substance that speeds up a reaction without being consumed'},
                {'q': 'The half-life of a first-order reaction is:', 'options': ['Dependent on initial concentration', 'Independent of initial concentration', 'Proportional to square of concentration', 'Zero'], 'ans': 'Independent of initial concentration'},
                {'q': 'Activation energy is:', 'options': ['Energy released during a reaction', 'Minimum energy required to start a reaction', 'Energy of the products', 'Energy of the reactants'], 'ans': 'Minimum energy required to start a reaction'},
                {'q': 'Le Chatelier\'s principle applies to systems in:', 'options': ['Dynamic equilibrium', 'Static equilibrium', 'Non-equilibrium', 'Vapor phase only'], 'ans': 'Dynamic equilibrium'}
            ]
        },
        'Biomedical': {
            'Biomechanics': [
                {'q': 'Which tissue connects muscle to bone?', 'options': ['Ligament', 'Tendon', 'Cartilage', 'Fascia'], 'ans': 'Tendon'},
                {'q': 'Wolffs Law states that bone will:', 'options': ['Degrade over time', 'Grow in response to the stresses placed upon it', 'Always be brittle', 'Not heal after a fracture'], 'ans': 'Grow in response to the stresses placed upon it'},
                {'q': 'What is the primary function of an ECG?', 'options': ['Measure brain activity', 'Measure muscle tension', 'Record electrical activity of the heart', 'Measure blood oxygen'], 'ans': 'Record electrical activity of the heart'},
                {'q': 'Which imaging modality uses magnetic fields?', 'options': ['X-Ray', 'CT Scan', 'Ultrasound', 'MRI'], 'ans': 'MRI'},
                {'q': 'Youngs modulus is a measure of a materials:', 'options': ['Hardness', 'Toughness', 'Stiffness', 'Ductility'], 'ans': 'Stiffness'}
            ]
        },
        'Information Technology': {
            'Web Technologies': [
                {'q': 'What does HTML stand for?', 'options': ['Hyper Text Markup Language', 'High Tech Modern Language', 'Hyperlink and Text Markup Language', 'Home Tool Markup Language'], 'ans': 'Hyper Text Markup Language'},
                {'q': 'Which HTTP method is idempotent?', 'options': ['POST', 'PUT', 'PATCH', 'None of these'], 'ans': 'PUT'},
                {'q': 'What does CSS stand for?', 'options': ['Creative Style Sheets', 'Computer Style Sheets', 'Cascading Style Sheets', 'Colorful Style Sheets'], 'ans': 'Cascading Style Sheets'},
                {'q': 'Which status code indicates "Not Found"?', 'options': ['200', '403', '404', '500'], 'ans': '404'},
                {'q': 'JavaScript is primarily a:', 'options': ['Server-side language', 'Client-side language', 'Database query language', 'Markup language'], 'ans': 'Client-side language'}
            ]
        },
        'Metallurgical': {
            'Material Science': [
                {'q': 'Steel is an alloy of iron and:', 'options': ['Carbon', 'Zinc', 'Copper', 'Aluminum'], 'ans': 'Carbon'},
                {'q': 'Which heat treatment process relieves internal stresses?', 'options': ['Quenching', 'Tempering', 'Annealing', 'Nitriding'], 'ans': 'Annealing'},
                {'q': 'Brass is an alloy of:', 'options': ['Copper and Tin', 'Copper and Zinc', 'Iron and Carbon', 'Aluminum and Magnesium'], 'ans': 'Copper and Zinc'},
                {'q': 'What is the hardest known natural substance?', 'options': ['Gold', 'Iron', 'Diamond', 'Quartz'], 'ans': 'Diamond'},
                {'q': 'Galvanization involves coating iron with:', 'options': ['Tin', 'Zinc', 'Copper', 'Silver'], 'ans': 'Zinc'}
            ]
        },
        'Mechatronics': {
            'Robotics': [
                {'q': 'Which sensor is typically used to measure distance?', 'options': ['Thermocouple', 'Ultrasonic sensor', 'Strain gauge', 'Photodiode'], 'ans': 'Ultrasonic sensor'},
                {'q': 'A servomotor allows for precise control of:', 'options': ['Temperature', 'Angular position', 'Light intensity', 'Pressure'], 'ans': 'Angular position'},
                {'q': 'PLC stands for:', 'options': ['Programmable Logic Controller', 'Process Level Control', 'Primary Logic Circuit', 'Programmable Linear Circuit'], 'ans': 'Programmable Logic Controller'},
                {'q': 'Degrees of freedom (DOF) refers to:', 'options': ['Number of sensors', 'Number of independent movements', 'Battery life', 'Processing power'], 'ans': 'Number of independent movements'},
                {'q': 'An actuator converts energy into:', 'options': ['Data', 'Electrical signals', 'Mechanical motion', 'Heat'], 'ans': 'Mechanical motion'}
            ]
        },
        'Instrumentation': {
            'Control Systems': [
                {'q': 'In a closed-loop control system, the feedback signal is compared to the:', 'options': ['Output signal', 'Reference input', 'Error signal', 'Disturbance'], 'ans': 'Reference input'},
                {'q': 'A PID controller consists of:', 'options': ['Proportional, Integral, Derivative', 'Primary, Inverse, Direct', 'Pulse, Impulse, Delay', 'Positive, Inverse, Differential'], 'ans': 'Proportional, Integral, Derivative'},
                {'q': 'Which system is more stable?', 'options': ['Open-loop', 'Closed-loop', 'Both are equally stable', 'Depends on the plant'], 'ans': 'Closed-loop'},
                {'q': 'A thermocouple measures:', 'options': ['Pressure', 'Flow', 'Temperature', 'Level'], 'ans': 'Temperature'},
                {'q': 'A strain gauge relies on the change of which property?', 'options': ['Capacitance', 'Inductance', 'Resistance', 'Voltage'], 'ans': 'Resistance'}
            ]
        },
        'Production': {
            'Manufacturing': [
                {'q': 'Which process involves removing material to form a shape?', 'options': ['Casting', 'Machining', 'Forging', 'Welding'], 'ans': 'Machining'},
                {'q': 'In CNC machining, CNC stands for:', 'options': ['Computer Numeric Control', 'Central Network Computer', 'Control Number Code', 'Computer Node Control'], 'ans': 'Computer Numeric Control'},
                {'q': 'Injection molding is primarily used for:', 'options': ['Metals', 'Ceramics', 'Plastics', 'Wood'], 'ans': 'Plastics'},
                {'q': 'Just-in-Time (JIT) manufacturing aims to reduce:', 'options': ['Quality', 'Inventory', 'Production speed', 'Worker safety'], 'ans': 'Inventory'},
                {'q': 'Which welding process uses a non-consumable tungsten electrode?', 'options': ['MIG', 'TIG', 'Stick', 'Submerged Arc'], 'ans': 'TIG'}
            ]
        },
        'Marine': {
            'Naval Architecture': [
                {'q': 'The center of buoyancy is located at the:', 'options': ['Center of gravity of the ship', 'Centroid of the displaced volume of fluid', 'Metacenter', 'Keel'], 'ans': 'Centroid of the displaced volume of fluid'},
                {'q': 'What does draft refer to in a ship?', 'options': ['The height of the mast', 'The vertical distance from the waterline to the bottom of the hull', 'The width of the ship', 'The speed of the ship'], 'ans': 'The vertical distance from the waterline to the bottom of the hull'},
                {'q': 'A ship is stable if its metacenter is:', 'options': ['Below the center of gravity', 'Above the center of gravity', 'At the center of gravity', 'At the keel'], 'ans': 'Above the center of gravity'},
                {'q': 'Cavitation in propellers causes:', 'options': ['Increased efficiency', 'Decreased noise', 'Pitting and erosion of blades', 'Better steering'], 'ans': 'Pitting and erosion of blades'},
                {'q': 'The Plimsoll line on a ship indicates:', 'options': ['Maximum safe draft', 'Minimum speed', 'Fuel capacity', 'Center of gravity'], 'ans': 'Maximum safe draft'}
            ]
        },
        'Mining': {
            'Mining Engineering': [
                {'q': 'Open-pit mining is an example of:', 'options': ['Underground mining', 'Surface mining', 'Placer mining', 'In-situ mining'], 'ans': 'Surface mining'},
                {'q': 'Which explosive is commonly used in mining operations?', 'options': ['TNT', 'ANFO', 'Dynamite', 'C4'], 'ans': 'ANFO'},
                {'q': 'Ventilation in underground mines is crucial to:', 'options': ['Provide lighting', 'Remove hazardous gases and provide oxygen', 'Cool down machinery only', 'Transport ore'], 'ans': 'Remove hazardous gases and provide oxygen'},
                {'q': 'What is the purpose of a headframe?', 'options': ['To crush ore', 'To support the hoist mechanism for underground access', 'To store explosives', 'To pump water'], 'ans': 'To support the hoist mechanism for underground access'},
                {'q': 'Tailings are:', 'options': ['High-grade ore', 'The valuable minerals extracted', 'The waste materials left after extracting the valuable minerals', 'Mining equipment parts'], 'ans': 'The waste materials left after extracting the valuable minerals'}
            ]
        }
    }

    for dept, subjects in real_data.items():
        for sub_name, questions in subjects.items():
            cur.execute("INSERT INTO subjects (Name, Timer, Department) VALUES (?, ?, ?)", (sub_name, 600, dept))
            sub_id = cur.lastrowid
            
            for q in questions:
                # Scramble choices so answer isn't always in the same place? 
                # Actually, options array already has them.
                c1, c2, c3, c4 = q['options']
                ans = q['ans']
                cur.execute('''INSERT INTO questions 
                               (Subject_ID, Title, Choice1, Choice2, Choice3, Choice4, Answer) 
                               VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                            (sub_id, q['q'], c1, c2, c3, c4, ans))

    conn.commit()
    conn.close()
    print("Database seeded with REAL questions for all 15 departments successfully!")

if __name__ == '__main__':
    seed()
