export default function formatCurrency(amount) {
  return `₹${Number(amount).toFixed(2)}`;
}
