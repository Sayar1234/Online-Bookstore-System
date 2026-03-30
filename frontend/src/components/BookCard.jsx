import { useCart } from "../hooks/useCart";

export default function BookCard({ book }) {
  const { addToCart } = useCart();

  return (
    <div className="border p-4 rounded-xl shadow">
      <h2 className="font-bold">{book.title}</h2>
      <p>{book.author}</p>
      <p className="text-green-600">₹{book.price}</p>

      <button
        onClick={() => addToCart({ ...book, id: book._id })}
        className="mt-2 bg-blue-600 text-white px-3 py-1 rounded"
      >
        Add to Cart
      </button>
    </div>
  );
}
