import re

# 1. Update Exam.html to fix the startQuiz button
exam_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\templates\Exam.html'
with open(exam_path, 'r', encoding='utf-8') as f:
    exam_content = f.read()

# Replace the startQuiz button
exam_content = re.sub(
    r'<button type="submit" id="startQuiz" class="btn text-white rounded-pill mb-2 mt-2"\s*>',
    '<button type="submit" id="startQuiz" class="btn text-white rounded-pill mb-2 mt-2" style="background: linear-gradient(90deg, #8b5cf6, #2dd4bf); border: none; padding: 10px 30px; font-weight: 600;">',
    exam_content
)

# Replace the nextBtn and prevBtn to match the gradient theme
exam_content = re.sub(
    r'<button id="nextBtn" class="btn btn-primary rounded-pill" style="[^"]*">',
    '<button id="nextBtn" class="btn text-white rounded-pill" style="background: linear-gradient(90deg, #8b5cf6, #2dd4bf); border: none; padding: 8px 25px; font-weight: 600;">',
    exam_content
)

with open(exam_path, 'w', encoding='utf-8') as f:
    f.write(exam_content)

# 2. Overhaul quiz.css to dark mode
quiz_css_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\static\css\quiz.css'
new_quiz_css = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

body{
    background: #0f172a;
    font-family: 'Outfit', sans-serif;
    color: #f8fafc;
}
header{
    background: #020617;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
header nav{
    position : fixed;
    overflow : hidden;
    width: 100%;
}
header nav span{
    font-size: 17px;
    font-weight : 600;
    color: #f8fafc;
    margin-left: 30px;
}
.card{
    border-radius: 20px;
    background: #1e293b;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}
.card-body{
    background: transparent;
    border-radius: 1em;
    color: #f8fafc;
}
.card-title {
    color: #2dd4bf !important;
    font-weight: 700;
}
hr.line {
    border-top: 1px solid rgba(255,255,255,0.1);
}
footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    text-align: center;
    padding-top: 12px;
    margin: auto;
    font-size: 14px;
    font-weight: 400;
    background-color: #020617;
    color: #94a3b8;
    border-top: 1px solid rgba(255,255,255,0.05);
}

/* Style the question text and options */
#quizContent h4 {
    color: #f8fafc;
    margin-bottom: 20px;
}
.form-check-label {
    color: #94a3b8;
    font-size: 1.1rem;
    cursor: pointer;
}
.form-check {
    margin-bottom: 10px;
    padding: 10px 30px;
    border-radius: 8px;
    transition: 0.3s;
    border: 1px solid transparent;
}
.form-check:hover {
    background: rgba(255,255,255,0.03);
    border-color: rgba(45, 212, 191, 0.2);
}
"""

with open(quiz_css_path, 'w', encoding='utf-8') as f:
    f.write(new_quiz_css)

print("Exam page and quiz CSS updated successfully!")
