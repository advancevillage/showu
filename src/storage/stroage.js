import localStorage from 'store'
import localCookie  from 'vue-cookie'

const QueryCookie = (key) => {
    return localCookie.get(key)
};

const QueryLocalStorage = (key) => {
    return localStorage.get(key);
};

const CreateLocalStorage = (key, value) => {
    localStorage.set(key, value)
};

export default  {
    QueryCookie,
    QueryLocalStorage,
    CreateLocalStorage,
}