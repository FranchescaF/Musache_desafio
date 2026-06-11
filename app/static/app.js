let currentSessionId = null;

async function askQuestion() {
    const inputElement = document.getElementById('question-input');
    const question = inputElement.value.trim();
    if (!question) return;

    // Mostrar pregunta
    appendMessage('user', question);
    inputElement.value = '';

    try {
        // Armar la URL, incluyendo el session_id si ya existe
        let url = '/ask';
        if (currentSessionId) {
            url += `?session_id=${currentSessionId}`;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();

        // Guardar el session_id retornado para futuras preguntas
        if (data.session_id) {
            currentSessionId = data.session_id;
        }

        // Mostrar respuesta
        appendMessage('assistant', data.answer);

    } catch (error) {
        console.error('Error:', error);
        appendMessage('assistant', 'Error de conexión con el servidor.');
    }
}

function appendMessage(role, text) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    msgDiv.className = role === 'user' ? 'user-msg' : 'ai-msg';
    msgDiv.innerHTML = `<strong>${role === 'user' ? 'Tú' : 'IA'}:</strong> ${text}`;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}