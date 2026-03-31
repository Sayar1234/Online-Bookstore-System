import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { BrowserRouter } from 'react-router-dom';
import Navbar from './Navbar';

// Mock the useAuth hook
jest.mock('../hooks/useAuth', () => ({
  useAuth: () => ({
    token: 'fake-token',
    user: { role: 'customer' },
    logout: jest.fn(),
    loading: false,
  }),
}));

describe('Navbar Component', () => {
  test('renders BookStore logo', () => {
    render(
      <BrowserRouter>
        <Navbar onCartClick={jest.fn()} />
      </BrowserRouter>
    );
    const logoElement = screen.getByText('BookStore');
    expect(logoElement).toBeInTheDocument();
  });

  test('renders Books link when authenticated', () => {
    render(
      <BrowserRouter>
        <Navbar onCartClick={jest.fn()} />
      </BrowserRouter>
    );
    const booksLink = screen.getByText('Books');
    expect(booksLink).toBeInTheDocument();
  });

  test('renders Cart button when authenticated', () => {
    render(
      <BrowserRouter>
        <Navbar onCartClick={jest.fn()} />
      </BrowserRouter>
    );
    const cartButton = screen.getByRole('button', { name: 'Cart' });
    expect(cartButton).toBeInTheDocument();
  });

  test('renders Orders link when authenticated', () => {
    render(
      <BrowserRouter>
        <Navbar onCartClick={jest.fn()} />
      </BrowserRouter>
    );
    const ordersLink = screen.getByText('Orders');
    expect(ordersLink).toBeInTheDocument();
  });

  test('renders Logout button when authenticated', () => {
    render(
      <BrowserRouter>
        <Navbar onCartClick={jest.fn()} />
      </BrowserRouter>
    );
    const logoutButton = screen.getByRole('button', { name: 'Logout' });
    expect(logoutButton).toBeInTheDocument();
  });
});
