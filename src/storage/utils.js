import storage from './storage'

const keys = {
    carts:      "carts",
    sessionId:  "sid"
};

const SIG = {
    AddCart: "0x0001",
}


const Singles = {
    SingleOfAddCart:  "sig_add_cart",
    SingleOfPushCart: "sig_push_cart",
    SingleOfPopCart:  "sig_pop_cart",
    SingleOfUpdateCart: "sig_update_cart",
    SingleOfDeleteCart: "sig_delete_cart",
    SingleOfLogin: "sig_query_login",
    SingleOfOpenLogin: "sig_open_login",
    SingleOfQueryCreditLogo: "sig_query_credit_logo"
};

/**
 * @brief: 用户登录操作 是否登录/登出
 */
const HasLogin = () => {
    return (storage.QueryCookie(keys.sessionId) || "").length !== 0;
}
const Logout = () => {
    storage.DeleteCookie(keys.sessionId);
}

/**
 * @brief: 购物车 无登录状态处理购物车
 */
const UpdateCart = (data) => {
   storage.CreateLocalStorage (keys.carts, JSON.stringify(data))
};

const QueryCart = () => {
    return JSON.parse(storage.QueryLocalStorage(keys.carts))
};

const DeleteCart = () => {
    storage.DeleteLocalStorage(keys.carts);
};

const SHA1 = (message) => {
    return storage.sha1(message)
};

export default {
    Singles,
    Logout,
    HasLogin,
    SIG,

    QueryCart,
    UpdateCart,
    DeleteCart,
    SHA1
}