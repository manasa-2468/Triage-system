document.getElementById('triageForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const symptoms = document.getElementById('symptoms').value;

    const response = await fetch('/check_condition', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ symptoms })
    });

    const data = await response.json();
    document.getElementById('result').textContent = data.result;
});