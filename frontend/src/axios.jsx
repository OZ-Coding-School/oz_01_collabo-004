import axios from "axios";

const request = axios.create({
    baseURL: "http://dog-go.store",
});
export default request;
