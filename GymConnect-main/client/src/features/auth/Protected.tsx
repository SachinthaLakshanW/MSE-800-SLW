import { ReactNode } from "react";
import { Navigate, useLocation } from "react-router-dom";

export default function Protected({ children }: { children: ReactNode }) {
  const token = localStorage.getItem("auth_token"); // replace with real auth
  const location = useLocation();
  if (!token) return <Navigate to="/login" replace state={{ from: location }} />;
  return <>{children}</>;
}