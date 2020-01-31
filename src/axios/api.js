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

const QueryGoods = (params, headers) => {
    return service({
        url: "/v1/goods",
        method: "get",
        params: params || {},
        headers: headers || {}
    })
};

const QueryOneGoods = (pathId, params, headers) => {
    return service({
        url: "/v1/goods/" + pathId,
        method: "get",
        params: params || {},
        headers: headers || {}
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
}