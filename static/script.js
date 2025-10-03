function login() {
    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
        })
    })
  .then(response => response.json())
  .then(data => {
    if (data.status == "ok"){
      localStorage.setItem("jwt", data.token)
      window.location.replace("/home");
    }
    else if (data.status == "error"){
      document.getElementById("loginError").innerText = data.msg;
    }
  })
  .catch(error => {
    console.log('Ошибка:', error);
  });
}

function protected() {
  token = localStorage.getItem("jwt")
  statusLabel = document.getElementById("statusLabel");
  fetch("/meme", {
    method: "GET",
    headers: {
      "Authorization": "Bearer " + token,
      "Content-type": "application/json"
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === "ok") {
      document.body.innerHTML = data.html;
    } else {
      statusLabel.textContent = data.msg;
    }
  })
  .catch(err => {
    console.error(err);
    statusLabel.textContent = "Ошибка соединения с сервером";
  });
}