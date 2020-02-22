<template>
    <div class="modal-card">
        <div class="credit_card">
            <Credit :card="card"/>
        </div>
        <div class="credit_number">
            <label>{{this.languages.Credit.number[this.language].toLowerCase()}}</label>
            <input v-model="card.number" v-bind:style="[numberErr ? {borderColor: 'red'}:{borderColor: 'gray'}]" type="text" placeholder="0000000000000000" maxlength="16" @input="CheckoutNumber"/>
        </div>
        <div class="credit_expire">
            <label>{{this.languages.Credit.expire[this.language].toLowerCase()}}</label>
            <input v-model="card.expire" v-bind:style="[expireErr ? {borderColor: 'red'}:{borderColor: 'gray'}]" type="text" placeholder="MM/YY" minlength="5" maxlength="5" @input="CheckoutExpire"/>
        </div>
        <div class="credit_security">
            <label>{{this.languages.Credit.security[this.language].toLowerCase()}}</label>
            <input v-model="card.cvv" v-bind:style="[securityErr ? {borderColor: 'red'}:{borderColor: 'gray'}]" type="text" placeholder="567" minlength="3" maxlength="3" @input="CheckoutSecurity"/>
        </div>
        <div class="credit_action">
            <button type="button">{{this.languages.Credit.create[this.language].toLowerCase()}}</button>
        </div>
    </div>
</template>

<script>
    import Credit from './Credit'

    export default {
        name: "Create",
        components: {
            Credit,
        },
        props: {
            language: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                languages: this.$languages,
                card: {
                    logo: "",
                    number: "",
                    month: "",
                    year: "",
                    cvv: "",
                    yourName: "",
                    expire: ""
                },
                numberErr: false,
                securityErr: false,
                expireErr: false,
            }
        },
        methods: {
            CheckoutNumber() {
                this.numberErr = false;
                for (let i = 0; i < this.card.number.length; i++) {
                    if (this.card.number[i] < '0' || this.card.number[i] > '9') {
                        this.numberErr = true;
                        break
                    }
                }
                this.$bus.$emit(this.$utils.Singles.SingleOfQueryCreditLogo)
            },
            CheckoutSecurity() {
                this.securityErr = false;
                for (let i = 0; i < this.card.cvv.length; i++) {
                    if (this.card.cvv[i] < '0' || this.card.cvv[i] > '9') {
                        this.securityErr = true;
                        break
                    }
                }
            },
            CheckoutExpire() {
                this.expireErr = false;
                for (let i = 0; i < this.card.expire.length; i++) {
                    switch (i) {
                        case 0:
                        case 1:
                            if (this.card.expire[i] < '0' || this.card.expire[i] > '9') {
                                this.expireErr = true;
                            }
                            break;
                        case 2:
                            if (this.card.expire[i] !== '/') {
                                this.expireErr = true;
                            }
                            this.card.month = this.card.expire.substr(0, 2);
                            switch (this.card.month) {
                                case "01":
                                case "02":
                                case "03":
                                case "04":
                                case "05":
                                case "06":
                                case "07":
                                case "08":
                                case "09":
                                case "10":
                                case "11":
                                case "12":
                                    this.expireErr = false;
                                    break;
                                default:
                                    this.expireErr = true;
                            }
                            break;
                        case 3:
                        case 4:
                            if (this.card.expire[i] < '0' || this.card.expire[i] > '9') {
                                this.expireErr = true;
                            }
                            this.card.year = this.card.expire.substr(3, 2);
                            break;
                        default:
                            this.expireErr = true;
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .modal-card {
        width: 300px;
        height: auto;
        background: rgb(192,192,192);
        display: block;
    }
    .credit_card {
        width: 100%;
    }
    .credit_number label, .credit_security label, .credit_expire label {
        font-size: smaller;
        line-height: 1.5rem;
        display: block;
        text-align: left;
        font-family: serif;
        text-transform: capitalize;
    }
    .credit_number input, .credit_security input, .credit_expire input{
        font-family: serif;
        font-size: medium;
        line-height: 1rem;
        border: 1px solid gray;
        background-color: #fff;
        color: black;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        width: 100%;
        letter-spacing: 0.1em;
        -webkit-appearance: none;
        border-radius: 5%;
        height: 25px;
        margin: 2px;
    }
    .credit_number input:focus, .credit_security input:focus, .credit_expire input:focus {
        outline-width: 0;
        border: 1px solid rgb(192,192,192);
    }
    .credit_number, .credit_security, .credit_expire, .credit_action {
        float: left;
        margin: 5px;
        padding: 0 1%;
        width: 94%;
    }
    .credit_security, .credit_expire {
        width: 45%;
    }
    .credit_action button {
        width: 100%;
        height: 25px;
        margin: 1% 0 0;
        text-transform: capitalize;
    }
</style>