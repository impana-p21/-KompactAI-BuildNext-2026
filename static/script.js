async function askQuestion() {
    const question = document.getElementById("question").value.trim();
    const button = document.getElementById("askButton");
    const results = document.getElementById("results");
    const status = document.getElementById("status");
    const answer = document.getElementById("answer");
    const sources = document.getElementById("sources");

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    button.disabled = true;
    button.textContent = "Searching...";
    results.hidden = false;
    status.textContent = "Retrieving evidence...";
    answer.textContent = "";
    sources.replaceChildren();

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Request failed.");
        }

        status.textContent = "Status: " + data.status;
        answer.textContent = data.answer;

        data.sources.forEach((item) => {
            const card = document.createElement("article");
            card.className = "source";

            const heading = document.createElement("h3");
            heading.textContent = item.topic;

            const content = document.createElement("p");
            content.textContent = item.content;

            const reference = document.createElement("p");
            reference.textContent = "Source: " + item.source;

            const link = document.createElement("a");
            link.href = item.url;
            link.textContent = "View source";
            link.target = "_blank";
            link.rel = "noopener noreferrer";

            card.append(heading, content, reference, link);
            sources.appendChild(card);
        });

    } catch (error) {
        status.textContent = "Unable to retrieve evidence.";
        answer.textContent = error.message;
    } finally {
        button.disabled = false;
        button.textContent = "Find Evidence";
    }
}
