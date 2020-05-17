<template>
    <div class="address" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <form>
            <div>
                <label for="email">{{languages.ADDRESS.EMAIL[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="email" />
            </div>
            <div>
                <label for="fullName">{{languages.ADDRESS.FULL_NAME[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="fullName" />
            </div>
            <div>
                <label for="password">{{languages.ADDRESS.PASSWORD[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="password" id="password" />
            </div>
            <div>
                <label for="confirm_password">{{languages.ADDRESS.CONFIRM_PASSWORD[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="password" id="confirm_password"/>
            </div>
            <div>
                <label for="line_1">{{languages.ADDRESS.LINE_1[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="line_1"/>
            </div>
            <div>
                <label for="line_2">{{languages.ADDRESS.LINE_2[language]}}</label>
                <input type="text" id="line_2"/>
            </div>
            <div>
                <label for="zip_code">{{languages.ADDRESS.ZIP_CODE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="zip_code"/>
            </div>
            <div>
                <label for="city">{{languages.ADDRESS.CITY[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="city"/>
            </div>
            <div>
                <label for="province">{{languages.ADDRESS.PROVINCE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <select id="province">
                    <option value ="volvo">Volvo</option>
                    <option value ="saab">Saab</option>
                    <option value="opel">Opel</option>
                    <option value="audi">Audi</option>
                </select>
            </div>
            <div>
                <label for="country">{{languages.ADDRESS.COUNTRY[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <select id="country">
                    <option value ="volvo">Volvo</option>
                    <option value ="saab">Saab</option>
                    <option value="opel">Opel</option>
                    <option value="audi">Audi</option>
                </select>
            </div>
            <div>
                <label for="phone">{{languages.ADDRESS.PHONE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input type="text" id="phone"/>
            </div>
            <span>
                <label for="agree"></label>
                <input type="checkbox" id="agree"/>
                <span><a>{{languages.ADDRESS.PRIVACY_POLICY[language]}}</a></span>
            </span>
            <span>
                <button>{{languages.OPERATE.SAVE[language]}}</button>
            </span>
        </form>
    </div>
</template>

<script>
    export default {
        name: "Address",
        props: {
            width: {
                type: Number,
                required: false,
                default: 600,
            },
            height: {
                type: Number,
                required: false,
                default: 800,
            },
            language: {
                type: String,
                required: false,
                default: "en"
            }
        },
        data() {
            return {
                languages: this.$languages,
            }
        }
    }
</script>

<style scoped>
    .address {
        border: 1px solid darkgray;
        padding: 1%;
    }
    .address > form > div {
        width: 45%;
        float: left;
        margin: 0 2% 5%;
    }
    .address > form > div > label {
        display: block;
        color: #666;
        cursor: pointer;
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: .5rem;
        width: 100%;
    }
    .address > form > div > label > small {
        float: right;
        margin-top: .375rem;
        color: #000;
        font-size: .625rem;
        text-transform: uppercase;
        vertical-align: bottom;
    }
    .address > form > div > input, .address > form > div > select {
        appearance: none;
        background-color: #fff;
        border-color: #ccc;
        color: #666;
        font-size: 1rem;
        height: 3rem;
        padding: .75rem 1rem;
        transition: border-color .1s ease-out;
        border-style: solid;
        border-width: 1px;
        font-family: inherit;
        margin: 0;
        box-shadow: none;
        outline: none;
        width: 100%;
    }
    .address > form > span {
        display: inline-block;
        width: 100%;
        margin: 0 2% 5%;
        font-size: 16px;
        letter-spacing: .2px;
    }
    .address > form > span button {
        width: 95%;
        height: 40px;
        border-radius: 5px;
        box-shadow: none;
        outline: none;
        line-height: 40px
    }
    .address > form > span > button {
        background: #000000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: 1rem;
        width: 95%;
        height: 3rem;
        outline: none;
        opacity: 0.75;
        letter-spacing: 0.5rem;
    }
    .address > form > span > button:hover {
        opacity: 1;
    }
    .address > form > span a {
        text-decoration: underline;
        color: black;
        font-size: 12px;
        letter-spacing: .2px;
        margin: 0 2%;
    }
</style>