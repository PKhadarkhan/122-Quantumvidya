import os
import re

departments = [
    'Computer', 'Electrical', 'ECE', 'Mechanical', 'Civil',
    'Aerospace', 'Chemical', 'Biomedical', 'Information Technology',
    'Metallurgical', 'Mechatronics', 'Instrumentation', 'Production',
    'Marine', 'Mining'
]

# Update login.html
login_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\login.html'
with open(login_path, 'r') as f:
    login_content = f.read()

new_options = '<option value="" disabled selected>Department (Students Only)</option>\n'
for d in departments:
    new_options += f'                            <option value="{d}">{d}</option>\n'

login_content = re.sub(r'<select name="department"[^>]*>.*?</select>', 
                       f'<select name="department" class="input" style="outline:none; border:none; background:transparent; font-family:\'Poppins\', sans-serif; color:#555;" required>\n{new_options}                        </select>', 
                       login_content, flags=re.DOTALL)

with open(login_path, 'w') as f:
    f.write(login_content)

# Update Subjects.html
subj_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\Subjects.html'
with open(subj_path, 'r') as f:
    subj_content = f.read()

# Replace the first select (Edit modal)
edit_options = ''
for d in departments:
    edit_options += f'                                                <option value="{d}" {{% if row.3 == \'{d}\' %}}selected{{% endif %}}>{d}</option>\n'

# Find the first select
pattern1 = r'<select class="form-control" name="department" required>\s*<option value="Computer" {% if row\.3 == \'Computer\' %}selected{% endif %}>Computer</option>.*?</select>'
subj_content = re.sub(pattern1, f'<select class="form-control" name="department" required>\n{edit_options}                                              </select>', subj_content, flags=re.DOTALL)

# Replace the second select (Add modal)
add_options = ''
for d in departments:
    add_options += f'                        <option value="{d}">{d}</option>\n'

pattern2 = r'<select class="form-control" name="department" required>\s*<option value="Computer">Computer</option>.*?</select>'
subj_content = re.sub(pattern2, f'<select class="form-control" name="department" required>\n{add_options}                      </select>', subj_content, flags=re.DOTALL)

with open(subj_path, 'w') as f:
    f.write(subj_content)

print("Updated HTML files.")
