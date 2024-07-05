const scriptURL = "https://api.telegram.org/bot" + process.env.TOKEN + "/sendMessage";
const form = document.forms['submit-to-google-sheet'];
const submitButton = form.querySelector('button[type="submit"]');
const msg = document.getElementById("span")

form.addEventListener('submit', e => {
  e.preventDefault();

  const submitButton = form.querySelector('button[type="submit"]');
  submitButton.disabled = true; // Disable the submit button
  var formData = new FormData(form);
  var time = new Date()
  console.log(time)
  formData.append('timestamp', time) // add timestamp to form data

  // Build the Telegram message
  const message = `
    New form submission:
    Name: ${formData.get('name')}
    Email: ${formData.get('email')}
    Message: ${formData.get('message')}
    Timestamp: ${time}
  `;

  // Send the message to the Telegram bot
  fetch(scriptURL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      chat_id: process.env.CHAT_ID,
      text: message
    })
  })
  .then(response => {
    msg.innerHTML = "Message has been sent!";
    setTimeout(function(){
      msg.innerHTML = "";
    }, 5000);
    form.reset();
  })
  .catch(error => console.error('Error!', error.message))
  .finally(() => {
    submitButton.disabled = false; // Re-enable the submit button
  });
});