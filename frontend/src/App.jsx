import Navbar from "./components/Navbar";
import AppRoutes from "./routes/AppRoutes";
import Modal from "./components/Modal";
import Cart from "./pages/Cart";
import { useState } from "react";

export default function App() {
  const [cartOpen, setCartOpen] = useState(false);

  return (
    <>
      <Navbar onCartClick={() => setCartOpen(true)} />
      <AppRoutes />
      <Modal isOpen={cartOpen} onClose={() => setCartOpen(false)}>
        <Cart onClose={() => setCartOpen(false)} />
      </Modal>
    </>
  );
}
