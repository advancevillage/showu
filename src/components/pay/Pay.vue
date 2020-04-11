<template>
    <div>
        <div id="drop-in-container"></div>
        <button v-if="paymentOption === 'card'" id="btn-pay" @click.prevent="Purchase">{{this.languages.Order.credit[this.language]}}</button>
    </div>
</template>

<script>
    import BrainTree from 'braintree-web-drop-in'

    export default {
        name: "Pay",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                instance: {},
                authorization: "",
                locale: "zh_CN",
                paypal: {
                    flow: "vault"
                },
                paymentOption: "",
                payInfo: {}
            }
        },
        mounted() {
            this.CreatePayToken();
        },
        methods: {
            Purchase() {
                let _this = this;
                _this.instance.requestPaymentMethod({}, function (err, payload) {
                    if (err) {
                        console.error(err);
                    } else {
                        _this.payInfo = payload;
                        _this.$emit("selectPay", _this.payInfo)
                    }
                });
            },
            async CreatePayToken() {
                const headers = {
                    "x-language": this.language,
                };
                const body = {};
                this.authorization = await this.$api.CreatePayToken(headers, body);
                this.CreateBrainTree();
            },
            CreateBrainTree() {
                let _this = this;
                BrainTree.create({authorization: this.authorization, selector: "#drop-in-container", paypal: this.paypal})
                    .then(instance => {
                        instance.on('paymentOptionSelected', function(option) {
                            _this.paymentOption = option.paymentOption;
                        });
                        this.instance = instance;
                    })
                    .catch(err => {
                        console.error(err);
                    })
            }
        }
    }
</script>

<style scoped>
    #btn-pay {
        background: #000000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: 0.875rem;
        width: 100%;
        height: 2rem;
        letter-spacing: 1rem;
        outline: none;
    }
    #btn-pay:hover {
        background: #1524d9;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        color:white;
    }
</style>