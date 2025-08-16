const tutors = {
  "Alfred": "secret1",
  "Dietmar": "secret2"
};

document.getElementById("login-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const role = document.getElementById("role").value;
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  let status = "Logged in as " + role;

  if(role === "tutor") {
    if(tutors[user] && tutors[user] === pass) {
      status = "✅ Tutor login successful: " + user;
      // Optional: unlock enhanced actions for tutor
    } else {
      status = "❌ Invalid tutor credentials";
    }
  }

  document.getElementById("login-status").innerText = status;
});
