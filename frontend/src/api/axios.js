import axios from "axios";
import { Navigate } from "react-router-dom";
const navigate = Navigate()
const request = axios.create({
  baseURL: "https://dog-go.store/",
  headers: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
});
const refreshToken = async () => {
  try {
    const response = await axios.post(
      "https://dog-go.store/api/v1/user/simple/jwt_refresh_token",
      {}
    );
    const newAccessToken = response.data.access;
    localStorage.setItem("token", newAccessToken);
    return newAccessToken;
  } catch (error) {
    if(error.response.status === 400){
      localStorage.removeItem("token")
      alert("로그인이 만료되었습니다. 다시 로그인 해주세요.")
      navigate("/login")
    }
    throw error;
  }
};

request.interceptors.request.use(
  async (config) => {
    const accessToken = localStorage.getItem("token");
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

request.interceptors.response.use(
  (response) => {
    return response;
  },
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      try {
        const newAccessToken = await refreshToken();
        originalRequest._retry = true;
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return request(originalRequest);
      } catch (error) {
        console.log("리프레시 토큰 에러", error);
        throw error;
      }
    }
    return Promise.reject(error);
  }
);

export default request;
