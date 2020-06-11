<template>
    <div class="ss_pay" v-bind:style="{width: width + 'px'}">
        <div id="drop-in-container"></div>
        <button v-if="paymentOption === 'card'" id="btn-pay" @click.prevent="Purchase">{{this.languages.Order.credit[this.language]}}</button>
    </div>
</template>

<script>
    import BrainTree from 'braintree-web-drop-in'

    export default {
        name: "Pay",
        props: {
            width: {
                type: Number,
                required: false,
                default: 300,
            },
            height: {
                type: Number,
                required: false,
                default: 200,
            }
        },
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
                payInfo: {},
                isLoading: true,
                isFullPage: false
            }
        },
        mounted() {
            this.PreLoading(8);
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
            },
            PreLoading(second) {
                this.isLoading = true
                setTimeout(() => {
                    this.isLoading = false
                }, second * 1000)
            }
        }
    }
</script>

<style scoped>
    .ss_pay {
        height: auto;
        overflow: hidden;
    }
    #drop-in-container {
        margin: 0;
        padding: 0;
    }
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
    .load_warp {
        z-index: 3;
        position: absolute;
        width: 100%;
        background: white;
        height: 180px;
        margin: 0;
        padding: 0;
    }
    .loading {
        zoom: 3;
        animation:circle 1.5s infinite linear;
    }
    @-webkit-keyframes circle{
        0%{ transform:rotate(0deg); }
        100%{ transform:rotate(360deg); }
    }
</style>