import service from './request'

const ImageDomain = "//localhost:13147/";

const QueryCategories = (params, headers) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryChildCategories = (pathId, params, headers) => {
    return service({
        url: "/v1/categories/" + pathId + "/categories",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateCategory = (body, headers) => {
    return service({
        url: "/v1/categories",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const QueryBrands = (params, headers) => {
    return service({
        url: "/v1/brands",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryBrand = (pathId) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "get",
        baseURL: '//localhost:13147',
    })
};

const CreateBrand = (body, headers) => {
    return service({
        url: "/v1/brands",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const UpdateBrand = (pathId, body, headers) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "put",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const DeleteBrand = (pathId, headers) => {
    return service({
        url: "/v1/brands/" + pathId,
        method: "delete",
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryColors = (params, headers) => {
    return service({
        url: "/v1/colors",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateSize = (body, headers) => {
    return service({
        url: "/v1/sizes",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const QuerySizes = (params, headers) => {
    return service({
        url: "/v1/sizes",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryManufacturers = (params, headers) => {
    return service({
        url: "/v1/manufacturers",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateManufacturer = (body, headers) => {
    return service({
        url: "/v1/manufacturers",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const CreateColor = (body, headers) => {
    return service({
        url: "/v1/colors",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const CreateGoods = (body, headers) => {
    return service({
        url: "/v1/goods",
        method: "post",
        headers: headers || {},
        data: body || {},
        baseURL: '//localhost:13147',
    })
};

const QueryGoods = (params, headers) => {
    return service({
        url: "/v1/goods",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
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
    CreateGoods,
    QueryGoods,
    ImageDomain,
}