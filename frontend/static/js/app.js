fetch("http://127.0.0.1:5000/api/trends")
.then(res => res.json())
.then(data => {
    let container = document.getElementById("container");

    data.forEach(t => {
        let div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `
            <h3>${t.topic}</h3>
            <p>Growth: ${t.growth}</p>
            <p>Competition: ${t.competition}</p>
            <h4>Score: ${t.score}</h4>
        `;

        container.appendChild(div);
    });
});
