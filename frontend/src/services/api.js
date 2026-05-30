import axios from "axios";

const API = axios.create({
  baseURL: "https://transitwatch-ai.onrender.com",
});

export default API;