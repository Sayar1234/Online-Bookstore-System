import useFetch from "../hooks/useFetch";
import { fetchOrders } from "../api/orderApi";
import Loader from "../components/Loader";

export default function Orders() {
  const { data, loading, error } = useFetch(fetchOrders);

  if (loading) return <Loader />;

  // 🔥 Normalize response
  const normalizeOrder = (order) => ({
    id: order.id || order._id,
    created_at: order.created_at || order.createdAt,
    status: order.status || "pending",
    items: order.items || order.order_items || [],
    total_amount: order.total_amount || order.total || 0,
  });

  // 🔥 Handle Axios / different shapes
  let orders = [];

  if (Array.isArray(data)) {
    orders = data;
  } else if (Array.isArray(data?.orders)) {
    orders = data.orders;
  } else if (Array.isArray(data?.data)) {
    orders = data.data;
  }

  const normalizedOrders = orders.map(normalizeOrder);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Your Orders</h1>

      {error && <p className="text-red-600 mb-4">{error}</p>}

      {normalizedOrders.length === 0 ? (
        <p className="text-gray-600">No orders yet</p>
      ) : (
        <div className="space-y-4">
          {normalizedOrders.map((order) => (
            <div key={order.id} className="border p-4 rounded">
              <div className="mb-3">
                <h3 className="font-bold text-lg">
                  Order #{order.id?.slice(-8) || "N/A"}
                </h3>

                <p className="text-gray-600 text-sm">
                  Date:{" "}
                  {order.created_at
                    ? new Date(order.created_at).toLocaleDateString()
                    : "N/A"}
                </p>
              </div>

              <div className="mb-3">
                <p className="text-sm">
                  <span className="font-semibold">Status:</span>

                  <span
                    className={`ml-2 px-2 py-1 rounded text-xs font-bold ${
                      order.status === "completed"
                        ? "bg-green-200 text-green-800"
                        : order.status === "pending"
                          ? "bg-yellow-200 text-yellow-800"
                          : "bg-red-200 text-red-800"
                    }`}
                  >
                    {order.status.toUpperCase()}
                  </span>
                </p>
              </div>

              {order.items.length > 0 && (
                <div className="bg-gray-50 p-3 rounded mb-3">
                  <p className="font-semibold text-sm mb-2">Items:</p>

                  {order.items.map((item, index) => {
                    const itemTotal =
                      item.total ?? item.price * item.quantity ?? 0;

                    return (
                      <p
                        key={item.id || index}
                        className="text-sm text-gray-700"
                      >
                        {item.title || "Item"} × {item.quantity} = ₹{itemTotal}
                      </p>
                    );
                  })}
                </div>
              )}

              <div className="pt-2 border-t">
                <p className="font-bold text-lg">
                  Total: ₹{order.total_amount}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
