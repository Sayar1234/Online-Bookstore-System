import axiosInstance from "./axiosInstance";

export const createOrder = (data) => axiosInstance.post("/orders", data);

export const fetchOrders = () => axiosInstance.get("/orders");

export const fetchCart = () => axiosInstance.get("/cart");

export const addToCart = (bookId) => axiosInstance.post(`/cart/${bookId}`);

export const removeFromCart = (bookId) =>
  axiosInstance.delete(`/cart/${bookId}`);
