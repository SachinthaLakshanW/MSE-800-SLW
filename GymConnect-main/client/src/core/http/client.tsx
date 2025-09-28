import axios from 'axios';


const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    withCredentials: true, // if you use cookies
});

// Add token automatically if you store it in localStorage
api.interceptors.request.use((config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

// Optional: handle errors globally
api.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      // token missing/expired/invalid
      window.location.href = "/auth/login";
    }
    return Promise.reject(err);
  }
);

export default api;