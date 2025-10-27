import axios from 'axios';
const API_BASE = import.meta.env.VITE_API_BASE || 'http://backend:8000';

export const getPods = (namespace="default") => {
    return axios.get(`${API_BASE}/pods?namespace=${namespace}`);
};

