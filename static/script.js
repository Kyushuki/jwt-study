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
  fetch("/meme", {
    method: "GET",
    headers: {
      "Authorization": "Bearer " + token,
      "Content-type": "application/json"
    }
  })
  .then(response => {
    if (!response.ok){
      throw new Error("Ошибка доступа: " + response.status)
    }
    return response.json();
  })
  .then(data => {
    document.body.innerHTML = data.html;
  })
}