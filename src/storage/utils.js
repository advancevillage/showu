import storage from './storage'

const keys = {
    carts: "carts",
    sessionId: "sid"
};

const Singles = {
    SingleOfAddCart:  "sig_add_cart",
    SingleOfPushCart: "sig_push_cart",
    SingleOfPopCart:  "sig_pop_cart",
    SingleOfUpdateCart: "sig_update_cart",
    SingleOfDeleteCart: "sig_delete_cart",
    SingleOfLogin: "sig_query_login",
    SingleOfOpenLogin: "sig_open_login",

};

const QueryLogin = () => {
    return storage.QueryCookie(keys.sessionId) || "";
};

const DeleteLogin = () => {
    storage.DeleteCookie(keys.sessionId);
};

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
    QueryCart,
    UpdateCart,
    DeleteCart,
    QueryLogin,
    DeleteLogin,
    SHA1
}