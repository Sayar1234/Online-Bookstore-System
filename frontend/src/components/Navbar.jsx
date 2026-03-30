import { Link } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

export default function Navbar({ onCartClick }) {
  const { token, logout, user, loading } = useAuth();

  if (loading) return null;

  return (
    <nav className="flex justify-between items-center p-4 bg-gray-900 text-white">
      <Link to={token ? "/books" : "/login"} className="text-xl font-bold">
        BookStore
      </Link>

      <div className="flex gap-4 items-center">
        {token && (
          <>
            <Link to="/books">Books</Link>
            <button onClick={onCartClick} className="hover:underline">
              Cart
            </button>
            <Link to="/orders">Orders</Link>
            {user?.role === "admin" && <Link to="/admin">Admin Dashboard</Link>}
            <button onClick={logout} className="hover:underline">
              Logout
            </button>
          </>
        )}

        {!token && (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}
