function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

function addFriend() {
  const formData = new FormData(document.getElementById("addFriendForm"));
  fetch("/friend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ friend: formData.get("friend") }),
  })
    .then((response) => {
      if (!response.ok) {
        return response.text().then((text) => {
          throw new Error(text);
        });
      }
      return response.json();
    })
    .then((data) => {
      alert(`Added ${formData.get("friend")} as a friend`);
      location.reload();
    })
    .catch((error) => {
      console.error("Error:", error);
      alert(error);
    });
}

function editContent() {
  const formData = new FormData(document.getElementById("contentUpdateForm"));
  const jsonObject = {};
  formData.forEach((value, key) => {
    jsonObject[key] = value;
  });

  fetch("/profile/update", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ content: formData.get("content") }),
  })
    .then((response) => {
      if (!response.ok) {
        return response.text().then((text) => {
          throw new Error(text);
        });
      }
      return response.json();
    })
    .then((data) => {
      alert("Updated content");
      location.reload();
    })
    .catch((error) => {
      console.error("Error:", error);
      alert(error);
    });
}

if (document.getElementById("update-btn") !== null) {
  document.getElementById("update-btn").addEventListener("click", editContent);
}

if (document.getElementById("friend-btn") !== null) {
  document.getElementById("friend-btn").addEventListener("click", addFriend);
}
