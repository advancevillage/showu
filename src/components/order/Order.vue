<template>
    <div>
        <Header :nav="1"/>
        <div id="container">
            <div class="order_info">
                <span class="order_back" @click="back"><em></em>{{languages.Order.back[language]}}</span>
                <b-steps  v-model="step" :has-navigation="hasNavigation">
                    <b-step-item size="is-small" type="is-dark" :label="languages.Order.account[language]" icon="account-key"></b-step-item>
                    <b-step-item size="is-small" type="is-dark" :label="languages.Order.address[language]" icon="home"></b-step-item>
                    <b-step-item size="is-small" type="is-dark" :label="languages.Order.credit[language]" icon="credit-card"></b-step-item>
                    <b-step-item size="is-small" type="is-dark" :label="languages.Order.shipping[language]" icon="package-variant"></b-step-item>
                </b-steps>
                <!-- 收货地址 -->
                <div style="float:left; width: 100%; margin: 5% 0 0">
                    <nav class="level">
                        <div class="level-item has-text-centered">
                        </div>
                        <div class="level-item has-text-centered">
                        </div>
                        <div class="level-item has-text-centered">
                        </div>
                    </nav>
                    <div class="order_address" v-for="(item, index) in address.items" :key="index">
                        <ul>
                            <li>
                                <span>
                                     <label><input v-model="address.selected" type="radio" checked :value="index" @click="SelectAddress(index)"></label>
                                </span>
                                <span>
                                    <button style="float: right; padding: 0; margin: 8px 2px 0;cursor: pointer;" type="button">
                                        <span class="mdi mdi-delete"></span>
                                    </button>
                                </span>
                                <span>
                                    <button style="float: right; padding: 0; margin: 8px 2px 0;cursor: pointer;" type="button">
                                        <span class="mdi mdi-account-edit"></span>
                                    </button>
                                </span>
                            </li>
                            <li><span class="order_address_info"><b>{{item.fullName}}</b></span></li>
                            <li><span class="order_address_info">{{item.phone}}</span></li>
                            <li>
                                <span style="font-size: 0.1rem; display: block" class="order_address_info">{{item.line1}}</span>
                                <span style="font-size: 0.1rem; display: block" class="order_address_info">{{item.line2}}</span>
                            </li>
                            <li>
                                <span style="font-size: 0.1rem;" class="order_address_info">{{item.city}}</span>
                                <span style="font-size: 0.1rem;" class="order_address_info">{{item.province}}</span>
                                <span style="font-size: 0.1rem;" class="order_address_info">{{item.country}}</span>
                            </li>
                        </ul>
                    </div>
                    <div class="order_address">
                        <button type="button" @click="OpenAddressModal">
                            <span class="mdi mdi-map-marker"></span>
                        </button>
                    </div>
                </div>
                <!-- 商品列表 -->
                <div style="float:left; width: 100%; margin: 5% 0;">
                    <nav class="level">
                        <div class="level-item has-text-centered">
                        </div>
                        <div class="level-item has-text-centered">
                            <span class="mdi mdi-cart-outline"></span>
                        </div>
                        <div class="level-item has-text-centered">
                        </div>
                    </nav>
                    <div class="cart-items" v-for="(item, index) in carts.items" :key="index">
                        <div class="card">
                            <div class="card-content">
                                <div class="media">
                                    <div class="media-left">
                                        <figure>
                                            <img style="width: 64px; height: 64px;" :src="api.QueryImageUrl(item.frontImage)" alt="Placeholder image">
                                        </figure>
                                    </div>
                                    <div class="media-content">
                                        <ul>
                                            <li style="float: right; line-height: 0.5rem; color: rgb(192,192,192); cursor: pointer;"><b-icon icon="close" @click.native="DeleteCartItem(index)"></b-icon></li>
                                            <li>{{item.goodsName[language]}}</li>
                                            <li>{{item.colorName[language]}}/{{item.sizeValue}}</li>
                                            <li>
                                                <b-numberinput v-model="item.total" style="width: 20%; float: left" type="is-light" min=1 size="is-small" controls-position="compact" @input="UpdateCartItem(index)"></b-numberinput>
                                                <p style="float: right; line-height: 1.5rem; margin-right: 5%">{{languages.Country[language]}}{{item.total * item.goodsPrice}}</p>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="order_summary">
                <ul>
                    <li style="font-weight: bolder">{{languages.Cart.summary[language]}}</li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.goods[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{goodsPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.shipping[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{shippingPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.tax[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{taxPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.total[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{totalPrice}}</span></li>
                    <li style="line-height: 0">
                        <span style="background: white; width: 100%; height: 2px; display: inline-block"></span>
                    </li>
                    <li style="cursor: pointer">

                    </li>
                </ul>
                <Pay v-on:selectPay="selectPay"></Pay>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header  from '../common/Header'
    import Footer  from '../common/Footer'
    import Address from '../account/Address'
    import Pay     from '../pay/Pay'

    export default {
        name: "Order",
        components: {
            Header,
            Footer,
            Pay,
        },
        data() {
            return {
                api: this.$api,
                languages: this.$languages,
                language: "chinese",
                hasNavigation: false,
                step: 0,
                address: {
                    total: 0,
                    selected: 0,
                    items: []
                },
                carts: {
                    items: [],
                    selected: 0,
                    total: 0,
                },
                pay: {},
                goodsPrice: 0.0,
                shippingPrice: 0.0,
                taxPrice: 0.0,
                totalPrice: 0.0,
                login: false,
            }
        },
        created() {
            //获取购物车数据
            this.$bus.$on(this.$utils.Singles.SingleOfPushCart, (data) => {
                this.carts = data;
                this.computePrice();
            });

            this.$bus.$on(this.$utils.Singles.SingleOfLogin, (login) => {
                this.login = login;
            });

        },
        mounted() {
            if (this.login) {
                this.step = 1;
                //TODO 获取订单页Token
                this.CreateOrderToken();
                //TODO 查询收货地址
                this.QueryAddress();
            } else {
                this.$bus.$emit(this.$utils.Singles.SingleOfOpenLogin);
            }
        },
        beforeDestroy() {
            this.$bus.$off(this.$utils.Singles.SingleOfPushCart);
            this.$bus.$off(this.$utils.Singles.SingleOfLogin);
        },
        methods: {
            back() {
                this.$router.push({path: '/cart'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            },
            DeleteCartItem(index) {
                this.$bus.$emit(this.$utils.Singles.SingleOfDeleteCart, index);
            },
            UpdateCartItem(index) {
                this.$bus.$emit(this.$utils.Singles.SingleOfUpdateCart, index);
            },
            async CreateOrder() {
                if (this.address.selected < 0 || this.address.selected >= this.address.items.length) {
                    return
                }
                const header = {
                    "x-language": this.language,
                };
                const body = {};
                body.address = this.address.items[this.address.selected];
                body.stocks  = this.carts.items;
                body.goodsCount = this.carts.total;
                body.subTotal   = this.goodsPrice;
                body.total      = this.totalPrice;
                body.shipping   = this.shippingPrice;
                body.tax        = this.taxPrice;
                body.pay        = this.pay;
                await this.$api.CreateOrder(header, body);
                this.$router.push({path: '/account?href=order'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            },
            computePrice() {
                this.goodsPrice = 0.0;
                this.shippingPrice = 0.0;
                this.taxPrice = 0.0;
                this.totalPrice = 0.0;
                for (let i = 0; i < this.carts.items.length; i++) {
                    this.goodsPrice +=  this.carts.items[i].total * this.carts.items[i].goodsPrice
                }
                this.totalPrice = this.goodsPrice + this.shippingPrice + this.taxPrice
            },
            OpenAddressModal() {
                this.$buefy.modal.open({
                    props: {
                        language: this.language
                    },
                    parent: this,
                    component: Address,
                    hasModalCard: true,
                    trapFocus: true,
                    scroll: "keep",
                    events: {}
                });
            },
            SelectAddress(index) {
                this.address.selected = index;
                this.step = this.step < 2 ? 2 : this.step;
            },
            selectPay(payInfo) {
                this.pay = payInfo;
                this.CreateOrder();
            },
            async QueryAddress() {
                const header = {
                    "x-language": this.language,
                };
                const params = {};
                let data = await this.$api.QueryAddress(header, params) || {};
                if (data.hasOwnProperty("code")) {
                    console.log(data);
                } else {
                    this.address.total = data.total;
                    this.address.items = data.items;
                    for (let i = 0; i < this.address.items.length; i++) {
                        if (this.address.items[i].isDefault) {
                            this.address.selected = i;
                            this.step = 2;
                            break;
                        } else {
                            this.address.selected = -1;
                        }
                    }
                }
            },
            async CreateOrderToken() {
                const header = {
                    "x-language": this.language,
                };
                const body = {};
                await this.$api.CreateOrderToken(header, body);
            }
        }

    }
</script>

<style scoped>
    .order_info, .order_summary {
        height: 100%;
        float: left;
        min-height: 740px;
        margin-top: 3%;
    }
    .order_info {
        width: 67%;
        padding-left: 3%;
        border-right: 1px solid black;
    }
    .order_summary {
        width: 33%;
        padding-left: 1%;
        padding-top: 1%;
        text-align: center;
        padding-right: 3%;
        position: fixed;
        top: 0;
        z-index: 0;
        right: 0;
    }
    .order_back {
        border-bottom: 1px solid black;
        width: 100%;
        display: block;
        line-height: 1.5rem;
        cursor: pointer;
        font-size: small;
        font-family: serif;
        font-weight: bolder;
        margin-bottom: 5%;
    }
    .order_back > em {
        border: 5px solid white;
        border-right: 10px solid black;
        width: 0;
        height: 0;
        font-size: 0;
        margin-right: 5px;
        position: relative;
        top: -4px;
        left: 0;
    }
    .order_address {
        width:  auto;
        height: 150px;
        border: none;
        float: left;
        margin: 5px;
        min-width: 150px;
    }
    .order_address > button {
        min-width: 150px;
        cursor: pointer;
        height: 100%;
        width: 100%;
        outline: none;
    }
    .order_address ul {
        padding: 3%;
        border: 1px solid gray;
        height: 100%;
    }
    .order_address_info {
        font-family: serif;
        font-size: 1rem;
        line-height: 1rem;
        letter-spacing: 1px;
    }
    .level-item {
        border: 1px solid;
    }
    .order_credit > button {
        min-width: 100%;
        height: 100%;
        cursor: pointer;
        outline: none;
    }
    .card-content {
        padding: 0;
    }
    .cart-items {
        margin: 1%;
    }
    .media-content li {
        font-size: 0.1rem;
        font-family: serif;
        text-transform: capitalize;
        word-spacing: 5px;
    }
    .order_summary ul li {
        background: rgb(64,64,64);
        color: white;
        line-height: 2.5rem;
        font-size: small;
        font-family: serif;
    }
    .level-item span button:focus {
        outline: none;
    }
</style>