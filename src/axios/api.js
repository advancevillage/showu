import service from './request'

const QueryCategories = (params, headers) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const CreateCategory = (body, headers) => {
    return service({
        url: "/v1/categories",
        method: "post",
        headers: headers || {},
        data: body || {}
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

const CreateBrand = (body, headers) => {
    return service({
        url: "/v1/brands",
        method: "post",
        headers: headers || {},
        data: body || {}
    })
};

const UpdateBrand = (pathId, body, headers) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "put",
        headers: headers || {},
        data: body || {}
    })
};

const DeleteBrand = (pathId, headers) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "delete",
        headers: headers || {}
    })
};

export default  {
    QueryCategories,
    CreateCategory,
    QueryBrands,
    QueryBrand,
    CreateBrand,
    UpdateBrand,
    DeleteBrand,
}