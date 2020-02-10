<template>
    <div>
        <div class="modal-card">
            <div class="login">
                <div v-if="register">
                    <p class="sign_header" v-html="languages.Login.register[language]" style="margin-left: 13%; margin-top: 11%"></p>
                    <p><b-button class="account_login"  type="is-dark" size="is-small" @click="register = false">{{languages.Login.login[language]}}</b-button></p>
                </div>
                <div v-else>
                    <p class="login_header" v-html="languages.Login.header[language]"></p>
                    <ul>
                        <li>
                            <div class="account_icon">
                                <b-icon icon="account-box"></b-icon>
                            </div>
                            <b-input v-model="account" class="account" placeholder="kelly@example.com" type="email" maxlength="30" minlength="7" size="is-small" @blur="QueryToken(0)"></b-input>
                            <span v-if="accountErr.length > 0" class="account_error" style="top: 42%;">{{this.accountErr}}</span>
                        </li>
                        <li><div class="password_icon"><b-icon icon="lock"></b-icon></div><b-input v-model="password" class="password" placeholder="password" type="password" maxlength="30" minlength="8" size="is-small" password-reveal></b-input></li>
                        <li><b-button class="account_forget" icon-left="alert-circle" type="is-light" size="is-small">{{languages.Login.forget[language]}}</b-button></li>
                        <li>
                            <b-button class="account_login"  type="is-dark" size="is-small" @click="QueryUser">{{languages.Login.login[language]}}</b-button>
                            <span v-if="loginErr.length > 0" class="login_error">{{this.loginErr}}</span>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="sign">
                <div v-if="register">
                    <p class="login_header" v-html="languages.Sign.header[language]" style="margin-top: 0; margin-bottom: 20px"></p>
                    <ul>
                        <li>
                            <div class="account_icon"><b-icon icon="account-box"></b-icon>
                            </div>
                            <span v-if="accountErr.length > 0" class="account_error">{{this.accountErr}}</span>
                            <b-input v-model="account" class="account" placeholder="kelly@example.com" type="email" maxlength="30" minlength="7" size="is-small" @blur="QueryToken(1)"></b-input>
                        </li>
                        <li><div class="password_icon"><b-icon icon="lock"></b-icon></div><b-input v-model="password" class="password" placeholder="password" type="password" maxlength="30" minlength="8" size="is-small" password-reveal></b-input></li>
                        <li>
                            <div class="account_gender">
                            <b-radio v-model="gender" size="is-small" type="is-dark" :native-value=women>{{languages.Sign.women[language]}}</b-radio>
                            <b-radio v-model="gender" size="is-small" type="is-dark" :native-value=man>{{languages.Sign.man[language]}}</b-radio>
                            </div>
                        </li>
                        <li><b-button class="account_login"  type="is-dark" size="is-small" @click="CreateUser">{{languages.Sign.sign[language]}}</b-button></li>
                        <span v-if="registerErr.length > 0" class="register_error">{{this.registerErr}}</span>
                    </ul>
                </div>
                <div v-else>
                    <p class="sign_header" v-html="languages.Sign.register[language]"></p>
                    <p><b-button class="account_sign"  type="is-dark" size="is-small" @click="register = true">{{languages.Sign.sign[language]}}</b-button></p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: "Login",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                languages: this.$languages,
                format: "YYYYMMDDHHmmss",
                account: "",
                password: "",
                token: "",
                gender: 0,
                man: 1,
                women: 0,
                register: false,
                accountErr: "",
                registerErr: "",
                loginErr: "",
            }
        },
        methods: {
            async QueryToken(category) {
                if (this.account.length <= 0) {
                    return
                }
                const headers = {
                    "x-language": this.language,
                };
                const body = {
                    "category": category,
                    "username": this.account,
                };
                let data = await this.$api.CreateToken(headers, body) || {};
                if (data.hasOwnProperty("code") && parseInt(data.code) > 999 ) {
                    this.accountErr = data.message;
                } else {
                    this.accountErr = "";
                    this.token = data.token;
                }
            },
            async CreateUser() {
                const headers = {
                    "x-language": this.language,
                };
                let password  = this.$utils.SHA1(this.password).toLowerCase();
                let timestamp = this.$moment(Date.now()).format(this.format);
                let sign      = this.$utils.SHA1(this.account + this.token + timestamp + password).toLowerCase();
                const body = {
                    "username": this.account,
                    "password": password,
                    "gender": this.gender,
                    "token": this.token,
                    "timestamp": timestamp,
                    "sign": sign,
                };
                let data = await this.$api.CreateUser(headers, body) || {};
                if (data.hasOwnProperty("code") && parseInt(data.code) > 999 ) {
                    this.registerErr = data.message;
                } else {
                    this.registerErr = "";
                    this.$emit('close');
                    this.$emit('triggerCheckLogin');
                }
            },
            async QueryUser() {
                const headers = {
                    "x-language": this.language,
                };
                let password  = this.$utils.SHA1(this.password).toLowerCase();
                let timestamp = this.$moment(Date.now()).format(this.format);
                let sign      = this.$utils.SHA1(this.account + this.token + timestamp + password).toLowerCase();
                const params = {
                    "username": this.account,
                    "password": password,
                    "token": this.token,
                    "timestamp": timestamp,
                    "sign": sign,
                };
                let data = await this.$api.QueryUser(headers, params) || {};
                if (data.hasOwnProperty("code") && parseInt(data.code) > 999 ) {
                    this.loginErr = data.message;
                } else {
                    this.loginErr = "";
                    this.$emit('close');
                    this.$emit('triggerCheckLogin');
                }
            }
        }
    }
</script>

<style scoped>
    .modal-card {
        width: 600px;
        height: 300px;
        flex-direction: row;
        background: rgb(192,192,192);
    }
    .login, .sign {
        width: 50%;
        height: 100%;
    }
    .sign {
        margin-top: 5%;
        margin-left: 1%;
        border-left: 2px solid;
    }
    .sign_header {
        display: block;
        margin: 10px;
        text-align: left;
        font-size: small;
        font-family: serif;
        line-height: 2rem;
    }
    .login_header {
        width: 100%;
        text-align: center;
        margin-top: 15%;
        margin-bottom: 30px;
        display: block;
        font-family: serif;
    }
    .login_header > b {
        font-weight: 900;
    }
    .account, .password {
        margin-left: 13%;
        width: 85%;
        padding: 0;
    }
    .account_icon, .password_icon {
        margin-left: 2%;
        width: 10%;
        color: gray;
        position: absolute;
    }
    .account_forget:hover {
        background: none;
    }
    .account_forget {
        float: right;
        background-color: rgba(192,192,192,1);
        text-decoration: underline;
        border: none;
    }
    .account_forget:focus, .account_login:focus, .account_sign:focus {
        border: none;
    }
    .account_login {
        width: 85%;
        margin-left: 13%;
    }
    .account_sign {
        width: 95%;
        margin: 2px 10px;
    }
    .account_gender {
        margin-left: 13%;
        margin-bottom: 5%;
    }
    .account_error, .register_error, .login_error {
        position: absolute;
        margin-left: 7%;
        top: 33%;
        font-size: small;
        font-family: serif;
        display: block;
        color: red;
    }
    .register_error {
        top: 79%;
    }
    .login_error {
        top: 84%;
    }
</style>