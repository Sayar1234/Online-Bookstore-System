import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import CartItem from './CartItem';
import { CartProvider } from '../context/CartContext';

// Mock the useCart hook
jest.mock('../hooks/useCart', () => ({
  useCart: () => ({
    removeFromCart: jest.fn(),
  }),
}));

describe('CartItem Component', () => {
  const mockItem = {
    id: '1',
    title: 'The Great Gatsby',
    price: 12.99,
    quantity: 2,
  };

  test('renders item title', () => {
    render(
      <CartProvider>
        <CartItem item={mockItem} />
      </CartProvider>
    );
    const titleElement = screen.getByText('The Great Gatsby');
    expect(titleElement).toBeInTheDocument();
  });

  test('renders item price and quantity', () => {
    render(
      <CartProvider>
        <CartItem item={mockItem} />
      </CartProvider>
    );
    const priceAndQtyElement = screen.getByText('₹12.99 x 2');
    expect(priceAndQtyElement).toBeInTheDocument();
  });

  test('renders Remove button', () => {
    render(
      <CartProvider>
        <CartItem item={mockItem} />
      </CartProvider>
    );
    const removeButton = screen.getByRole('button', { name: 'Remove' });
    expect(removeButton).toBeInTheDocument();
  });
});
