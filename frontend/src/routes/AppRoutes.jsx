import { Routes, Route, Navigate } from "react-router-dom";
import Books from "../pages/Books";
import Login from "../pages/Login";
import Cart from "../pages/Cart";
import ProtectedRoute from "../components/ProtectedRoute";
import Orders from "../pages/Orders";
import Register from "../pages/Register";
import BookDetails from "../pages/BookDetails";
import AdminDashboard from "../pages/AdminDashboard";
import CreateBook from "../pages/CreateBook"; // ✅ ADD THIS
import EditBook from "../pages/EditBook"; // ✅ ADD THIS
import { useAuth } from "../hooks/useAuth";

export default function AppRoutes() {
  const { token } = useAuth();

  return (
    <Routes>
      <Route
        path="/"
        element={token ? <Navigate to="/books" /> : <Navigate to="/login" />}
      />

      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      <Route
        path="/books"
        element={
          <ProtectedRoute>
            <Books />
          </ProtectedRoute>
        }
      />

      <Route
        path="/books/:id"
        element={
          <ProtectedRoute>
            <BookDetails />
          </ProtectedRoute>
        }
      />

      <Route
        path="/orders"
        element={
          <ProtectedRoute>
            <Orders />
          </ProtectedRoute>
        }
      />

      {/* ✅ ADMIN DASHBOARD */}
      <Route
        path="/admin"
        element={
          <ProtectedRoute role="admin">
            <AdminDashboard />
          </ProtectedRoute>
        }
      />

      {/* 🔥 ADD THESE TWO ROUTES */}
      <Route
        path="/admin/create"
        element={
          <ProtectedRoute role="admin">
            <CreateBook />
          </ProtectedRoute>
        }
      />

      <Route
        path="/admin/edit/:id"
        element={
          <ProtectedRoute role="admin">
            <EditBook />
          </ProtectedRoute>
        }
      />

      <Route
        path="/cart"
        element={
          <ProtectedRoute role="user">
            <Cart />
          </ProtectedRoute>
        }
      />

      {/* ⚠️ fallback */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
