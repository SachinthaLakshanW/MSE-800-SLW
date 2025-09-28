import { Outlet } from "react-router-dom";
import NavBar from "../Components/NavBar";

export default function AppLayout() {
  return (
    <>
      <NavBar />
      <div className="container py-3">
        <Outlet />
      </div>
    </>
  );
}