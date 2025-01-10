/* jshint esversion: 6 */

/*
 * Function to send an email using EmailJS.
 *
 * @param {HTMLFormElement} form The form element 
 * containing the user's email and username.
 */
export function sendEmail(form) {
    const email = form.elements.email.value;
    const username = form.elements.username.value;

    const templateParams = {
        to_email: email,
        username: username,
    };

    if (
        typeof emailjs !== "undefined" &&
        typeof emailjs.send === "function"
    ) {
        emailjs.send(
            "service_ab2vrqc",
            "template_oo7qvf5",
            templateParams
        )
            .then((result) => {
                console.log(
                    "Email sent successfully:",
                    result.text
                );

                const registrationMessage = document.getElementById(
                    "registration-message"
                );
                if (registrationMessage) {
                    registrationMessage.textContent =
                        "You have successfully registered!";
                }
            })
            .catch((error) => {
                console.error("Error sending email:", error);
            });
    } else {
        console.error(
            "EmailJS is not loaded or initialized properly."
        );
    }
}

/*
 * Function to check for a registration success 
 * message and send an email if found.
 */
export function checkRegistrationMessage() {
    const registrationMessage = document.getElementById(
        "registration-message"
    );
    if (
        registrationMessage &&
        registrationMessage.textContent ===
            "registration_successful"
    ) {
        sendEmail(document.querySelector(".signup-form"));
    }
}

// Call checkRegistrationMessage when the window loads
window.onload = checkRegistrationMessage;