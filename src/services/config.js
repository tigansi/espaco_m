import axios from "axios";

export const http = axios.create({
  //baseURL: "http://192.168.8.7:5000/",
  baseURL: "http://192.168.1.166:5000/",
  //baseURL: "http://192.168.1.106:5000/",
  //baseURL: "http://192.168.8.15:5000/"
});
