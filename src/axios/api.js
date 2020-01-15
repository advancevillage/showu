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

const QueryBrand = (pathId) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "get"
    })
};

const CreateBrand = (body) => {
    return service({
        url: "/v1/brands",
        method: "post",
        data: body || {}
    })
};

const UpdateBrand = (pathId, body) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "put",
        data: body || {}
    })
};

const DeleteBrand = (pathId) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "delete",
    })
};

export default  {
    QueryCategories,
    QueryBrands,
    QueryBrand,
    CreateBrand,
    UpdateBrand,
    DeleteBrand,
}