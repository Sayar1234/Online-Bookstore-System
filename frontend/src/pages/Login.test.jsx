import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { BrowserRouter } from 'react-router-dom';
import Login from './Login';

// Mock useAuth hook
jest.mock('../hooks/useAuth', () => ({
  useAuth: () => ({
    login: jest.fn(),
    user: null,
    loading: false,
  }),
}));

// Mock loginUser API
jest.mock('../api/authApi', () => ({
  loginUser: jest.fn(),
}));

describe('Login Page', () => {
  test('renders Login heading', () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );
    const heading = screen.getByRole('heading', { name: 'Login' });
    expect(heading).toBeInTheDocument();
  });

  test('renders email input field', () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );
    const emailInput = screen.getByPlaceholderText('Email');
    expect(emailInput).toBeInTheDocument();
    expect(emailInput).toHaveAttribute('type', 'email');
  });

  test('renders password input field', () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );
    const passwordInput = screen.getByPlaceholderText('Password');
    expect(passwordInput).toBeInTheDocument();
    expect(passwordInput).toHaveAttribute('type', 'password');
  });

  test('renders Login button', () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );
    const loginButton = screen.getByRole('button', { name: /login/i });
    expect(loginButton).toBeInTheDocument();
  });

  test('renders Register link', () => {
    render(
      <BrowserRouter>
        <Login />
      </BrowserRouter>
    );
    const registerLink = screen.getByText('Register here');
    expect(registerLink).toBeInTheDocument();
  });
});
