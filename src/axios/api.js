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

const GenerateLink = (type, project, name, id) => {
    let language = "en";
    return ("/" + type + "/" + project + "-" + name[language] + "-" + id).toLowerCase().trim().replace(/\s+/g, "-");
}

const QueryCategories = (headers, params) => {
    return service({
        url: "/v1/categories",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
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

const QueryGoods = (headers, params) => {
    return service({
        url: "/v1/goods",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryOneGoods = (pathId, headers, params) => {
    return service({
        url: "/v1/goods/" + pathId,
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};
const QuerySimilarGoods = (headers, params) => {
    return service({
        url: "/v1/similarGoods/",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
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
        baseURL: '//localhost:13147',
    })
};

const QueryCarts = (headers, params) => {
    return service({
        url: "/v1/carts",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const CreateCarts = (headers, body) => {
    return service({
        url: "/v1/carts",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const UpdateCart = (pathId, headers, body) => {
    return service({
        url: "/v1/carts/" + pathId,
        method: "put",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const DeleteCart = (pathId, headers, params) => {
    return service({
        url: "/v1/carts/" + pathId,
        method: "delete",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateAddress = (headers, body) => {
    return service({
        url: "/v1/address",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryAddress = (headers, params) => {
    return service({
        url: "/v1/address",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateCreditCard = (headers, body) => {
    return service({
        url: "/v1/credit",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const CreateOrderToken = (headers, body) => {
    return service({
        url: "/v1/orderToken",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};


const CreateOrder = (headers, body) => {
    return service({
        url: "/v1/orders",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryOrder = (headers, params) => {
    return service({
        url: "/v1/orders",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryOneOrder = (pathId, headers, params) => {
    return service({
        url: "/v1/orders/" + pathId,
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:13179',
    })
};

const CreatePayToken = (headers, body) => {
    return service({
        url: "/v1/payToken",
        method: "post",
        data: body || {},
        headers: headers || {},
        baseURL: '//localhost:13147',
    })
};

const QueryNotices = (headers, params) => {
    return service({
        url: "/v1/notices",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryCountries = (headers, params) => {
    return service({
        url: "/v1/countries",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryProvinces = (headers, params) => {
    return service({
        url: "/v1/provinces",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryBanners = (headers, params) => {
    return service({
        url: "/v1/banners",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryNewIns = (headers, params) => {
    return service({
        url: "/v1/newIns",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryHots = (headers, params) => {
    return service({
        url: "/v1/hots",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryFooters = (headers, params) => {
    return service({
        url: "/v1/footers",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QuerySizes = (headers, params) => {
    return service({
        url: "/v1/sizes",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

const QueryColors = (headers, params) => {
    return service({
        url: "/v1/colors",
        method: "get",
        params: params || {},
        headers: headers || {},
        baseURL: '//localhost:20520',
    })
};

export default  {
    GenerateLink,
    QueryBanners,
    QueryColors,
    QueryCountries,
    QueryFooters,
    QueryHots,
    QueryNotices,
    QueryNewIns,
    QueryProvinces,
    QuerySizes,
    QuerySimilarGoods,

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
    DeleteCart,
    CreateAddress,
    QueryAddress,
    CreateCreditCard,
    CreateOrderToken,
    CreateOrder,
    QueryOrder,
    QueryOneOrder,
    CreatePayToken,
}