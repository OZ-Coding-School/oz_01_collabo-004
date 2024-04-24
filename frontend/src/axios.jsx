import axios from "axios";

const request = axios.create({
    baseURL: "https://dog-go.store",
});
export default request;
