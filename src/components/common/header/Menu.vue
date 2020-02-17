<template>
    <div>
        <nav class="first-level-category"
             v-bind:class="{'first-level-category-hover': flagMenu > 0 }"
             v-on:mouseenter="flagMenu = 1"
             v-on:mouseleave="flagMenu = nav">
            <!-- 导航栏 -->
            <div class="category" v-for="(item, index) in categories.items" :key="index"
                 v-on:mouseenter="EnterCategories(index)"
                 v-on:mouseleave="flagCategory=-1">
                {{item.name[language]}}
                <em v-if="flagCategory === index"></em>
            </div>

            <div class="account-info">
                <!-- login in状态 -->
                <div v-if="login" class="button">
                    <b-icon icon="account-card-details" size="is-small"></b-icon>
                </div>
                <!-- 登出状态 -->
                <div v-else class="button" v-on:click="OpenLogin">
                    <b-icon icon="account" size="is-small"></b-icon>
                </div>
                <div class="button" v-bind:class="{'rock': rock}"
                     v-on:mouseenter="flagCartDetail=1"
                     v-on:mouseleave="flagCartDetail=-1">
                    {{carts.total}}
                    <svg style="position: absolute; top: -7px; left: -5px; z-index: -1;" version="1.1" x="0px" y="0px" width="40px" height="40px" viewBox="0 0 40 40">
                        <g>
                            <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M6.588,19.992c0,1.434-1.159,2.594-2.589,2.594"></path>
                            <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d="M16.456,13.569c0-2.507,2.029-4.54,4.531-4.54c2.503,0,4.532,2.033,4.532,4.54"></path>
                            <path stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" d=" M16.605,13.591h-3.403c-3.652,0-6.614,2.966-6.614,6.626v6.355l-0.614,2.967c0,0.791,0.64,1.433,1.429,1.433h27.166 c0.791,0,1.431-0.642,1.431-1.433l-0.614-3.171v-6.151c0-3.66-2.962-6.626-6.614-6.626h-3.253"></path>
                            <line stroke-width="1.5" fill="#ffffff" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10" x1="21.936" y1="13.591" x2="16.457" y2="13.591"></line>
                        </g>
                    </svg>
                </div>
            </div>
        </nav>
        <div class="category-children"
             v-if="flagMenu >= 0 && flagCategory >= 0"
             v-on:mouseleave="flagMenu=nav; flagCategory=-1; flagCategoryDetail=-1"
             v-on:mouseenter="EnterChildCategories"
             >
            <div class="child-categories">
                <ul>
                    <li style="font-size: 0.8rem;">
                        <a :href="api.CreateListLink(categories.items[flagCategory].name, categories.items[flagCategory].id)">{{categories.items[flagCategory].name[language]}}</a>
                    </li>
                    <li v-for="(item, index) in this.children" :key="index">
                        <a :href="api.CreateListLink(item.name, item.id)">{{item.name[language]}}</a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="cart"
             v-if="flagMenu >= 0 && flagCartDetail >= 0"
             v-on:mouseenter="flagMenu=1,  flagCartDetail=1"
             v-on:mouseleave="flagMenu=nav,flagCartDetail=-1">
            <div v-if="carts.total <= 0" class="cart-header">
                <b-icon icon="cart-arrow-down"></b-icon>
                <p>{{languages.Cart.empty[language]}}</p>
            </div>
            <div v-else class="cart-context">
                <div class="cart-items" v-for="(item, index) in carts.items" :key="index">
                    <div class="card">
                        <div class="card-content">
                        <div class="media">
                            <div class="media-left">
                                <figure>
                                    <img style="width: 96px; height: 96px;" :src="api.QueryImageUrl(item.frontImage)" alt="Placeholder image">
                                </figure>
                            </div>
                            <div class="media-content">
                                <ul>
                                    <li style="float: right; line-height: 1rem; color: rgb(192,192,192); cursor: pointer;"><b-icon icon="close" @click.native="DeleteCartItem(index)"></b-icon></li>
                                    <li>{{item.goodsName[language]}}</li>
                                    <li>{{item.colorName[language]}}</li>
                                    <li>{{item.sizeValue}}</li>
                                    <li>
                                        <b-numberinput v-model="item.count" style="width: 50%; float: left" type="is-light" min=1 size="is-small" controls-position="compact" @input="UpdateCartItem(index)"></b-numberinput>
                                        <p style="float: right; line-height: 1.5rem; margin-right: 5%">{{languages.Country[language]}}{{item.count * item.goodsPrice}}</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>

            <div class="cart-footer">
                <b-button class="checkout"  type="is-dark" size="is-small" @click="RedirectCartPage" style="letter-spacing: 1rem">{{languages.Cart.commit[language]}}</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    import Login from './Login'

    export default {
        name: "Menu",
        props: {
            nav: {
                type: Number,
                required: true,
            },
            language: {
                type: String,
                required: true,
            },
        },
        created() {
            this.flagMenu = this.nav;
        },
        mounted() {
            this.CartRefresh();
            this.QueryCategories();

            this.$bus.$on(this.$utils.Singles.SingleOfAddCart,  (data) => {
                if (this.login) {
                    this.LoginAddCart(data);
                } else {
                    this.UnLoginAddCart(data);
                }
            });

            //删除购物车中商品
            this.$bus.$on(this.$utils.Singles.SingleOfDeleteCart,  (index) => {
                this.DeleteCartItem(index);
            });
            //更改购物车中商品
            this.$bus.$on(this.$utils.Singles.SingleOfUpdateCart,  (index) => {
                this.UpdateCartItem(index);
            });

            //事件触发登录弹框
            this.$bus.$on(this.$utils.Singles.SingleOfOpenLogin, () => {
                this.OpenLogin();
            });
        },
        beforeDestroy() {
            this.$bus.$off(this.$utils.Singles.SingleOfAddCart);
            this.$bus.$off(this.$utils.Singles.SingleOfDeleteCart);
            this.$bus.$off(this.$utils.Singles.SingleOfUpdateCart);
        },
        data() {
            return {
                languages: this.$languages,
                flagMenu: -1,
                flagCategory: -1,
                flagCategoryDetail: -1,
                flagCartDetail: -1,
                login: false,
                categories: {
                    total: 0,
                    items: []
                },
                children: [],
                api: this.$api,
                carts: {
                    total: 0,
                    items: []
                },
                rock: false
            }
        },
        methods: {
            OpenLogin() {
                this.$buefy.modal.open({
                    props: {
                        language: this.language
                    },
                    parent: this,
                    component: Login,
                    hasModalCard: true,
                    trapFocus: true,
                    scroll: "keep",
                    events: {
                        triggerQueryLogin: this.CartRefresh
                    }
                });
            },
            QueryCategories: async function() {
                const params = {
                    level: 1
                };
                const headers = {
                   "x-language": this.language
                };
                this.categories = await this.$api.QueryCategories(params, headers) || {total: 0, items:[]}
            },
            QueryChildCategories: async function(cid) {
                const headers = {
                    "x-language": this.language
                };
                const params = {};
                this.children = [];
                this.children = await this.$api.QueryChildCategories(cid, params, headers) || [];
            },
            EnterCategories(index) {
                this.flagCategory = index;
                this.flagCategoryDetail = index;
                this.QueryChildCategories(this.categories.items[this.flagCategory].id);
            },
            EnterChildCategories() {
                this.flagMenu = 1;
                this.flagCategory= this.flagCategoryDetail;
            },
            RedirectCartPage() {
                this.$router.push({path: '/order'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(0);
                    });
            },
            CartRefresh() {
                this.login = this.$utils.QueryLogin().length > 0;
                this.$bus.$emit(this.$utils.Singles.SingleOfLogin, this.login);
                if (this.login) {
                    //合并购物车
                    this.carts.items = this.$utils.QueryCart();
                    for (let i = 0; i < this.carts.items.length; i++ ) {
                        this.LoginAddCart(this.carts.items[i])
                    }
                    this.$utils.DeleteCart();
                    this.QueryCarts();
                } else {
                    this.carts.items = this.$utils.QueryCart();
                }
                this.QueryCartTotal();
            },
            QueryCartTotal() {
                this.carts.total = 0;
                for (let i = 0; i < this.carts.items.length; i++ ) {
                    this.carts.total += this.carts.items[i].count;
                }
                this.animation();
                //push carts data
                this.$bus.$emit(this.$utils.Singles.SingleOfPushCart, {items: this.carts.items, total: this.carts.total});
            },
            DeleteCartItem(index) {
                if (index < 0 || index >= this.carts.items.length) {
                    return
                }
                if (this.login) {
                    this.DeleteCarts(index);
                } else {
                    this.carts.items.splice(index, 1);
                    this.$utils.UpdateCart(this.carts.items);
                    this.QueryCartTotal();
                }
            },
            UpdateCartItem(index) {
                if (index < 0 || index >= this.carts.items.length) {
                    return
                }
                if (this.login) {
                    this.UpdateCarts(index);
                } else {
                    this.$utils.UpdateCart(this.carts.items);
                    this.QueryCartTotal();
                }
            },
            UnLoginAddCart(data) {
                let i = 0;
                for (i = 0; i < this.carts.items.length; i++) {
                    if (data.goodsId === this.carts.items[i].goodsId && data.sizeId === this.carts.items[i].sizeId && data.colorId === this.carts.items[i].colorId) {
                        this.carts.items[i].count += data.count;
                        break
                    } else {
                        continue
                    }
                }
                if ( i >= this.carts.items.length) {
                    this.carts.items.push(data);
                }
                this.QueryCartTotal();
                this.$utils.UpdateCart(this.carts.items);
            },
            async LoginAddCart(data) {
                const headers = {
                    "x-language": this.language
                };
                const body = data || {};
                data = await this.$api.CreateCarts(headers, body);
                this.QueryCarts();
            },
            async QueryCarts() {
                const params = {};
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryCarts(headers, params);
                if (data.hasOwnProperty("code")) {
                    this.$utils.DeleteLogin();
                    this.CartRefresh();
                } else {
                    this.carts = data || {total: 0, items: []};
                    this.QueryCartTotal();
                }
            },
            async UpdateCarts(index) {
                if (index < 0 || index > this.carts.items.length) {
                    return
                }
                const headers = {
                    "x-language": this.language,
                };
                const body = this.carts.items[index];
                await this.$api.UpdateCart(body.id, headers, body);
                this.QueryCarts();
            },
            async DeleteCarts(index) {
                if (index < 0 || index > this.carts.items.length) {
                    return
                }
                const headers = {
                    "x-language": this.language,
                };
                const params = {};
                await this.$api.DeleteCart(this.carts.items[index].id, headers, params);
                this.QueryCarts();
            },
            animation() {
                let timeout = 8;
                let clock = window.setInterval( () => {
                    if (timeout < 1) {
                        window.clearInterval(clock);
                        this.rock = false;
                    } else {
                        timeout--;
                        this.rock = true;
                    }
                }, 50)
            }
        }
    }
