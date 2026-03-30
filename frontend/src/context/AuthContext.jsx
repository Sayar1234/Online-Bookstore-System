import { createContext, useState, useEffect, useCallback } from "react";
import { getProfile } from "../api/authApi";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(!!localStorage.getItem("token"));

  const logout = useCallback(() => {
    localStorage.removeItem("token");
    setToken(null);
    setUser(null);
    setLoading(false);
  }, []);

  const login = (token) => {
    localStorage.setItem("token", token);
    setToken(token);
  };

  useEffect(() => {
    if (!token) {
      return;
    }

    let isMounted = true;

    setLoading(true);

    getProfile()
      .then((res) => {
        if (isMounted) {
          setUser(res.data);
        }
      })
      .catch((err) => {
        console.error("Profile error:", err);
        if (isMounted) {
          logout();
        }
      })
      .finally(() => {
        if (isMounted) setLoading(false);
      });

    return () => {
      isMounted = false;
    };
  }, [token]);

  return (
    <AuthContext.Provider value={{ token, user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}
