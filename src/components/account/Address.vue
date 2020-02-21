<template>
    <div class="modal-card">
        <!-- 收货人 -->
        <div class="fullName">
            <label>{{this.languages.Address.fullName[this.language]}}</label>
            <input type="text"/>
        </div>
        <!-- 国家 -->
        <div class="country">
            <label>{{this.languages.Address.country[this.language]}}</label>
            <select>
                <option></option>
            </select>
        </div>
        <div class="line1">
            <label>{{this.languages.Address.line1[this.language]}}</label>
            <input type="text"/>
        </div>
        <div class="line2">
            <label>{{this.languages.Address.line2[this.language]}}</label>
            <input type="text"/>
        </div>
        <div class="city">
            <label>{{this.languages.Address.city[this.language]}}</label>
            <select>
                <option></option>
            </select>
        </div>
        <div class="province">
            <label>{{this.languages.Address.province[this.language]}}</label>
            <select>
                <option></option>
            </select>
        </div>
        <div class="zipCode">
            <label>{{this.languages.Address.zipCode[this.language]}}</label>
            <input type="text"/>
        </div>
        <div class="phone">
            <label>{{this.languages.Address.phone[this.language]}}</label>
            <input type="text"/>
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
                    fullName: ""
                }
            }
        }
    }
</script>

<style scoped>
    .modal-card {
        width: 400px;
        height: auto;
        /*flex-direction: column;*/
        background: rgb(192,192,192);
        display: block;
    }
    .fullName, .line1, .line2, .country, .city, .province, .phone, .zipCode {
        padding: 2% 5% 0;
        margin: 0;
        width: 100%;
    }
    .fullName label, .line1 label, .line2 label, .country label, .province label, .city label, .zipCode label, .phone label {
        font-size: smaller;
        line-height: 1rem;
        text-transform: uppercase;
        letter-spacing: .05em;
        display: block;
        text-align: left;
        font-family: serif;
    }
    .fullName input, .line1 input, .line2 input, .country select, .province select, .city select, .zipCode input, .phone input{
        font-family: serif;
        font-size: small;
        line-height: 1rem;
        border: 1px solid #dfe0e1;
        background-color: #fff;
        color: #4c4c4b;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        width: 100%;
        -webkit-appearance: none;
        border-radius: 5%;
        height: 25px;
        margin: 2px;
    }
    .fullName input:focus, .line1 input:focus, .line2 input:focus, .country select:focus, .province select:focus, .city select:focus, .zipCode input:focus, .phone input:focus {
        border: 1px solid black;
        outline-width: inherit;
    }
    .city, .province, .phone, .zipCode {
        width: 50%;
        float: left;
    }
</style>