</script>

<style scoped>
    .first-level-category, .category-children {
        width: 100%;
        padding: 0 2%;
        background-color: rgba(192, 192, 192, 0);
        z-index: 25;
        height: 40px;
    }
    .first-level-category-hover {
        background-color: rgba(192, 192, 192, 1);
    }
    .category {
        line-height: 2.5rem;
        margin: 0 5px;
        padding: 0;
        color: white;
        display: block;
        float: left;
        position: relative;
        font-family: serif;
    }
    .category > em {
        width: 0;
        height: 0;
        font-size: 0;
        opacity: 1;
        border: 4px solid rgb(192, 192, 192);
        border-bottom: 8px solid white;
        position: absolute;
        left: 45%;
        top: 30px;
    }
    .category:hover {
        color: black;
    }
    .category-children {
        position: absolute;
        height: 240px;
        border-top: 2px solid white;
        background-color: rgba(160, 160, 160, 0.9);
        top: 40px;
    }
    .child-categories {
        margin: 10px 0;
    }
    .child-categories ul li {
        width: 100px;
        text-align: left;
        font-size: 0.5rem;
        margin: 5px 0;
        color: black;
        text-decoration: underline;
    }
    .account-info, .account-info > .button {
        float: right;
        background-color: rgba(192,192,192,0);
        border: none;
        padding: 0;
        margin: 1px 5px;
        color: white;
    }
    .account-info > .button {
        float: left;
        width: 30px;
        height: 30px;
        margin: 5px;
        padding: 2px;
        color: black;
        border-radius: 100%;
        font-family: serif;
        font-size: inherit;
        z-index: 5;
    }
    .cart {
        width: 20%;
        z-index: 30;
        position: absolute;
        right: 0;
        height: auto;
        border-top: 2px solid white;
    }
    .cart-header, .cart-footer, .cart-context, .cart-items {
        width: 100%;
        background-color: rgba(192, 192, 192, 0.8);
        text-align: center;
    }
    .cart-context {
        max-height: 600px;
        overflow: auto;
    }
    .cart-header {
        color: white;
        padding: 10% 0;
        font-family: serif;
        height: 100px;
    }
    .cart-footer, .checkout {
        width: 100%;
        height: 2rem;
    }
    .card-content {
        margin: 0;
        padding: 0;
    }
    .media-content li {
        font-size: smaller;
    }
    .rock {
        display: inline-block;
        background-size: 100% 100%;
        animation-name: rock;
        transform-origin: center bottom;
        animation-duration: 1s;
        animation-fill-mode: both;
        animation-iteration-count: infinite;
        animation-delay: 0s;
    }

    @keyframes rock {
        0% {
            transform: rotate(0deg);
            transition-timing-function: cubic-bezier(0.215, .61, .355, 1)
        }

        10% {
            transform: rotate(-12deg);
            transition-timing-function: cubic-bezier(0.215, .61, .355, 1)
        }

        20% {
            transform: rotate(12deg);
            transition-timing-function: cubic-bezier(0.215, .61, .355, 1)
        }

        28% {
            transform: rotate(-10deg);
            transition-timing-function: cubic-bezier(0.215, .61, .355, 1)
        }

        36% {
            transform: rotate(10deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        42% {
            transform: rotate(-8deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        48% {
            transform: rotate(8deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        52% {
            transform: rotate(-4deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        56% {
            transform: rotate(4deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        60% {
            transform: rotate(0deg);
            transition-timing-function: cubic-bezier(0.755, .5, .855, .06)
        }

        100% {
            transform: rotate(0deg);
            transition-timing-function: cubic-bezier(0.215, .61, .355, 1)
        }
    }
</style>