import axios from 'axios';

// 请求的默认域名
const service = axios.create({
    baseURL: 'http://localhost:13147',
    timeout: 15 * 1000,
    responseType: 'json',
    headers: {
        post: {
            "Content-Type": "application/json"
        },
        put: {
            "Content-Type": "application/json"
        }
    }
});

service.interceptors.request.use(config => {
    if (config.method === 'post') {
        config.data = JSON.stringify(config.data);
    }
    return config;
}, error => {
    console.log(error);
});


service.interceptors.response.use(response => {
    return response.data
}, error => {
    console.log(error);
});


export default  service;