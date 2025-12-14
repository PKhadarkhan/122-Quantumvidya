const BASE_URL = "http://127.0.0.1:8000";

function getInputs() {
  return {
    course: document.getElementById("subject")?.value,
    subject: document.getElementById("topic")?.value,
    output: document.getElementById("output")
  };
}

// ---------- POST helper ----------
async function post(endpoint, body, output, loading) {
  output.textContent = loading;

  try {
    const res = await fetch(BASE_URL + endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    const data = await res.json();
    return data;

  } catch (e) {
    output.textContent = "⚠ Backend not reachable";
    return null;
  }
}

// ---------- Notes ----------
async function generateNotes() {
  const { course, subject, output } = getInputs();
  if (!subject) return output.textContent = "Enter topic";

  const data = await post("/notes", { course, topic: subject }, output, "📘 Generating notes...");
  if (data?.notes) output.textContent = data.notes;
}

// ---------- Exam ----------
async function generateExam() {
  const { course, subject, output } = getInputs();
  if (!subject) return output.textContent = "Enter topic";

  // You may want to add a level selector in your HTML and pass it here
  const data = await post("/exam", { course, subject, level: "easy" }, output, "📝 Generating exam...");
  if (data) output.textContent = JSON.stringify(data, null, 2);
}

// ---------- PYQ ----------
async function generatePYQs() {
  const { course, subject, output } = getInputs();
  if (!subject) return output.textContent = "Enter topic";

  const data = await post("/pyq", { course, subject }, output, "📄 Loading PYQs...");
  if (data?.questions) output.textContent = data.questions;
}

// ---------- Textbook ----------
async function askTextbook() {
  const { course, subject, output } = getInputs();
  if (!course || !subject) return output.textContent = "Enter course and subject";
  output.textContent = "📚 Searching textbook...";
  try {
    const res = await fetch(
      `${BASE_URL}/textbook?course=${encodeURIComponent(course)}&subject=${encodeURIComponent(subject)}`
    );
    const data = await res.json();
    if (data.textbook) output.textContent = data.textbook;
    else if (data.error) output.textContent = data.error;
    else output.textContent = "No textbook found.";
  } catch {
    output.textContent = "⚠ Backend error";
  }
}

// ---------- AI Doubt Solver ----------
async function askAI() {
  const { subject, output } = getInputs();
  if (!subject) return output.textContent = "Ask a question";

  const data = await post("/ask", { question: subject }, output, "🤖 Thinking...");
  if (data?.answer) output.textContent = data.answer;
}

// Export functions for use in HTML
window.generateNotes = generateNotes;
window.generateExam = generateExam;
window.generatePYQs = generatePYQs;
window.askTextbook = askTextbook;
window.askAI = askAI;
