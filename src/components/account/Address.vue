<template>
    <div class="modal-card">
        <!-- 收货人 -->
        <div class="fullName">
            <label>{{this.languages.Address.fullName[this.language]}}</label>
            <input v-model="address.fullName" type="text"/>
        </div>
        <!-- 国家 -->
        <div class="country">
            <label>{{this.languages.Address.country[this.language]}}</label>
            <select v-model="address.country">
                <option v-for="(item, index) in country.items" :key="index">{{item.value}}</option>
            </select>
        </div>
        <div class="line1">
            <label>{{this.languages.Address.line1[this.language]}}</label>
            <input v-model="address.line1" type="text"/>
        </div>
        <div class="line2">
            <label>{{this.languages.Address.line2[this.language]}}</label>
            <input v-model="address.line2" type="text"/>
        </div>
        <div class="city">
            <label>{{this.languages.Address.city[this.language]}}</label>
            <select v-model="address.city">
                <option v-for="(item, index) in city.items" :key="index">{{item.value}}</option>
            </select>
        </div>
        <div class="province">
            <label>{{this.languages.Address.province[this.language]}}</label>
            <select v-model="address.province">
                <option v-for="(item, index) in province.items" :key="index">{{item.value}}</option>
            </select>
        </div>
        <div class="zipCode">
            <label>{{this.languages.Address.zipCode[this.language]}}</label>
            <input v-model="address.zipCode" type="text"/>
        </div>
        <div class="phone">
            <label>{{this.languages.Address.phone[this.language]}}</label>
            <input v-model="address.phone" type="text"/>
        </div>
        <div class="address_action">
            <button type="button" @click="CreateAddress">{{this.languages.Address.create[this.language]}}</button>
            <span v-if="addressErr.length > 0">{{this.addressErr}}</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Address",
        props: {
            language: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                languages: this.$languages,
                country: {
                    total: 0,
                    items: [
                        {key: "cn", value: "中国"},
                        {key: "us", value: "美国"}
                    ]
                },
                province: {
                    total: 0,
                    items: [
                        {key: "beijing", value: "北京"},
                        {key: "shanghai", value: "上海"},
                    ]
                },
                city: {
                    total: 0,
                    items: [
                        {key: "beijing", value: "北京"},
                        {key: "shanghai", value: "上海"},
                    ]
                },
                area: {
                    total: 0,
                    items: [
                        {key: "beijing", value: "北京"},
                        {key: "shanghai", value: "上海"},
                    ]
                },
                address: {
                    fullName: "",
                    line1: "",
                    line2: "",
                    phone: "",
                    zipCode: "",
                    country: "",
                    city: "",
                    province: "",
                },
                addressErr: "",
            }
        },
        methods: {
            async CreateAddress() {
                let body = this.address || {};
                const headers = {
                    "x-language": this.language,
                };
                let data = await  this.$api.CreateAddress(headers, body);
                if (data.hasOwnProperty("code") && parseInt(data.code) > 299) {
                    this.addressErr = data.message;
                } else {
                    this.addressErr = "";
                    this.$emit('close');
                }
            }
        }
    }
</script>

<style scoped>
    .modal-card {
        width: 450px;
        height: auto;
        padding-bottom: 5%;
        background: rgb(64,64,64);
        display: block;
    }
    .fullName, .line1, .line2, .country, .city, .province, .phone, .zipCode, .address_action {
        padding: 4% 4% 0;
        margin: 0;
        width: 100%;
    }
    .fullName label, .line1 label, .line2 label, .country label, .province label, .city label, .zipCode label, .phone label {
        font-size: smaller;
        line-height: 1rem;
        text-transform: capitalize;
        letter-spacing: .05em;
        display: block;
        text-align: left;
        font-family: serif;
        color: white;
    }
    .fullName input, .line1 input, .line2 input, .country select, .province select, .city select, .zipCode input, .phone input , .address_action button{
        font-family: serif;
        font-size: medium;
        line-height: 1rem;
        border: 1px solid #eee;
        background-color: #eee;
        color: #4c4c4b;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        border-radius: 2%;
        width: 100%;
        -webkit-appearance: none;
        height: 25px;
        margin: 2px;
    }
    .fullName input:focus, .line1 input:focus, .line2 input:focus, .country select:focus, .province select:focus, .city select:focus, .zipCode input:focus, .phone input:focus {
        border: 1px solid gray;
        outline: none;
    }
    .city, .province, .phone, .zipCode, .address_action {
        width: 50%;
        float: left;
    }
    .address_action, .address_action button {
        width: 100%;
        text-transform: capitalize;
        outline: none;
        cursor: pointer;
        margin-top: 2%;
    }
    .address_action span {
        color: red;
    }
</style>