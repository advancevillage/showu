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

const CreateBrand = (body) => {
    return service({
        url: "/v1/brands",
        method: "post",
        data: body || {}
    })
};

export default  {
    QueryCategories,
    QueryBrands,
    CreateBrand,
}