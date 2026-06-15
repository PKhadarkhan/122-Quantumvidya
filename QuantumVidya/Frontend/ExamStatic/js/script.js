var startButton = document.querySelector("#startQuiz");
var timer = document.querySelector("#timer");
var mainContent = document.querySelector("#mainContent");
var questionEl = document.querySelector("#title");
var quizContent = document.querySelector("#quizContent");
var navControls = document.querySelector("#navControls");
var submitContainer = document.querySelector("#submitContainer");
var prevBtn = document.querySelector("#prevBtn");
var nextBtn = document.querySelector("#nextBtn");
var bookmarkBtn = document.querySelector("#bookmarkBtn");
var submitExamBtn = document.querySelector("#submitExamBtn");

var questions = [];
var userAnswers = {};
var bookmarks = {};
var secondsLeft = 300;
var questionIndex = 0;
var timeInterval;

function init() {
    $.ajax({
        type: "GET",
        url: "/api/getExamData",
        success: function(response) {
            questions = response.questions;
            secondsLeft = response.timer;
            // Now start the monitoring
            $.ajax({
                type: "POST",
                url: "/exam",
                contentType: "application/json",
                data: JSON.stringify({input:''}),
                success: function(res) {
                    startQuiz();
                }
            });
        },
        error: function(err) {
            alert("Error loading exam data. Have you selected a subject?");
            console.error(err);
        }
    });
}

$(document).ready(function() {
    startButton.addEventListener("click", function() {
        init();
    });
});

function startQuiz() {
    mainContent.style.display = "none";
    quizContent.style.display = "block";
    navControls.style.display = "block";
    submitContainer.style.display = "block";
    startTimer();
    buildQuestion();
}

function startTimer() {
    timer.textContent = "Time : " + secondsLeft + " sec";
    timeInterval = setInterval(function() {
        secondsLeft--;
        timer.textContent = "Time : " + secondsLeft + " sec";
        if(secondsLeft <= 0) {
            clearInterval(timeInterval);
            timer.textContent = "Time's up!";
            submitExam();
        }
    }, 1000);
}

function buildQuestion() {
    if (questions.length === 0) {
        questionEl.innerHTML = "No questions available for this subject.";
        return;
    }
    
    quizContent.innerHTML = "";
    var q = questions[questionIndex];
    
    questionEl.innerHTML = "Q" + (questionIndex + 1) + ": " + q.title;
    questionEl.setAttribute("class","text-left mb-4");
    questionEl.style.display= "block";
    
    var bookmarked = bookmarks[questionIndex] || false;
    if (bookmarked) {
        questionEl.innerHTML = "🔖 " + questionEl.innerHTML;
        bookmarkBtn.checked = true;
    } else {
        bookmarkBtn.checked = false;
    }
    
    for(var i = 0; i < 4; i++) {
        var choiceText = q.choices[i];
        var btn = document.createElement("button");
        btn.setAttribute("class", "btn mb-2 d-block w-100 text-left");
        
        if (userAnswers[questionIndex] === choiceText) {
            btn.setAttribute("style", "background: #205c5e; color: white; border-radius: 20px; padding: 10px; font-weight: bold;");
        } else {
            btn.setAttribute("style", "background: #5f9ea0; color: white; border-radius: 20px; padding: 10px;");
        }
        
        btn.textContent = (i + 1) + ". " + choiceText;
        btn.onclick = (function(text) {
            return function() {
                userAnswers[questionIndex] = text;
                buildQuestion();
            }
        })(choiceText);
        
        quizContent.appendChild(btn);
    }
    
    prevBtn.disabled = questionIndex === 0;
    nextBtn.disabled = questionIndex === questions.length - 1;
}

prevBtn.addEventListener("click", function() {
    if(questionIndex > 0) {
        questionIndex--;
        buildQuestion();
    }
});

nextBtn.addEventListener("click", function() {
    if(questionIndex < questions.length - 1) {
        questionIndex++;
        buildQuestion();
    }
});

bookmarkBtn.addEventListener("change", function() {
    bookmarks[questionIndex] = this.checked;
    buildQuestion(); // Re-render to show/hide bookmark icon in title
});

submitExamBtn.addEventListener("click", function() {
    if(confirm("Are you sure you want to submit the exam?")) {
        clearInterval(timeInterval);
        submitExam();
    }
});

function submitExam() {
    quizContent.style.display = "none";
    navControls.style.display = "none";
    submitContainer.style.display = "none";
    
    var correct = 0;
    for(var i = 0; i < questions.length; i++) {
        var uAns = userAnswers[i] ? userAnswers[i].trim().toLowerCase() : "";
        var cAns = questions[i].answer ? questions[i].answer.trim().toLowerCase() : "";
        if(uAns !== "" && uAns === cAns) {
            correct++;
        }
    }
    
    var totalMark = questions.length > 0 ? Math.round((correct / questions.length) * 100) : 0;
    
    questionEl.innerHTML = "Submitting your score...";
    
    $.ajax({
        type: "POST",
        url: "/exam",
        contentType: "application/json",
        data: JSON.stringify({input: totalMark}),
        success: function(response) {
            window.location.href = "/" + response['link'] + "/" + response['output'];
        },
        error: function(xhr, status, error) {
            questionEl.innerHTML = "Error submitting test.";
        }
    });
}
