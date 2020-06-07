<template>
    <div class="ss_address modal-card" v-bind:style="{width: width + 'px'}">
        <form v-if="type" class="ss_address_detail">
            <div>
                <label for="email">{{languages.ADDRESS.EMAIL[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input v-model="item.email" type="text" id="email" />
            </div>
            <div>
                <label for="fullName">{{languages.ADDRESS.FULL_NAME[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input v-model="item.fullName" type="text" id="fullName" />
            </div>
            <div>
                <label for="line_1">{{languages.ADDRESS.LINE_1[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input v-model="item.line1" type="text" id="line_1"/>
            </div>
            <div>
                <label for="line_2">{{languages.ADDRESS.LINE_2[language]}}</label>
                <input v-model="item.line2" type="text" id="line_2"/>
            </div>
            <div>
                <label for="zip_code">{{languages.ADDRESS.ZIP_CODE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input v-model="item.zipCode" type="text" id="zip_code"/>
            </div>
            <div>
                <label for="city">{{languages.ADDRESS.CITY[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <select id="city" v-model="item.city">
                    <option v-for="(item, index) in cities" :key="index" :value="item">{{item}}</option>
                </select>
            </div>
            <div>
                <label for="province">{{languages.ADDRESS.PROVINCE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <select id="province" v-model="item.province" @change="changeProvince($event)">
                    <option v-for="(item, index) in provinces" :key="index" :value="item.value">{{item.value}}</option>
                </select>
            </div>
            <div>
                <label for="country">{{languages.ADDRESS.COUNTRY[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <select id="country" v-model="item.country" @change="changeCountry()">
                    <option v-for="(item, index) in countries" :key="index" :value="item.value">{{item.value}}</option>
                </select>
            </div>
            <div>
                <label for="phone">{{languages.ADDRESS.PHONE[language]}}
                    <small>{{languages.ADDRESS.REQUIRED[language]}}</small>
                </label>
                <input v-model="item.phone" type="text" id="phone"/>
            </div>
            <span>
                <button  type="button" @click="save(item)">{{languages.OPERATE.SAVE[language]}}</button>
            </span>
        </form>
        <form v-else class="ss_address_item">
            <button type="button" @click="clear(item)"><span class="mdi mdi-delete"></span></button>
            <Dialog :params="params" icon="mdi mdi-playlist-edit" />
            <label>
                <input v-model="self_which" type="radio" :value="id"  @change="selected()"/>
            </label>
            <div>
                <span>{{item.fullName}}</span>
                <span>{{item.email}}</span>
                <span>{{item.phone}}</span>
                <span>{{item.zipCode}}</span>
                <span>{{item.city + " " + item.province + " " + item.country}}</span>
                <span>{{item.line1}}</span>
                <span v-if="item.line2 && item.line2.length > 0">{{item.line2}}</span>
            </div>
        </form>
    </div>
</template>

<script>
    import Dialog  from "../Basic/Dialog";
    import Address  from "./Address";

    export default {
        name: "Address",
        components: {
            Dialog,
        },
        props: {
            item: {
                type: Object,
                required: true
            },
            id: {
                type: Number,
                required: true,
            },
            which: {
                type: Number,
                required: false,
                default: -1,
            },
            width: {
                type: Number,
                required: false,
                default: 200,
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
            },
            type: {
                type: Boolean,
                required: false,
                default: false
            },
        },
        watch: {
           which() {
               this.self_which = this.which;
           }
        },
        data() {
            return {
                languages: this.$languages,
                params: {
                    props: {
                        language: this.language,
                        item: this.item,
                        type: true,
                        width: this.width * 3
                    },
                    component: Address,
                },
                countries: [],
                provinces: [],
                cities: [],
                self_which: -1
            }
        },
        mounted() {
            this.self_which = this.which;
            this.QueryCountries();
            this.QueryProvinces();
        },
        methods: {
            save(item) {
                item.save(item);
                this.$emit('close');
            },
            clear(item) {
                this.$emit('clear', item, this.id)
            },
            selected() {
                this.$emit('which', this.self_which);
            },
            changeProvince(e) {
                this.cities = this.provinces[e.target.selectedIndex].cities || [];
            },
            changeCountry() {
                this.QueryProvinces();
            },
            async QueryCountries() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCountries(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.countries = response.data.items;
                }
            },
            async QueryProvinces() {
                const params = {
                    country: this.item.country,
                };
                const headers = {};
                let response = await this.$api.QueryProvinces(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.provinces = response.data.items;
                }
            },
        }
    }
</script>

<style scoped>
    .ss_address {
        border: 1px solid lightgray;
        padding: 1%;
        height: auto;
        background: white;
        margin: 0;
    }
    .ss_address:hover {
        border: 1px solid black;
    }
    .ss_address_detail > div {
        width: 45%;
        float: left;
        margin: 0 2% 5%;
    }
    .ss_address_detail > div > label {
        display: block;
        color: #666;
        cursor: pointer;
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: .5rem;
        width: 100%;
    }
    .ss_address_detail > div > label > small {
        float: right;
        margin-top: .375rem;
        color: #000;
        font-size: .625rem;
        text-transform: uppercase;
        vertical-align: bottom;
    }
    .ss_address_detail > div > input, .ss_address_detail > div > select {
        appearance: none;
        background-color: #fff;
        border-color: #ccc;
        color: #666;
        font-size: 1rem;
        height: 3rem;
        padding: .75rem 1rem;
        transition: border-color .1s ease-out;
        border-style: solid;
        border-width: 2px;
        border-top: none;
        border-left: none;
        border-right: none;
        font-family: inherit;
        margin: 0;
        box-shadow: none;
        outline: none;
        width: 100%;
    }
    .ss_address_detail > div > input:focus {
        border-color: black;
        color: black;
    }
    .ss_address_detail > span {
        display: inline-block;
        width: 100%;
        margin: 0 2% 2%;
        font-size: 16px;
        letter-spacing: .2px;
    }
    .ss_address_detail > span button {
        width: 95%;
        height: 40px;
        border-radius: 5px;
        box-shadow: none;
        outline: none;
        line-height: 40px
    }
    .ss_address_detail > span > button {
        background: #000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: x-large;
        width: 95%;
        height: 3rem;
        outline: none;
        letter-spacing: 0.2rem;
    }
    .ss_address_detail > span > button:hover {
        background: #1524d9;
    }
    .ss_address_detail > span a {
        text-decoration: underline;
        color: black;
        font-size: 12px;
        letter-spacing: .2px;
        margin: 0 2%;
    }
    .ss_address_item {
        position: relative;
    }
    .ss_address_item > div {
        /*border: 1px solid red;*/
    }
    .ss_address_item > button, .ss_address_item > label {
        float: right;
        cursor: pointer;
        margin: 0 1%;
        text-align: center;
        color: black;
    }
    .ss_address_item > div > span {
        display: inline-block;
        width: 100%;
        text-align: left;
        margin-bottom: 2%;
        word-spacing: normal;
    }
</style>