const form = document.getElementById("chatForm");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const question = document.getElementById("question").value;

    const response = await fetch("/ask", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            question
        })

    });

    const data = await response.json();

    const chat = document.getElementById("chat");

    chat.innerHTML += `
        <div class="mt-3">
            <strong>Tú:</strong><br>
            ${question}
        </div>

        <div class="mt-2 mb-4">
            <strong>IA:</strong><br>
            ${data.answer}
        </div>
    `;

    document.getElementById("question").value = "";

    chat.scrollTop = chat.scrollHeight;

});