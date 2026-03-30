import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";
import { fetchBookById } from "../api/bookApi";
import Loader from "../components/Loader";
import { useCart } from "../hooks/useCart";

export default function BookDetails() {
  const { id } = useParams();
  const { data, loading } = useFetch(() => fetchBookById(id));
  const { addToCart } = useCart();

  if (loading) return <Loader />;

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">{data.title}</h1>
      <p>{data.author}</p>
      <p className="text-green-600">₹{data.price}</p>
      <p className="mt-4">{data.description}</p>

      <button
        onClick={() => addToCart({ ...data, id: data._id })}
        className="mt-4 bg-blue-600 text-white px-3 py-1 rounded"
      >
        Add to Cart
      </button>
    </div>
  );
}
