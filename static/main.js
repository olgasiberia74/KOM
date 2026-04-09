async function loadQuestions() {
  const response = await fetch('/api/questions');
  if (!response.ok) {
    showMessage('Ошибка при загрузке вопросов.', true);
    return;
  }

  const questions = await response.json();
  const form = document.getElementById('survey-form');
  form.innerHTML = '';

  questions.forEach((question) => {
    const label = document.createElement('label');
    label.textContent = question.text;
    label.htmlFor = `question-${question.id}`;

    const input = document.createElement('textarea');
    input.id = `question-${question.id}`;
    input.name = `question-${question.id}`;
    input.rows = 2;
    input.required = true;

    form.appendChild(label);
    form.appendChild(input);
  });
}

function showMessage(text, isError = false) {
  const message = document.getElementById('message');
  message.textContent = text;
  message.style.color = isError ? '#b00020' : '#1a7f37';
}

async function submitAnswers() {
  const form = document.getElementById('survey-form');
  const answers = [];

  Array.from(form.querySelectorAll('textarea')).forEach((input) => {
    const questionId = Number(input.id.replace('question-', ''));
    answers.push({ question_id: questionId, text: input.value.trim() });
  });

  const response = await fetch('/api/answers', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ answers }),
  });

  if (!response.ok) {
    showMessage('Ошибка при отправке ответов.', true);
    return;
  }

  showMessage('Спасибо! Ваши ответы отправлены.');
  form.reset();
}

document.getElementById('submit-button').addEventListener('click', submitAnswers);
loadQuestions();
