import { useEffect, useState, useCallback } from "react";
import { fetchBooks, deleteBook } from "../api/bookApi";
import Table from "../components/Table";
import { useNavigate } from "react-router-dom";

export default function AdminDashboard() {
  const [books, setBooks] = useState([]);
  const navigate = useNavigate();

  const normalizeBook = (b) => ({
    id: b.id || b._id,
    title: b.title || "No Title",
    price: b.price ?? 0,
  });

  const loadBooks = useCallback(async () => {
    try {
      const res = await fetchBooks();

      console.log("BOOK API RESPONSE:", res); // 🔥 DEBUG THIS

      // 🧠 Handle ALL possible shapes safely
      let bookArray = [];

      if (Array.isArray(res)) {
        bookArray = res;
      } else if (Array.isArray(res?.books)) {
        bookArray = res.books;
      } else if (Array.isArray(res?.data)) {
        bookArray = res.data;
      } else {
        console.warn("Unexpected book response shape:", res);
        bookArray = [];
      }

      setBooks(bookArray.map(normalizeBook));
    } catch (err) {
      console.error("Fetch failed:", err);
      setBooks([]);
    }
  }, []);

  useEffect(() => {
    loadBooks();
  }, [loadBooks]);

  const handleDelete = async (id) => {
    try {
      await deleteBook(id);
      loadBooks();
    } catch (err) {
      console.error("Delete failed:", err.response?.data || err.message);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Admin Dashboard</h1>

      {/* CREATE BUTTON */}
      <button
        onClick={() => navigate("/admin/create")}
        className="mb-4 bg-green-600 text-white px-4 py-2 rounded"
      >
        Add Book
      </button>

      {/* EMPTY STATE */}
      {books.length === 0 ? (
        <p className="text-gray-500">No books found.</p>
      ) : (
        <Table
          columns={["ID", "Title", "Price", "Actions"]}
          data={books.map((b) => ({
            id: b.id,
            title: b.title,
            price: b.price,
            actions: (
              <div className="space-x-2">
                <button
                  onClick={() => navigate(`/admin/edit/${b.id}`)}
                  className="bg-blue-500 text-white px-2 py-1 rounded"
                >
                  Edit
                </button>

                <button
                  onClick={() => handleDelete(b.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded"
                >
                  Delete
                </button>
              </div>
            ),
          }))}
        />
      )}
    </div>
  );
}
