import re

# Remove from login.html
login_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\login.html'
with open(login_path, 'r') as f:
    login_content = f.read()

# The department div in login.html starts with <div class="input-div pass" style="margin-top: 20px;">
# and ends with </div>\n                </div> right before <br>
pattern_login = r'<div class="input-div pass" style="margin-top: 20px;">\s*<div class="i">\s*<i class="fas fa-building"></i>\s*</div>\s*<div class="div">\s*<select name="department".*?</select>\s*</div>\s*</div>'

extracted_dropdown = re.search(pattern_login, login_content, flags=re.DOTALL)
if extracted_dropdown:
    dropdown_html = extracted_dropdown.group(0)
    # Remove from login
    new_login_content = login_content.replace(dropdown_html, '')
    with open(login_path, 'w') as f:
        f.write(new_login_content)
    
    # Add to signup.html
    signup_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\signup.html'
    with open(signup_path, 'r') as f:
        signup_content = f.read()
    
    # Insert it after the role dropdown
    # The role dropdown is also <div class="input-div pass" style="margin-top: 20px;">
    # Let's insert it right before the <br> tag in signup.html
    # Or replace <option value="" disabled selected>Department (Students Only)</option> with just Department
    dropdown_html = dropdown_html.replace('Department (Students Only)', 'Department (Students Only)')
    
    # But wait, in signup, role has margin-top 20px. We can just add another one.
    if 'name="department"' not in signup_content:
        new_signup_content = signup_content.replace('<br>', dropdown_html + '\n\t\t\t\t<br>')
        
        # Add a simple JS to toggle the department dropdown based on role
        # It's optional, but it's cleaner if it only shows when STUDENT is selected.
        js = """
        <script>
            document.querySelector('select[name="role"]').addEventListener('change', function() {
                const deptDiv = document.querySelector('select[name="department"]').closest('.input-div');
                if(this.value === 'STUDENT') {
                    deptDiv.style.display = 'flex';
                    document.querySelector('select[name="department"]').required = true;
                } else {
                    deptDiv.style.display = 'none';
                    document.querySelector('select[name="department"]').required = false;
                    document.querySelector('select[name="department"]').value = '';
                }
            });
            // trigger on load
            document.querySelector('select[name="role"]').dispatchEvent(new Event('change'));
        </script>
        """
        new_signup_content = new_signup_content.replace('</body>', js + '\n</body>')
        with open(signup_path, 'w') as f:
            f.write(new_signup_content)
        
    print("UI templates updated successfully!")
else:
    print("Could not find department dropdown in login.html")
