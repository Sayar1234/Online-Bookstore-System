import { useEffect, useState } from "react";
import { fetchBookById, updateBook } from "../api/bookApi";
import { useNavigate, useParams } from "react-router-dom";

export default function EditBook() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [form, setForm] = useState({
    title: "",
    author: "",
    price: "",
    stock: "",
  });

  useEffect(() => {
    const loadBook = async () => {
      try {
        const res = await fetchBookById(id);
        const data = res.data || res; // handle axios

        setForm({
          title: data.title || "",
          author: data.author || "",
          price: data.price || "",
          stock: data.stock ?? "",
        });
      } catch (err) {
        console.error(err);
      }
    };

    loadBook();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await updateBook(id, {
        title: form.title,
        author: form.author,
        price: Number(form.price),
        stock: Number(form.stock) || 0,
      });

      navigate("/admin");
    } catch (err) {
      console.error("Update failed:", err.response?.data || err.message);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Edit Book</h1>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          placeholder="Title"
          value={form.title}
          onChange={(e) => setForm({ ...form, title: e.target.value })}
          className="border p-2 w-full"
        />

        <input
          placeholder="Author"
          value={form.author}
          onChange={(e) => setForm({ ...form, author: e.target.value })}
          className="border p-2 w-full"
        />

        <input
          placeholder="Price"
          type="number"
          value={form.price}
          onChange={(e) => setForm({ ...form, price: e.target.value })}
          className="border p-2 w-full"
        />

        <input
          placeholder="Stock"
          type="number"
          value={form.stock}
          onChange={(e) => setForm({ ...form, stock: e.target.value })}
          className="border p-2 w-full"
        />

        <button className="bg-blue-600 text-white px-4 py-2 rounded">
          Update
        </button>
      </form>
    </div>
  );
}
