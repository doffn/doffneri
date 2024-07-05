const scriptURL = "https://script.google.com/macros/s/AKfycbwBlTKlXuTe4qP8q0cqdpd3jVmGVK9icDgZ-9NcghgasVh-gbiCLXmZgydMGH-WHMyfow/exec";
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
  fetch(scriptURL, { method: 'POST', body: formData })
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

event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);

        fetch('{% url "contact" %}', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                form.reset();
                document.getElementById('span').textContent = 'Form submitted successfully!';
            } else {
                document.getElementById('span').textContent = 'Error submitting form.';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('span').textContent = 'Error submitting form.';
        });