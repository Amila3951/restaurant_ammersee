import { sendEmail } from './email.js';

jest.mock('@emailjs/browser', () => ({
  send: jest.fn(() => Promise.resolve({ text: 'Success' }))
}));

const emailjs = require('@emailjs/browser');

describe('sendEmail', () => {
  it('should prevent default form submission', () => {
    const form = {
      elements: {
        email: { value: 'test@example.com' },
        username: { value: 'testuser' }
      },
      submit: jest.fn()
    };

    const event = {
      preventDefault: jest.fn()
    };

    sendEmail(form, event);

    expect(event.preventDefault).toHaveBeenCalled();
  });

  it('should call emailjs.send with correct arguments', () => {
    const form = {
      elements: {
        email: { value: 'test@example.com' },
        username: { value: 'testuser' }
      },
      submit: jest.fn()
    };

    const event = {
      preventDefault: jest.fn()
    };

    sendEmail(form, event);

    expect(emailjs.send).toHaveBeenCalledWith(
      'service_ab2vrqc',
      'template_oo7qvf5',
      {
        to_email: 'test@example.com',
        username: 'testuser'
      }
    );
  });

  it('should submit the form after successful email sending', () => {
    const form = {
      elements: {
        email: { value: 'test@example.com' },
        username: { value: 'testuser' }
      },
      submit: jest.fn()
    };

    const event = {
      preventDefault: jest.fn()
    };

    // Simulate a successful email sending
    emailjs.send.mockResolvedValueOnce({ text: 'Success' });

    sendEmail(form, event);

    expect(form.submit).toHaveBeenCalled();
  });
});