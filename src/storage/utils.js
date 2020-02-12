import storage from './storage'

const keys = {
    carts: "carts",
    sessionId: "sid"
};

const Singles = {
    SingleOfAddCart: "sig_add_cart"
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