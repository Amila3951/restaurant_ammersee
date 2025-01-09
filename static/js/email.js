import emailjs from 'emailjs-com';
export function sendEmail(form, event) {
    event.preventDefault();

    const email = form.elements['email'].value;
    const username = form.elements['username'].value;

    const templateParams = {
        to_email: email,
        username: username
    };

    try {
       
        if (typeof emailjs.send === 'function') {
            emailjs.send('service_ab2vrqc', 'template_oo7qvf5', templateParams)
                .then((result) => {
                    console.log('Email sent successfully:', result.text);
                    form.submit();
                })
                .catch((error) => {
                    console.error('Error sending email:', error);
                });
        } else {
            console.error('emailjs.send is not a function');
        }

    } catch (error) {
        console.error('Unexpected error:', error);
    }
}