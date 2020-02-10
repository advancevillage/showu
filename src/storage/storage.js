import localStorage from 'store'
import CryptoJS     from 'crypto-js'
import localCookie  from 'vue-cookie'

const info = {
    key: "20170729202005151994021519951101",
    iv: "1994021519951101"
};

const QueryCookie = (key) => {
    return localCookie.get(key)
};

const QueryLocalStorage = (key) => {
    let value =  localStorage.get(key) || "";
    if (value.length === 0) {
        return "[]";
    } else {
        return decode(value, info.key, info.iv);
    }
};

const CreateLocalStorage = (key, value) => {
    let aes = encode(value, info.key, info.iv);
    localStorage.set(key, aes)
};

//@link: https://www.jianshu.com/p/1aed5b55ca27
function encode(data,key,iv){//加密
    let encrypted =CryptoJS.AES.encrypt(data,CryptoJS.enc.Utf8.parse(key), {
            iv:CryptoJS.enc.Utf8.parse(iv),
            mode:CryptoJS.mode.CBC,
            padding:CryptoJS.pad.Pkcs7
        });
    return encrypted.toString();    //返回的是base64格式的密文
}
function decode(encrypted,key,iv){//解密
    let decrypted =CryptoJS.AES.decrypt(encrypted,CryptoJS.enc.Utf8.parse(key), {
            iv:CryptoJS.enc.Utf8.parse(iv),
            mode:CryptoJS.mode.CBC,
            padding:CryptoJS.pad.Pkcs7
        });
    return decrypted.toString(CryptoJS.enc.Utf8);
}

const sha1 = (message) => {
    //.toString(CryptoJS.enc.Hex)
    return CryptoJS.SHA1(message).toString()
};

export default  {
    QueryCookie,
    QueryLocalStorage,
    CreateLocalStorage,
    sha1,
}