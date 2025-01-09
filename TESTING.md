# Testing

This document outlines the testing strategy employed to ensure the quality and functionality of the Restaurant Ammersee website.  A combination of manual and automated testing was utilized to provide comprehensive coverage. Manual testing was conducted to thoroughly assess core functionality, user experience, and usability. Automated testing, specifically unit and integration tests, was implemented to increase efficiency and repeatability in verifying individual code units and their interactions.  Furthermore, code validation was performed using various validators to ensure adherence to web standards and best practices.

While the current testing strategy provides a solid foundation, future iterations will focus on expanding automated testing coverage to further enhance the robustness and reliability of the application.


## Code Validation

### HTML

* **W3C Markup Validation Service:** All HTML code was validated using the official W3C Markup Validation Service to ensure adherence to web standards and identify any potential issues.

<details>
<summary>Screenshots and results for all templates.</summary>
<br>

**HOME**

**MENU**

**REGISTER**
Some HTML validation errors are ignored due to the limitations of Django's template engine in generating perfectly valid HTML for forms. These errors do not affect the functionality or user experience of the website.

**LOG IN**

## Automated Tests

Automated tests were implemented using the Django testing framework. These tests focus on verifying the behavior of specific units of code and their integration within the application.

###  `MakeReservationViewTest`

This test suite focuses on the `make_reservation` view, which handles the creation of new reservations.

* **`test_make_reservation_valid_form`:** This test case verifies that a valid reservation form successfully creates a new reservation in the database and redirects the user to the confirmation page.
* **`test_make_reservation_invalid_form`:** This test case ensures that an invalid reservation form (e.g., with a past date) does not create a new reservation and returns an appropriate error response.


### `MyReservationsViewTest`

This test suite focuses on the `my_reservations` view, which displays a user's existing reservations.

* **`test_my_reservations_logged_in`:** This test case checks that the view correctly displays the user's reservations when they are logged in.
* **`test_my_reservations_not_logged_in`:** This test case verifies that the view redirects to the login page when the user is not logged in.

