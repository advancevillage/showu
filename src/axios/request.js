import axios from 'axios';
import qs from 'qs';

// 请求的默认域名
const service = axios.create({
    baseURL: 'http://localhost:13147',
    timeout: 15 * 1000,
    responseType: 'json',
});

service.interceptors.request.use(config => {
    config.method === 'post'
        ? config.data = qs.stringify({...config.data})
        : config.params = {...config.params};
    config.headers["Content-Type"] = "application/json";
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