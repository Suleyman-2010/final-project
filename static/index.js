let userButtons = document.getElementsByClassName("user-button");
for (let user = 0; user < userButtons.length; user++) {
  userButtons[user].onclick = async () => {
    try {
      const response = await fetch(`/user/${user}`);
      const userData = await response.json();

      showUserInfo(userData);
    } catch (error) {
      console.error(error);
    }
  };
}

function showUserInfo(userData) {
  const newContactSection = document.querySelector("section:first-child");
  const ContactsSection = document.querySelector("section:nth-child(2)");
  const userInfoSection = document.querySelector("section:last-child");
  const userInfoArticle = document.querySelector(
    "section:last-child > article",
  );

  if (!userInfoSection.classList.contains("moved")) {
    newContactSection.classList.add("moved");
    ContactsSection.classList.add("moved");
    userInfoSection.style.display = "block";
    setTimeout(() => {
      userInfoSection.classList.add("moved");
    }, 10);
  }

  userInfoArticle.innerHTML = `
    <span>Name:</span>
    <p>${userData.name}</p>
    <span>Surname:</span>
    <p>${userData.surname}</p>
    <span>Email:</span>
    <p>${userData.email}</p>
    <span>Phone number:</span>
    <p>${userData.phone_number}</p>
  `;
}
