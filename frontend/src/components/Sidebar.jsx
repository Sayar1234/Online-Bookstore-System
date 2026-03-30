import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-64 bg-gray-800 text-white h-screen p-4">
      <h2 className="text-xl font-bold mb-4">Dashboard</h2>

      <div className="flex flex-col gap-3">
        <Link to="/books">Books</Link>
        <Link to="/orders">Orders</Link>
        <Link to="/admin">Admin</Link>
      </div>
    </div>
  );
}
