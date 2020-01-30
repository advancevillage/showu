import service from './request'

const QueryImageUrl = (relative) => {
   const imageDomain =  "//localhost:13147/";
   return imageDomain + relative;
};

const QueryCategories = (params, headers) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const QueryGoods = (params, headers) => {
    return service({
        url: "/v1/goods",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

export default  {
    QueryImageUrl,
    QueryCategories,
    QueryGoods,
}