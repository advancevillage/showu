import storage from './storage'

const keys = {
    carts: "carts",
    sessionId: "sid"
};

const QueryLogin = () => {
    let value = storage.QueryCookie(keys.sessionId);
    console.log(value);
    return value
};

//TODO 复杂度
const CheckLogin = () => {
    let value = storage.QueryCookie(keys.sessionId) || "";
    return value.length > 0
};

const QueryCart = () => {
    return JSON.parse(storage.QueryLocalStorage(keys.carts))
};

const AddCart = (item) => {
    let carts = JSON.parse(storage.QueryLocalStorage(keys.carts));
    let i = 0;
    for (i = 0; i < carts.length; i++) {
        if (carts[i].gid === item.gid && carts[i].colorId === item.colorId && carts[i].sizeId === item.sizeId) {
            break;
        } else {
            continue
        }
    }
    if (i < carts.length) {
        carts[i].count++;
    } else {
        carts.push(item);
    }
    storage.CreateLocalStorage(keys.carts, JSON.stringify(carts));
    console.log(CheckLogin());
};

const SHA1 = (message) => {
    return storage.sha1(message)

};

export default {
    AddCart,
    QueryCart,
    QueryLogin,
    CheckLogin,
    SHA1,
}