import service from './request'

const QueryImageUrl = (relative) => {
   const imageDomain =  "//localhost:13147/";
   return imageDomain + relative;
};

/**
 * @param brand object 品牌对象
 * @param name  object 商品名称对象
 * @param category object 分类对象
 * @constructor
 */
const CreateDetailLink = (brand, category, name, id) => {
    //含义之间用 - 链接
    //去掉空格
    //全小写
    let en = "english";
    return ("/detail/" + brand.name[en] + "-" + category.name[en] + "-" + name[en] + "?gid=" + id).toLowerCase().trim().replace(/\s+/g, "");
};

const CreateListLink = (name, id) => {
    let en = "english";
    return ("/list/" + name[en] + "?cid=" + id).toLowerCase().trim().replace(/\s+/g, "");
};

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

const QueryGoods = (params, headers) => {
    return service({
        url: "/v1/goods",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryOneGoods = (pathId, params, headers) => {
    return service({
        url: "/v1/goods/" + pathId,
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateToken = (headers, body) => {
    return service({
        url: "/v1/tokens",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateUser = (headers, body) => {
    return service({
        url: "/v1/users",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryUser = (headers, params) => {
    return service({
        url: "/v1/users",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13173',
    })
};


const QueryCarts = (headers, params) => {
    return service({
        url: "/v1/carts",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13173',
    })
};

const CreateCarts = (headers, body) => {
    return service({
        url: "/v1/carts",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13173',
    })
};

const UpdateCart = (pathId, headers, body) => {
    return service({
        url: "/v1/carts/" + pathId,
        method: "put",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13173',
    })
};

const DeleteCart = (pathId, headers, params) => {
    return service({
        url: "/v1/carts/" + pathId,
        method: "delete",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13173',
    })
};

export default  {
    QueryImageUrl,
    CreateListLink,
    QueryCategories,
    QueryChildCategories,
    QueryGoods,
    QueryOneGoods,
    CreateDetailLink,
    CreateToken,
    CreateUser,
    QueryUser,
    QueryCarts,
    CreateCarts,
    UpdateCart,
    DeleteCart
}