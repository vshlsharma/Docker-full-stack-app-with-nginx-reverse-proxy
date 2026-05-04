function getData() {
    fetch('/api')
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").innerText =
                "Message: " + data.message + " | Host: " + data.hostname;
        })
        .catch(error => {
            console.error("Error:", error);
        });
}

