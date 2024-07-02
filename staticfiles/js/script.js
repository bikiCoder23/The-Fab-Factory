document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("submitbtn").onclick = (event) => {
    const name = document.getElementById("Name").value.trim();
    const phoneNumber = document.getElementById("PhoneNumber").value.trim();
    const email = document.getElementById("Email").value.trim();
    const country = document.getElementById("Country").value.trim();
    const feedback = document.getElementById("Feedback").value.trim();

    if (!name || !phoneNumber || !email || !country) {
      alert("* Indicates mandatory fields");
      event.preventDefault();
      return;
    }

    console.log(
      `Name: ${name}\nPhone Number: ${phoneNumber}\nEmail: ${email}\nCountry: ${country}\nFeedback: ${feedback}`
    );
    document.getElementById("success").innerHTML =
      "Thanks for connecting to The Fab Community❤️.";
  };
});
