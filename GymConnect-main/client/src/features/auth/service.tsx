import api from "../../core/http/client";

export const AuthService = {
  login: (email: string, password: string) =>
    api.post("/auth/login", { email, password }),

  register: (email: string, password: string, name: string) =>
    api.post("/auth/register", { email, password, name }),

  me: () => api.get("/auth/me"),
};
