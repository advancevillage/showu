import service from './request'

const QueryCategories = (params, headers) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const QueryChildCategories = (pathId, params, headers) => {
    return service({
        url: "/v1/categories/" + pathId + "/categories",
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

const QueryColors = (params, headers) => {
    return service({
        url: "/v1/colors",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const CreateSize = (body, headers) => {
    return service({
        url: "/v1/sizes",
        method: "post",
        headers: headers || {},
        data: body || {}
    })
};

const QuerySizes = (params, headers) => {
    return service({
        url: "/v1/sizes",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const QueryManufacturers = (params, headers) => {
    return service({
        url: "/v1/manufacturers",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const CreateManufacturer = (body, headers) => {
    return service({
        url: "/v1/manufacturers",
        method: "post",
        headers: headers || {},
        data: body || {}
    })
};

const CreateColor = (body, headers) => {
    return service({
        url: "/v1/colors",
        method: "post",
        headers: headers || {},
        data: body || {}
    })
};

export default  {
    QueryCategories,
    QueryChildCategories,
    CreateCategory,
    QueryBrands,
    QueryBrand,
    CreateBrand,
    UpdateBrand,
    DeleteBrand,
    QueryColors,
    QuerySizes,
    CreateSize,
    QueryManufacturers,
    CreateManufacturer,
    CreateColor,
}