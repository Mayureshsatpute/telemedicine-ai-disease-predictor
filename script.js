document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    const response = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
  
    const result = await response.json();
  
    const messageDiv = document.getElementById("login-message");
    if (response.ok) {
      messageDiv.innerText = result.message;
      messageDiv.style.color = "green";
    } else {
      messageDiv.innerText = result.error;
      messageDiv.style.color = "red";
    }
  });
  document.getElementById("registerForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const email = document.getElementById("reg-email").value;
    const password = document.getElementById("reg-password").value;
  
    const response = await fetch("http://localhost:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
  
    const result = await response.json();
    const msg = document.getElementById("register-message");
    msg.innerText = result.message || result.error;
    msg.style.color = response.ok ? "green" : "red";
  });
    