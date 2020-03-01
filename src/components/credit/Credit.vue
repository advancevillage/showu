<template>
    <div class="credit_card">
        <ul v-if="card.bin !== 'paypal'">
            <li class="credit_logo">
                <img v-if="card.bin.length > 0" :src="url" alt="logos"/>
            </li>
            <li class="credit_number">
                <label>
                    <input v-model="card.number" type="text" name="credit_number" minlength="13" maxlength="16" readonly="readonly" disabled="disabled"/>
                </label>
            </li>
            <li class="credit_expire">
                 <div style="float: right;margin: 0 5%;text-align: center;">
                     <div style="font-size: 0.1rem;color: darkgray;">Month/Year</div>
                     <div style="font-size: 1rem;">{{this.card.expire}}</div>
                 </div>
            </li>
        </ul>
        <ul v-if="card.bin === 'paypal'">
            <li class="credit_logo">
                <img v-if="card.bin.length > 0" :src="url" alt="logos"/>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Credit",
        props: {
            card: {
                type: Object,
                required: true,
            }
        },
        data() {
            return {
                image: "https://assets.braintreegateway.com/payment_method_logo/",
                height: 32,
                url: "",
            }
        },
        mounted() {
            this.$bus.$on(this.$utils.Singles.SingleOfQueryCreditLogo, () => {
                this.CreateCreditLogo();
            });
            this.CreateCreditLogo();
        },
        methods: {
            CreateCreditLogo() {
                //https://developers.braintreepayments.com/guides/credit-cards/testing-go-live/php
                this.card.bin = "";
                if (this.card.number.length <= 0) {
                    return
                }
                let bin = this.card.number[0];
                let bin2 = "";
                switch (bin) {
                    case "4":  //visa  4
                        this.card.bin = "visa";
                        break;
                    case "5":  //mastercard 5|2
                        this.card.bin = "mastercard";
                        break;
                    case "2":  //mastercard 5|2
                        this.card.bin = "mastercard";
                        break;
                    case "6": //Discover  6
                        this.card.bin = "discover";
                        break;
                    case "3":
                        if (this.card.number.length <= 1) {
                            return
                        }
                        bin2 = this.card.number[1];
                        switch (bin2) {
                            case "7": //American Express 37
                                this.card.bin = "American_Express";
                                break;
                            case "5": //JCB 35
                                this.card.bin = "JCB";
                                break;
                            default:
                                return
                        }
                        break;
                    case "9":
                        this.card.bin = "paypal";
                        break;
                    default:
                        return
                }
                this.url = this.image + this.card.bin.toLowerCase() + ".png";
            },
        }
    }
</script>

<style scoped>
    .credit_card {
        width: 150px;
        height: 150px;
        border-radius: 0;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_logo, .credit_number, .credit_expire {
        width: 100%;
        font-family: serif;
        padding: 2%;
    }
    .credit_logo > img {
        margin: 4px;
    }
    .credit_number input {
        width: 100%;
        height: 100%;
        border: none;
        font-size: medium;
        letter-spacing: 2px;
        text-align: center;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_expire {
        padding: 5px 0;
        text-transform: capitalize;
    }
</style>