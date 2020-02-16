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
                            <span>
                                <button style="cursor: pointer; border: none; margin: 0 10px" type="button">
                                    <span class="mdi mdi-account-plus"></span>
                                </button>
                            </span>
                        </div>
                        <div class="level-item has-text-centered">
                        </div>
                    </nav>
                    <div class="order_address" v-for="(item, index) in address.items" :key="index">
                        <ul>
                            <li>
                                <span>
                                     <label><input v-model="address.selected" type="radio" checked :value="index"></label>
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
                            <li><span class="order_address_info"><b>{{item.people}}</b></span></li>
                            <li><span class="order_address_info">{{item.email}}</span></li>
                            <li><span class="order_address_info">{{item.phone}}</span></li>
                            <li>
                                <span style="font-size: 0.1rem;margin: 0 3px" class="order_address_info">{{item.country}}</span>
                                <span style="font-size: 0.1rem;margin: 0 3px" class="order_address_info">{{item.province}}</span>
                                <span style="font-size: 0.1rem;margin: 0 3px" class="order_address_info">{{item.city}}</span>
                            </li>
                            <li>
                                <span style="font-size: 0.1rem" class="order_address_info">{{item.area}}</span>
                                <span style="font-size: 0.1rem" class="order_address_info">{{item.street}}</span>
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- 支付信息 -->
                <div style="float:left; width: 100%; margin: 5% 0">
                    <nav class="level">
                        <div class="level-item has-text-centered">
                        </div>
                        <div class="level-item has-text-centered">
                            <span>
                                <img style="height: 20px" src="http://i76.imgup.net/accepted_c22e0.png">
                            </span>
                            <span>
                                <button style="cursor: pointer; border: none; margin: 0 10px" type="button">
                                    <span class="mdi mdi-credit-card-plus"></span>
                                </button>
                            </span>
                        </div>
                        <div class="level-item has-text-centered">
                        </div>
                    </nav>
                    <div class="order_credit" v-for="(item, index) in credit.items" :key="index">
                        <ul>
                            <li>
                                <span style="float: right; margin: 5px;cursor: pointer;">
                                    <button  type="button">
                                        <span class="mdi mdi-delete"></span>
                                    </button>
                                </span>
                                <span style="float: right; margin: 5px;cursor: pointer;">
                                    <button  type="button">
                                        <span class="mdi mdi-account-edit"></span>
                                    </button>
                                </span>
                                <span style="float: right; margin: 5px;">
                                     <label><input v-model="credit.selected" type="radio" checked :value="index"></label>
                                </span>
                            </li>
                            <li><Credit :card="item"/></li>
                        </ul>
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
                                                <b-numberinput v-model="item.count" style="width: 20%; float: left" type="is-light" min=1 size="is-small" controls-position="compact" @input="UpdateCartItem(index)"></b-numberinput>
                                                <p style="float: right; line-height: 1.5rem; margin-right: 5%">{{languages.Country[language]}}{{item.count * item.goodsPrice}}</p>
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

            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'
    import Credit from './Credit'

    export default {
        name: "Order",
        components: {
            Header,
            Footer,
            Credit
        },
        data() {
            return {
                api: this.$api,
                languages: this.$languages,
                language: "chinese",
                hasNavigation: false,
                step: 0,
                address: {
                    total: 1,
                    selected: 0,
                    items: [
                        {
                            people: "richard ",
                            country: "中国",
                            province: "shanghai",
                            city: "上海",
                            area: "浦东新区",
                            street: "栖霞路20#201",
                            email: "richard@test.com",
                            phone:"+86 17621620657"
                        },
                        {
                            people: "richard richard richard",
                            country: "中国",
                            province: "shanghai",
                            city: "上海",
                            area: "浦东新区",
                            street: "栖霞路20#201 栖霞路20#201 栖霞路20#201",
                            email: "richard@test.com",
                            phone:"+86 17621620657"
                        }
                    ]
                },
                credit: {
                    total: 0,
                    selected: 1,
                    items: [
                        {
                            logo: "v",
                            number: "0000111122223333",
                            month: "01",
                            year: "22",
                            yourName: "kai yan chen",
                        },
                        {
                            logo: "v",
                            number: "0000111122223333",
                            month: "01",
                            year: "22",
                            yourName: "sun he"
                        },
                    ],
                },
                carts: {
                    items: [],
                    total: 0,
                },
            }
        },
        created() {
            //获取购物车数据
            this.$bus.$on(this.$utils.Singles.SingleOfPushCart, (data) => {
                this.carts = data;
            });
        },
        beforeDestroy() {
            this.$bus.$off(this.$utils.Singles.SingleOfPushCart);
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
        width: 63%;
        padding-left: 10%;
        border-right: 1px solid black;
    }
    .order_summary {
        width: 37%;
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
        height: auto;
        border: 1px solid gray;
        float: left;
        padding: 0 10px;
        margin: 0 5px;
    }
    .order_address_info {
        font-family: serif;
        font-size: 1rem;
        line-height: 1rem;
    }
    .level-item {
        border: 1px solid;
    }
    .order_credit {
        float: left;
        margin: 5px;
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
</style>