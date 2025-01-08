import emailjs from 'https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js';

export function sendEmail(form, event) {
    event.preventDefault();

    const email = form.elements['email'].value;
    const username = form.elements['username'].value;

    const templateParams = {
        to_email: email,
        username: username
    };

    emailjs.send('service_ab2vrqc', 'template_oo7qvf5', templateParams)
        .then((result) => {
            console.log('Email sent successfully:', result.text);
            form.submit();
        }, (error) => {
            console.log('Error sending email:', error.text);
        });
}