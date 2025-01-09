export function sendEmail(form) { 
    const email = form.elements['email'].value;
    const username = form.elements['username'].value;

    const templateParams = {
        to_email: email,
        username: username
    };

    if (typeof emailjs !== 'undefined' && typeof emailjs.send === 'function') {
        emailjs.send('service_ab2vrqc', 'template_oo7qvf5', templateParams)
            .then((result) => {
                console.log('Email sent successfully:', result.text);

                const registrationMessage = document.getElementById('registration-message');
                if (registrationMessage) {
                    registrationMessage.textContent = 'You have successfully registered!';
                }

            })
            .catch((error) => {
                console.error('Error sending email:', error);
            });
    } else {
        console.error('EmailJS is not loaded or initialized properly.');
    }
}

export function checkRegistrationMessage() {
    const registrationMessage = document.getElementById('registration-message');
    if (registrationMessage && registrationMessage.textContent === 'registration_successful') {
        sendEmail(document.querySelector('.signup-form'));
    }
}

window.onload = checkRegistrationMessage;