<template>
    <div class="credit_card">
        <ul>
            <li class="credit_logo">
                <img v-if="card.logo.length > 0" :src="url" alt="logos"/>
            </li>
            <li class="credit_number">
                <label>
                    <input v-model="card.number" type="text" name="credit_number" minlength="13" maxlength="16" readonly="readonly" disabled="disabled"/>
                </label>
            </li>
            <li class="credit_expire">
                 <div style="float: right;margin: 0 5%;text-align: center;">
                     <div style="font-size: 0.1rem;color: darkgray;">Month/Year</div>
                     <div style="font-size: 1rem;">{{this.card.month}}/{{this.card.year}}</div>
                 </div>
            </li>
            <li class="credit_your_name">
                <span v-if="card.yourName.length > 0">{{this.card.yourName}}</span>
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
                this.card.logo = "";
                if (this.card.number.length <= 0) {
                    return
                }
                let bin = this.card.number[0];
                let bin2 = "";
                switch (bin) {
                    case "4":  //visa  4
                        this.card.logo = "visa";
                        break;
                    case "5":  //mastercard 5|2
                        this.card.logo = "mastercard";
                        break;
                    case "2":  //mastercard 5|2
                        this.card.logo = "mastercard";
                        break;
                    case "6": //Discover  6
                        this.card.logo = "discover";
                        break;
                    case "3":
                        if (this.card.number.length <= 1) {
                            return
                        }
                        bin2 = this.card.number[1];
                        switch (bin2) {
                            case "7": //American Express 37
                                this.card.logo = "American_Express";
                                break;
                            case "5": //JCB 35
                                this.card.logo = "JCB";
                                break;
                            default:
                                return
                        }
                        break;
                    default:
                        return
                }
                this.url = this.image + this.card.logo.toLowerCase() + ".png";
            },
        }
    }
</script>

<style scoped>
    .credit_card {
        height: 150px;
        width: 237px;
        border-radius: 0;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_logo, .credit_number, .credit_expire, .credit_your_name {
        height: 40px;
        width: 100%;
        font-family: serif;
        padding: 2%;
    }
    .credit_your_name {
        height: 30px;
        padding: 0 20px;
        font-size: 1rem;
        text-transform: capitalize;
        position: relative;
        top: -20px;
    }
    .credit_logo > img {
        margin: 4px;
    }
    .credit_number input {
        width: 100%;
        height: 100%;
        border: none;
        font-size: medium;
        letter-spacing: 5px;
        text-align: center;
        background: rgb(128, 128, 128);
        color: white;
    }
    .credit_expire {
        padding: 5px 0;
        text-transform: capitalize;
    }
</style>