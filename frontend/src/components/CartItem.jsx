import { useCart } from "../hooks/useCart";

export default function CartItem({ item }) {
  const { removeFromCart } = useCart();

  const handleRemove = () => {
    removeFromCart(item.id);
  };

  return (
    <div className="flex justify-between border p-3 rounded mb-2">
      <div>
        <h3 className="font-bold">{item.title}</h3>
        <p>
          ₹{item.price} x {item.quantity}
        </p>
      </div>

      <button
        onClick={handleRemove}
        className="bg-red-500 text-white px-3 py-1 rounded"
      >
        Remove
      </button>
    </div>
  );
}
