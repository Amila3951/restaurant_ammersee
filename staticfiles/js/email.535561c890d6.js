export function sendEmail(form) {
  event.preventDefault(); 

  const email = form.elements['email'].value;
  const username = form.elements['username'].value;

  const templateParams = {
    to_email: email,
    username: username
  };

  emailjs.send('service_ab2vrqc', 'template_oo7qvf5', templateParams)
    .then((result) => {
      console.log(result.text);
     
      form.submit(); 
    }, (error) => {
      console.log(error.text);
      
    });
}