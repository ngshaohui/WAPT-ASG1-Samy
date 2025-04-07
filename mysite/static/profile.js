function addFriend() {
  fetch("/friend", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ friend: "{{username}}" }),
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
      alert("Added {{username}} as a friend");
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
    },
    body: JSON.stringify(jsonObject),
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

document.getElementById("update-btn").addEventListener("click", editContent);
