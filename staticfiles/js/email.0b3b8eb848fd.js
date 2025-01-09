/*
 * Function to send an email using EmailJS.
 * 
 * @param {HTMLFormElement} form The form element containing the user's email and username.
 */
export function sendEmail(form) { 
    const email = form.elements['email'].value;  // Get the email address from the form
    const username = form.elements['username'].value;  // Get the username from the form

    const templateParams = {  // Create an object with the email and username for the email template
        to_email: email,
        username: username
    };

    // Check if EmailJS is loaded and initialized correctly
    if (typeof emailjs !== 'undefined' && typeof emailjs.send === 'function') {
        emailjs.send('service_ab2vrqc', 'template_oo7qvf5', templateParams)  // Send the email using EmailJS
            .then((result) => {
                console.log('Email sent successfully:', result.text);  // Log success message to the console

                const registrationMessage = document.getElementById('registration-message');  // Get the registration message element
                if (registrationMessage) {
                    registrationMessage.textContent = 'You have successfully registered!';  // Update the registration message
                }
            })
            .catch((error) => {
                console.error('Error sending email:', error);  // Log error message to the console
            });
    } else {
        console.error('EmailJS is not loaded or initialized properly.');  // Log error if EmailJS is not loaded
    }
}

/*
 * Function to check for a registration success message and send an email if found.
 */
export function checkRegistrationMessage() {
    const registrationMessage = document.getElementById('registration-message');  // Get the registration message element
    // Check if the message element exists and its content indicates successful registration
    if (registrationMessage && registrationMessage.textContent === 'registration_successful') {
        sendEmail(document.querySelector('.signup-form'));  // Send the email using the signup form data
    }
}

// Call checkRegistrationMessage when the window loads
window.onload = checkRegistrationMessage;