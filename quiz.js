let currentQuestion = 0;
const timeLeftDuration = 60;  // Timer duration in seconds
let timeLeft = timeLeftDuration;
let timerInterval;
let totalQuestions = 0;  // Ensure this is set correctly when initializing quiz data

function displayQuestion() {
    const questionData = quizData.questions[currentQuestion];
    const questionContainer = document.getElementById('question-container');
    const optionContainer = document.getElementById('option-container');

    questionContainer.innerHTML = `${currentQuestion + 1}. ${questionData.content}`;
    
    const optionsHtml = questionData.options
        .map(option => `
            <div class="form-check">
                <input class="form-check-input" type="checkbox" value="${option}" id="${option}">
                <label class="form-check-label" for="${option}">${option}</label>
            </div>
        `).join('');  // Use map to generate options and join them into a string
    
    optionContainer.innerHTML = optionsHtml;
}

function nextQuestion() {
    if (currentQuestion < totalQuestions - 1) {
        currentQuestion++;
        displayQuestion();
    } else {
        displayResult();
    }
}

function prevQuestion() {
    if (currentQuestion > 0) {
        currentQuestion--;
        displayQuestion();
    }
}

function submitQuiz() {
    clearInterval(timerInterval);
    displayResult();
}

function displayResult() {
    // Placeholder for result calculation and display logic
    alert('Quiz submitted!');
}

function updateTimer() {
    const timerElement = document.getElementById('time-left');
    timerElement.innerText = timeLeft;

    if (timeLeft <= 0) {
        clearInterval(timerInterval);
        displayResult();
    } else {
        timeLeft--;
    }
}
