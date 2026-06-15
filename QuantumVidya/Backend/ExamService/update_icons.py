import os
import re

files = [
    r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\login.html',
    r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\admin_login.html',
    r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\signup.html'
]

replacements = {
    '<script src="https://kit.fontawesome.com/a81368914c.js"></script>': '<script src="https://unpkg.com/@phosphor-icons/web"></script>',
    '<i class="fas fa-user"></i>': '<i class="ph-duotone ph-user" style="font-size: 1.5rem;"></i>',
    '<i class="fas fa-lock"></i>': '<i class="ph-duotone ph-lock-key" style="font-size: 1.5rem;"></i>',
    '<i class="fas fa-id-card"></i>': '<i class="ph-duotone ph-identification-card" style="font-size: 1.5rem;"></i>',
    '<i class="fas fa-users-cog"></i>': '<i class="ph-duotone ph-users-three" style="font-size: 1.5rem;"></i>',
    '<i class="fas fa-building"></i>': '<i class="ph-duotone ph-buildings" style="font-size: 1.5rem;"></i>'
}

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        # In signup.html, the email icon is fa-user, but we want ph-envelope
        # The script above replaces fa-user with ph-user. Let's fix that specifically for signup.html
        if 'signup.html' in file_path:
            # We know the second input in signup is email.
            # But the HTML currently says <h5>Email Address</h5> after the icon.
            # We can use regex to target the icon near "Email Address"
            content = re.sub(r'<i class="ph-duotone ph-user" style="font-size: 1\.5rem;"></i>(?=\s*</div>\s*<div class="div">\s*<h5>Email Address</h5>)', 
                             '<i class="ph-duotone ph-envelope" style="font-size: 1.5rem;"></i>', content)

        with open(file_path, 'w') as f:
            f.write(content)
            
print("Icons updated successfully!")
