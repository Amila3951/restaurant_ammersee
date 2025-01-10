# Testing

This document outlines the testing strategy employed to ensure the quality and functionality of the Restaurant Ammersee website. A combination of manual and automated testing was utilized to provide comprehensive coverage. Manual testing was conducted to thoroughly assess core functionality, user experience, and usability. Automated testing, specifically unit and integration tests, was implemented to increase efficiency and repeatability in verifying individual code units and their interactions. Furthermore, code validation was performed using various validators to ensure adherence to web standards and best practices.

While the current testing strategy provides a solid foundation, future iterations will focus on expanding automated testing coverage to further enhance the robustness and reliability of the application.


## Table of Contents

* [Code Validation](#code-validation)
    * [HTML](#html)
    * [CSS](#css)
    * [Python](#python)
    * [JavaScript](#javascript)
* [Automated Tests](#automated-tests)
* [Manual Testing](#manual-testing)


## Code Validation

### HTML

**W3C Markup Validation Service:** All HTML code was validated using the official W3C Markup Validation Service to ensure adherence to web standards and identify any potential issues.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

* **Home**

![HtmlValidator](documentation/home-htmlpagevalidator.png)

* **Menu**

![HtmlValidator](documentation/menu-htmlpagevalidator.png)

* **Register**

   * Some HTML validation errors are ignored due to the limitations of Django's template engine in generating perfectly valid HTML for forms. These errors do not affect the functionality or user experience of the website.

![HtmlValidator](documentation/register-htmlpagevalidator.png)

* **Log In**

![HtmlValidator](documentation/login-htmlpagevalidator.png)

* **Make a Reservation**

![HtmlValidator](documentation/make_reservation-htmlpagevalidator.png)

* **My Reservations**

![HtmlValidator](documentation/my-reservations-htmlpagevalidator.png)

* **Edit Reservation**

![HtmlValidator](documentation/edit_reservation-htmlpagevalidator.png)

* **Delete Reservation**

![HtmlValidator](documentation/delete_reservation-htmlpagevalidator.png)

* **Admin Reservation**

![HtmlValidator](documentation/adminreservations-htmlpagevalidator.png)

* **Admin Add Reservation**

![HtmlValidator](documentation/admin_add_reservations-htmlpagevalidator.png)

* **Admin Edit Reservation**

![HtmlValidator](documentation/admin_edit_reservation-htmlpagevalidator.png)

* **Admin Delete Reservation**

![HtmlValidator](documentation/admin_delete_reservation-htmlpagevalidator.png)

</details>

[Back to top](#testing) <br>


### CSS

CSS code was tested using the **W3C CSS Validation Service** via text input.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

* **Style.css**

![CssValidator](documentation/style.css-validator.png)

* **Reservations.css**

![CssValidator](documentation/reservations.css-validator.png)

</details>

[Back to top](#testing) <br>

### Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>Screenshots and results for all python files</summary>

* settings.py

![CI Python Linter](documentation/settings.py.png)

* ammersee/urls.py

![CI Python Linter](documentation/ammersee_urls.py.png)

* wsgi.py

![CI Python Linter](documentation/wsgi.py.png)

* forms.py

![CI Python Linter](documentation/forms.py.png)

* models.py

![CI Python Linter](documentation/models.py.png)


* tests.py

![CI Python Linter](documentation/test.py.png)

* urls.py

![CI Python Linter](documentation/urls.py.png)

* views.py

![CI Python Linter](documentation/views.py.png)

</details>

[Back to top](#testing) <br>

### JavaScript

JavaScript code was tested using [JSHint](https://jshint.com/).

<details>
<summary>Screenshots and results for all JS files</summary>
<br>

* email.js

**JSHint Warning: "One undefined variable emailjs"**

This warning occurs because JSHint analyzes JavaScript code independently and doesn't recognize the emailjs variable loaded from HTML.

![JSHint](documentation/email.js.png)


* reservation.js

![JSHint](documentation/reservation.js.png)

</details>

[Back to top](#testing) <br>


## Automated Tests

Automated tests were implemented using the Django testing framework. These tests focus on verifying the behavior of specific units of code and their integration within the application.

<details>
<summary>Test Suites</summary>
<br>

###  `MakeReservationViewTest`

This test suite focuses on the `make_reservation` view, which handles the creation of new reservations.

* **`test_make_reservation_valid_form`:** This test case verifies that a valid reservation form successfully creates a new reservation in the database and redirects the user to the confirmation page.
* **`test_make_reservation_invalid_form`:** This test case ensures that an invalid reservation form (e.g., with a past date) does not create a new reservation and returns an appropriate error response.


### `MyReservationsViewTest`

This test suite focuses on the `my_reservations` view, which displays a user's existing reservations.

* **`test_my_reservations_logged_in`:** This test case checks that the view correctly displays the user's reservations when they are logged in.
* **`test_my_reservations_not_logged_in`:** This test case verifies that the view redirects to the login page when the user is not logged in.

</details>

[Back to top](#testing) <br>

## Manual Testing

**Objective:** To verify the functionality and user experience of the Restaurant Ammersee website and ensure it aligns with the specified requirements.

**Methodology:** A series of test cases were executed manually, covering key user interactions and functionalities across different sections of the website. Each test case involved specific actions and observations to determine if the actual outcome matched the expected behavior.

<details>
<summary>Test Cases and Results</summary>
<br>

**NAVBAR**

![Navbar](documentation/navbar-testing.png)

**BUTTONS (HOME PAGE)**

![Buttons (Home Page)](documentation/buttons_homepage-testing.png)

**SOCIAL MEDIA ICONS (FOOTER)**

![Social Media Icons (Footer)](documentation/social_media_icons-testing.png)

**CONTACT LINKS (FOOTER)**

![Contact Links (Footer)](documentation/contact_links-testing.png)

**BUTTONS (MENU PAGE)**

![Buttons (Menu Page)](documentation/buttons_menupage-testing.png)

**RESERVE A TABLE**

![Reserve a table](documentation/reserve_a_table-testing.png)

**MY RESERVATIONS**

![My Reservations](documentation/my_reservations-testing.png)

**REGISTER / SIGN UP**

![Register / Sign Up](documentation/register-testing.png)

**LOG OUT**

![Log out](documentation/logout-testing.png)

**ADMINISTRATION PANEL**

![Admin Panel](documentation/admin_panel-testing.png)

**EMAILJS**

![EmailJS](documentation/emailjs-testing.png)

</details>

[Back to top](#testing) <br>

[Back to README](README.md)