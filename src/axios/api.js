import service from './request'

const QueryCategories = (params, headers) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const QueryBrands = (params, headers) => {
    return service({
        url: "/v1/brands",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

export default  {
    QueryCategories,
    QueryBrands,
}