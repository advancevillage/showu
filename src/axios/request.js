import axios from 'axios';

// 请求的默认域名
const service = axios.create({
    baseURL: 'http://localhost:13171',
    timeout: 60 * 1000,
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
    if (!error.response) {
        let response = {};
        response.code = 110;
        response.message = "network error";
        return response
    } else {
        return error.response.data
    }
});


export default  service;