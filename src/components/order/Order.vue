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
                <div style="float:left; width: 100%; margin: 5% 0">
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
                <!-- 支付信息 -->
                <div style="float:left; width: 100%; margin: 5% 0">
                    <nav class="level">
                        <div class="level-item has-text-centered">
                        </div>
                        <div class="level-item has-text-centered"></div>
                        <div class="level-item has-text-centered"></div>
                    </nav>
                    <div class="order_credit">
                        <v-braintree :authorization="brainTree.authorization"
                                     :locale="brainTree.locale"
                                     :paypal="brainTree.paypal"
                                     btnText=""
                                     btnClass="pay_btn"
                                     @success="PaySuccess"
                                     @error="PayError">
                        </v-braintree>
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
                        <b-button type="is-dark" size="is-small" expanded @click="CreateOrder" style="letter-spacing: 0.1em">{{languages.Cart.pay[language]}}</b-button>
                    </li>
                </ul>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header  from '../common/Header'
    import Footer  from '../common/Footer'
    import Address from '../account/Address'

    export default {
        name: "Order",
        components: {
            Header,
            Footer,
        },
        data() {
            return {
                brainTree: {
                    authorization: "eyJ2ZXJzaW9uIjoyLCJhdXRob3JpemF0aW9uRmluZ2VycHJpbnQiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpGVXpJMU5pSXNJbXRwWkNJNklqSXdNVGd3TkRJMk1UWXRjMkZ1WkdKdmVDSXNJbWx6Y3lJNklrRjFkR2g1SW4wLmV5SmxlSEFpT2pFMU9EUTBNekkzTXprc0ltcDBhU0k2SWpCaE1XTXhaR0l5TFRSbU9USXROR1l3T1MxaU1XWmxMV05oWm1Sa04yVTNaVEUyTmlJc0luTjFZaUk2SWpNMFpqaHJNbVJ0Y25remFHTnpPVzBpTENKcGMzTWlPaUpCZFhSb2VTSXNJbTFsY21Ob1lXNTBJanA3SW5CMVlteHBZMTlwWkNJNklqTTBaamhyTW1SdGNua3phR056T1cwaUxDSjJaWEpwWm5sZlkyRnlaRjlpZVY5a1pXWmhkV3gwSWpwMGNuVmxmU3dpY21sbmFIUnpJanBiSW0xaGJtRm5aVjkyWVhWc2RDSmRMQ0p2Y0hScGIyNXpJanA3SW0xbGNtTm9ZVzUwWDJGalkyOTFiblJmYVdRaU9pSXpOR1k0YXpKa2JYSjVNMmhqY3psdEluMTkucWJOdHVUWHNocUNkdXQ3dXd5Y2xzd3dGeTRVeDNycVZaRTJ5a3REOEdadmZ5NHV5dnh6SExwXzJjUWlObFBUN2htNkdXUUM5VEp6Z0RfU3RkR2J6aEEiLCJjb25maWdVcmwiOiJodHRwczovL2FwaS5zYW5kYm94LmJyYWludHJlZWdhdGV3YXkuY29tOjQ0My9tZXJjaGFudHMvMzRmOGsyZG1yeTNoY3M5bS9jbGllbnRfYXBpL3YxL2NvbmZpZ3VyYXRpb24iLCJncmFwaFFMIjp7InVybCI6Imh0dHBzOi8vcGF5bWVudHMuc2FuZGJveC5icmFpbnRyZWUtYXBpLmNvbS9ncmFwaHFsIiwiZGF0ZSI6IjIwMTgtMDUtMDgifSwiY2hhbGxlbmdlcyI6W10sImVudmlyb25tZW50Ijoic2FuZGJveCIsImNsaWVudEFwaVVybCI6Imh0dHBzOi8vYXBpLnNhbmRib3guYnJhaW50cmVlZ2F0ZXdheS5jb206NDQzL21lcmNoYW50cy8zNGY4azJkbXJ5M2hjczltL2NsaWVudF9hcGkiLCJhc3NldHNVcmwiOiJodHRwczovL2Fzc2V0cy5icmFpbnRyZWVnYXRld2F5LmNvbSIsImF1dGhVcmwiOiJodHRwczovL2F1dGgudmVubW8uc2FuZGJveC5icmFpbnRyZWVnYXRld2F5LmNvbSIsImFuYWx5dGljcyI6eyJ1cmwiOiJodHRwczovL29yaWdpbi1hbmFseXRpY3Mtc2FuZC5zYW5kYm94LmJyYWludHJlZS1hcGkuY29tLzM0ZjhrMmRtcnkzaGNzOW0ifSwidGhyZWVEU2VjdXJlRW5hYmxlZCI6dHJ1ZSwicGF5cGFsRW5hYmxlZCI6dHJ1ZSwicGF5cGFsIjp7ImRpc3BsYXlOYW1lIjoic2hvd3UiLCJjbGllbnRJZCI6bnVsbCwicHJpdmFjeVVybCI6Imh0dHA6Ly9leGFtcGxlLmNvbS9wcCIsInVzZXJBZ3JlZW1lbnRVcmwiOiJodHRwOi8vZXhhbXBsZS5jb20vdG9zIiwiYmFzZVVybCI6Imh0dHBzOi8vYXNzZXRzLmJyYWludHJlZWdhdGV3YXkuY29tIiwiYXNzZXRzVXJsIjoiaHR0cHM6Ly9jaGVja291dC5wYXlwYWwuY29tIiwiZGlyZWN0QmFzZVVybCI6bnVsbCwiYWxsb3dIdHRwIjp0cnVlLCJlbnZpcm9ubWVudE5vTmV0d29yayI6dHJ1ZSwiZW52aXJvbm1lbnQiOiJvZmZsaW5lIiwidW52ZXR0ZWRNZXJjaGFudCI6ZmFsc2UsImJyYWludHJlZUNsaWVudElkIjoibWFzdGVyY2xpZW50MyIsImJpbGxpbmdBZ3JlZW1lbnRzRW5hYmxlZCI6dHJ1ZSwibWVyY2hhbnRBY2NvdW50SWQiOiJzaG93dSIsImN1cnJlbmN5SXNvQ29kZSI6IlVTRCJ9LCJtZXJjaGFudElkIjoiMzRmOGsyZG1yeTNoY3M5bSIsInZlbm1vIjoib2ZmIiwibWVyY2hhbnRBY2NvdW50SWQiOiIzNGY4azJkbXJ5M2hjczltIn0=",
                    locale: "zh_CN",
                    paypal: {
                        flow: "vault",
                    }
                },
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
                credit: {
                    total: 1,
                    selected: 0,
                    items: [],
                },
                carts: {
                    items: [],
                    selected: 0,
                    total: 0,
                },
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
                //TODO 查询支付方式
                this.QueryCreditCard();
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
                if (this.credit.selected < 0 || this.credit.selected >= this.credit.items.length) {
                    return
                }
                const header = {
                    "x-language": this.language,
                };
                const body = {};
                body.address = this.address.items[this.address.selected];
                body.pay     = this.credit.items[this.credit.selected];
                body.stocks  = this.carts.items;
                body.goodsCount = this.carts.total;
                body.subTotal   = this.goodsPrice;
                body.total      = this.totalPrice;
                body.shipping   = this.shippingPrice;
                body.tax        = this.taxPrice;
                let data = await this.$api.CreateOrder(header, body);
                console.log(data);
            },
            computePrice() {
                this.goodsPrice = 0.0;
                this.shippingPrice = 0.0;
                this.taxPrice = 0.0;
                this.totalPrice = 0.0;
                console.log(this.carts);
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
            PaySuccess(payload) {
                console.log(payload);
            },
            PayError(error) {
                console.log(error)
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
            async QueryCreditCard() {
                const header = {
                    "x-language": this.language,
                };
                const params = {};
                let data = await this.$api.QueryCreditCard(header, params) || {};
                if (data.hasOwnProperty("code")) {
                    console.log(data);
                } else {
                    this.credit.total = data.total;
                    this.credit.items = data.items;
                    for (let i = 0; i < this.credit.items.length; i++) {
                        if (this.credit.items[i].isDefault) {
                            this.credit.selected = i;
                            this.step = 3;
                            break;
                        } else {
                            this.credit.selected = -1;
                        }
                    }
                    this.credit.total++;
                    this.credit.items.push({number:"9999999999999999", bin: "paypal"})
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
        margin-top: 5%;
    }
    .order_info {
        width: 67%;
        padding-left: 10%;
        border-right: 1px solid black;
    }
    .order_summary {
        width: 33%;
        padding-left: 1%;
        padding-top: 4%;
        text-align: center;
        padding-right: 10%;
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
    .order_credit {
        float: left;
        margin: 1%;
        width: 98%;
        height: auto;
        border: none;
        background: white;
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
    .pay_btn {
        display: none;
    }
</style>