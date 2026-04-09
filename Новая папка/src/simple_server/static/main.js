const button = document.getElementById('fetchButton');
const result = document.getElementById('result');

button.addEventListener('click', async () => {
  result.textContent = 'Loading...';

  try {
    const response = await fetch('/api/hello');
    const data = await response.json();
    result.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (error) {
    result.textContent = 'Request failed: ' + error.message;
  }
});