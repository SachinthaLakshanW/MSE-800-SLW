// import { createBrowserRouter } from "react-router-dom";
import AppLayout from "../layout/AppLayout";
import DashboardLayout from "../layout/DashboardLayout";
import LoginPage from "../features/auth/login";
import RegisterPage from "../features/auth/register";
import DashboardPage from "../features/dashboard/Dashboard";
// import { Protected } from "../hooks/useAuth";
import { createBrowserRouter } from "react-router-dom";
import Protected from "../features/auth/Protected";
import Home from "../features/home/home";
import Locations from "../features/locations/location";

const user = { username: "", role: "" }; 

export const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { path: "/", element: <Home /> }, // or a Home page if you have one
      { path: "/login", element: <LoginPage onLogin={handleLogin} /> },
      { path: "/register", element: <RegisterPage /> },
      { path: "/locations", element: <Locations /> },

      {
        element: (
          <Protected>
            <DashboardLayout  user={user} onLogout={handleLogout} />
          </Protected>
        ),
        children: [
          { path: "/dashboard", element: <DashboardPage user={user} onLogout={handleLogout} /> },
        ],
      },
    ],
  },
]);
function handleLogin(userObjct: any): void {
    throw new Error("Function not implemented.");
}

function handleLogout(): void {
    throw new Error("Function not implemented.");
}

