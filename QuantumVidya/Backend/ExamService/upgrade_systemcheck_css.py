import os

css_path = r'd:\project\122-Quantumvidya\AI-Proctor-Exam-Monitor\static\css\SystemCheck.css'

new_css = """@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Outfit', sans-serif;
}

body {
    min-height: 100vh;
    background: #0f172a;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #f8fafc;
}
nav {
   display: flex;
   position: fixed;
   top:0;
   width: 100%;
   background-color: #020617;
   border-bottom: 1px solid rgba(255,255,255,0.05);
   overflow: auto;
   height: 60px;
   justify-content: space-between;
   align-items: center;
   z-index: 1000;
}
.left-links{
   flex:1 1 200px;
   display: flex;
   align-items: center;
}
.left-links .P-title
{
    font-size: 17px;
    font-weight: 600;
    margin-left: 30px;
    color: #f8fafc;
}
.links {
   display: inline-block;
   text-align: center;
   padding: 14px;
   color: #94a3b8;
   text-decoration: none;
   font-size: 16px;
   font-weight: 600;
   transition: 0.3s;
}
.links:hover {
    color: #2dd4bf;
}

main.table {
    width: 82vw;
    height: 60vh;
    background-color: #1e293b;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: .8rem;
    overflow: hidden;
}

.table__header {
    width: 100%;
    height: 20%;
    background-color: rgba(0,0,0,0.2);
    padding: .8rem 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.table__header h1 {
    color: #2dd4bf;
    font-weight: 700;
}

.table__body {
    width: 95%;
    max-height: calc(89% - 1.6rem);
    background-color: transparent;
    margin: 1.5rem auto;
    border-radius: .6rem;
    overflow: auto;
    overflow: overlay;
}

table {
    width: 100%;
}

table, th, td {
    border-collapse: collapse;
    padding: 1rem;
    text-align: left;
}
table th,td{
    width: 50%;
}

thead th {
    position: sticky;
    top: 0;
    left: 0;
    background-color: rgba(0,0,0,0.3);
    cursor: pointer;
    text-transform: capitalize;
    color: #94a3b8;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

tbody tr {
    --delay: .1s;
    transition: .3s ease-in-out;
    border-bottom: 1px solid rgba(255,255,255,0.02);
}

tbody tr:hover {
    background-color: rgba(255,255,255,0.02) !important;
}

@media (max-width: 1000px) {
    td:not(:first-of-type) {
        min-width: 12.1rem;
    }
}

thead th span.icon-arrow {
    display: inline-block;
    width: 1.3rem;
    height: 1.3rem;
    border-radius: 50%;
    border: 1.4px solid transparent;
    text-align: center;
    font-size: 1rem;
    margin-left: .5rem;
    transition: .2s ease-in-out;
}

thead th:hover span.icon-arrow{
    border: 1.4px solid #ddd;
}

thead th:hover {
    color: #f8fafc;
}

.export__file {
    position: relative;
}

.export__file .export__file-btn {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    background: rgba(255,255,255,0.1) url("/static/img/check.png") center / 80% no-repeat;
    border-radius: 50%;
    transition: .2s ease-in-out;
}

.export__file .export__file-btn:hover { 
    background-color: #2dd4bf;
    transform: scale(1.15);
    cursor: pointer;
}

.export__file input {
    display: none;
}


.section-button{
    margin: auto;
    text-align: center;
    margin-top: 10px;
}

.next {
  background: linear-gradient(90deg, #8b5cf6, #2dd4bf);
  color: white;
  border-radius: 50px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  transition: 0.3s;
}
.nextButton a {
  text-decoration: none;
  display: inline-block;
  padding: 10px 30px;
  font-size: 18px;
  font-weight: 600;
}

.nextButton a:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(45, 212, 191, 0.4);
  color: white;
}
footer {
    background-color: #020617;
    text-align: center;
    padding: 10px 0;
    position: absolute;
    bottom: 0;
    width: 100%;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.container8 {
    max-width: 100%;
    max-height: 100%;
    display: grid;    
    grid-template-columns: 1fr;
    justify-items: center;
    font-size: 14px;
    font-weight: 400;
    text-decoration: none;     
}

.box-footer1 {
    font-size: 14px;
    color: #94a3b8;
    font-weight: 400;
    padding: 5px;
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_css)

print("SystemCheck.css updated to premium dark mode!")
