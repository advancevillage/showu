<template>
    <div>
        <Header/>
        <div id="container">

            <div class="cart_list">
                <span class="cart_back" @click="back"><em></em>{{languages.Cart.back[language]}}</span>
                <div class="cart-items" v-for="(item, index) in carts.items" :key="index">
                    <div class="card">
                        <div class="card-content">
                            <div class="media">
                                <div class="media-left">
                                    <figure>
                                        <img style="width: 128px; height: 128px;" :src="api.QueryImageUrl(item.frontImage)" alt="Placeholder image">
                                    </figure>
                                </div>
                                <div class="media-content">
                                    <ul>
                                        <li style="float: right; line-height: 1rem; color: rgb(192,192,192); cursor: pointer;"><b-icon icon="close" @click.native="DeleteCartItem(index)"></b-icon></li>
                                        <li>{{item.goodsName[language]}}</li>
                                        <li>{{item.colorName[language]}}</li>
                                        <li>{{item.sizeValue}}</li>
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
            <div class="cart_summary">
                <ul>
                    <li style="font-weight: bolder">{{languages.Cart.summary[language]}}</li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.goods[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{goodsPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.shipping[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{shippingPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.tax[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{taxPrice}}</span></li>
                    <li><span style="text-align: left;float: left; width: 80%; padding-left: 5%">{{languages.Cart.total[language]}}</span><span style="float: right; width: 20%">{{languages.Country[language]}}{{totalPrice}}</span></li>
                    <li style="line-height: 0">
                        <span style="background: white; width: 100%; height: 30px; display: inline-block"></span>
                    </li>
                    <li>
                        <b-button type="is-dark" size="is-small" expanded>{{languages.Cart.checkout[language]}}</b-button>
                    </li>
                </ul>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'

    export default {
        name: "Cart",
        components: {
            Header,
            Footer
        },
        created() {
            //获取购物车数据
            this.$bus.$on(this.$utils.Singles.SingleOfPushCart, (data) => {
                this.carts = data;
            });
        },
        mounted() {},
        beforeDestroy() {
            this.$bus.$off(this.$utils.Singles.SingleOfPushCart);
        },
        data() {
            return {
                carts: {
                    items: [],
                    total: 0,
                },
                api: this.$api,
                languages: this.$languages,
                language: "chinese",
                totalPrice: 0,   //最后结算总价
                goodsPrice: 0,   //商品求和
                shippingPrice: 0,//运费
                taxPrice: 0,     //税费
            }
        },
        methods: {
            DeleteCartItem(index) {
                this.$bus.$emit(this.$utils.Singles.SingleOfDeleteCart, index);
            },
            UpdateCartItem(index) {
                this.$bus.$emit(this.$utils.Singles.SingleOfUpdateCart, index);
            },
            back() {
                this.$router.push({path: '/'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            }
        }
    }
</script>

<style scoped>
    .cart_list,  .cart_summary {
        height: 100%;
        float: left;
        min-height: 740px;
        margin-top: 5%;
    }
    .cart_list {
        width: 60%;
        padding-left: 10%;
    }
    .cart_back {
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
    .cart_back > em {
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
    .card-content {
        padding: 1rem;
    }
    .media-content {
        font-family: serif;
    }
    .cart_summary {
        width: 40%;
        padding-left: 1%;
        padding-top: 4%;
        text-align: center;
        padding-right: 20%;
        position: fixed;
        top: 0;
        z-index: -1;
        right: 0;
    }
    .cart_summary ul li {
        background: rgb(64,64,64);
        color: white;
        line-height: 2.5rem;
        font-size: small;
        font-family: serif;
    }
    .cart_summary > ul > li {
        margin: 0 1%;
    }
</style>


