// email.test.js
import { sendEmail } from './email.js';
import emailjs from 'emailjs-com';

// Mock emailjs-com
jest.mock('emailjs-com', () => ({
  send: jest.fn(() => Promise.resolve({ text: 'Success' }))
}));

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

  it('should call emailjs.send with correct arguments', async () => {
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

    await sendEmail(form, event);

    expect(emailjs.send).toHaveBeenCalledWith(
      'service_ab2vrqc',
      'template_oo7qvf5',
      {
        to_email: 'test@example.com',
        username: 'testuser'
      }
    );
  });

  it('should submit the form after successful email sending', async () => {
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

    await sendEmail(form, event);

    expect(form.submit).toHaveBeenCalled();
  });
});