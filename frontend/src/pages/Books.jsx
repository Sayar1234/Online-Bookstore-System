import useFetch from "../hooks/useFetch";
import { fetchBooks } from "../api/bookApi";
import Loader from "../components/Loader";
import BookCard from "../components/BookCard";

export default function Books() {
  const { data, loading } = useFetch(fetchBooks);

  if (loading) return <Loader />;

  return (
    <div className="grid grid-cols-4 gap-4 p-6">
      {data.map((b) => (
        <BookCard key={b.id} book={b} />
      ))}
    </div>
  );
}
