import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import BookCard from './BookCard';
import { CartProvider } from '../context/CartContext';

// Mock the useCart hook
jest.mock('../hooks/useCart', () => ({
  useCart: () => ({
    addToCart: jest.fn(),
  }),
}));

describe('BookCard Component', () => {
  const mockBook = {
    _id: '1',
    title: 'The Great Gatsby',
    author: 'F. Scott Fitzgerald',
    price: 12.99,
    stock: 50,
  };

  test('renders book title', () => {
    render(
      <CartProvider>
        <BookCard book={mockBook} />
      </CartProvider>
    );
    const titleElement = screen.getByText('The Great Gatsby');
    expect(titleElement).toBeInTheDocument();
  });

  test('renders book author', () => {
    render(
      <CartProvider>
        <BookCard book={mockBook} />
      </CartProvider>
    );
    const authorElement = screen.getByText('F. Scott Fitzgerald');
    expect(authorElement).toBeInTheDocument();
  });

  test('renders book price', () => {
    render(
      <CartProvider>
        <BookCard book={mockBook} />
      </CartProvider>
    );
    const priceElement = screen.getByText('₹12.99');
    expect(priceElement).toBeInTheDocument();
  });

  test('renders Add to Cart button', () => {
    render(
      <CartProvider>
        <BookCard book={mockBook} />
      </CartProvider>
    );
    const buttonElement = screen.getByRole('button', { name: 'Add to Cart' });
    expect(buttonElement).toBeInTheDocument();
  });
});
