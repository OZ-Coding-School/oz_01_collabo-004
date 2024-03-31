import axios from "axios";

const request = axios.create({
  baseURL: "https://d865-114-207-131-9.ngrok-free.app",
  headers: {
    "Content-Type": "application/json",
    "ngrok-skip-browser-warning": "69420",
  },
  withCredentials: true,
});

export default request;
