import { createOrder } from "../api/orderApi";
import { useNavigate } from "react-router-dom";
import { useCart } from "../hooks/useCart";
import CartItem from "../components/CartItem";

export default function Cart({ onClose }) {
  const { cart, clearCart } = useCart();
  const navigate = useNavigate();

  const handleCheckout = async () => {
    try {
      await createOrder({
        items: cart.map((item) => ({
          book_id: item.id,
          quantity: item.quantity,
        })),
      });

      clearCart();
      onClose();
      navigate("/orders");
    } catch (err) {
      console.error(err);
    }
  };

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div>
      <h1 className="text-xl font-bold mb-4">Cart</h1>

      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          {cart.map((item) => (
            <CartItem key={item.id} item={item} />
          ))}

          <p className="mt-4 font-bold">Total: ₹{total}</p>

          <button
            onClick={handleCheckout}
            className="mt-4 bg-green-600 text-white px-4 py-2 rounded"
          >
            Checkout
          </button>
        </>
      )}
    </div>
  );
}
