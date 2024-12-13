import emailjs from '@emailjs/browser';

emailjs.init("YJtEjZpi5gTulnaLfS");
emailjs.send("service_ab2vrqc", "template_oo7qvf5", templateParams)

  .then(function (response) {

    console.log("Welcome email sent successfully!", response.status, response.text);
  }, function (error) {
    console.log("There was an error sending the email:", error);
   });