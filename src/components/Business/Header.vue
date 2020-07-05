<template>
    <div class="ss_header" v-bind:style="[scroll > height ? {position: 'fixed'}:{}]">
        <Notice :items="notices" :countries="countries" :language="language" :width="width" :height="height/3" @getLanguage="getLanguage"></Notice>
        <Menu :categories="categories" :users="users" :carts="carts" :width="width" :height="2 * height/3" :language="language" :currency="currency" :opacity="opacity" :userClickFn="userLogin" @getCart="getCart"/>
    </div>
</template>

<script>
    import Notice from "./Notice";
    import Menu   from "./Menu";
    import Login  from "./Login";

    export default {
        name: "Header",
        components: {
            Notice,
            Menu,
        },
        props: {
            width: {
                type: Number,
                required: true,
            },
            height: {
                type: Number,
                required: true,
            },
            opacity: {
                type: Boolean,
                required: false,
                default: true
            }
        },
        mounted() {
            this.QueryNotices();
            this.QueryCountries();
            this.QueryCategories();
            this.QueryCarts();

            this.$bus.$on(this.$utils.SIG.AddCart, this.CreateCarts);
            window.addEventListener('scroll', this.fixedHeader, true)
        },
        beforeDestroy() {
            window.removeEventListener('scroll', this.fixedHeader,true);
        },
        data() {
            return {
                languages: this.$languages,
                notices: [],
                countries: [],
                categories: [],
                users: [
                    { value: this.$languages.NOUN.ACCOUNT, link: "/account"},
                    { value: this.$languages.NOUN.ORDER, link: "/orders"},
                    { value: this.$utils.HasLogin() ? this.$languages.OPERATE.LOGOUT : this.$languages.OPERATE.LOGIN,
                      fn: this.$utils.HasLogin() ? this.userLogout : this.userLogin,
                    },
                ],
                carts: [],
                language: "en",
                currency: "$",
                scroll: 0
            }
        },
        methods: {
            async QueryNotices() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryNotices(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.notices = response.data.items;
                }
            },
            async QueryCountries() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCountries(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response)
                } else {
                    this.countries = response.data.items;
                }
            },
            async QueryCategories() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCategories(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(this.response);
                } else {
                    this.categories = response.data.items;
                }
            },
            QueryCarts() {
                return this.$utils.HasLogin() ? this.queryCartsLogin() : this.queryCartsLogout();
            },
            async queryCartsLogin() {
                const params = {};
                const headers = {};
                let response = await this.$api.QueryCarts(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(this.response);
                } else {
                    this.carts = response.data.items;
                }
            },
            queryCartsLogout() {
                this.carts = this.$utils.QueryCart();
            },
            CreateCarts(goods) {
                return this.$utils.HasLogin() ? this.createCartsLogin(goods) : this.createCartLogout(goods);
            },
            async createCartsLogin(goods) {
                console.log(goods);
            },
            createCartLogout(goods) {
                let snapshot = {};
                snapshot.imageUrl      = goods.imageUrl;
                snapshot.name          = goods.name;
                snapshot.stateImageUrl = goods.stateImageUrl; //活动图片链接
                snapshot.color         = goods.colors[goods.colorSelected];
                snapshot.size          = goods.sizes[goods.sizeSelected];
                snapshot.state         = goods.state;
                snapshot.price         = goods.price;
                snapshot.count         = 1;
                snapshot.id            = goods.id;
                snapshot.addCartTime   = this.$moment(Date.now()).format('X') //Unix Timestamp
                snapshot.updateTime    = this.$moment(Date.now()).format('X') //Unix Timestamp

                //合并购物车商品
                let i = 0;
                for (; i < this.carts.length; i++) {
                    let g = this.carts[i];
                    if (
                        g.id === snapshot.id &&
                        g.size === snapshot.size &&
                        g.color.rgb === snapshot.color.rgb
                    ) {
                        g.count++;
                        break
                    }
                }
                if (i >= this.carts.length) {
                    this.carts.push(snapshot);
                }
                this.$utils.UpdateCart(this.carts);
                this.carts = this.$utils.QueryCart() || [];
            },
            //多语言事件触发
            getLanguage(data) {
                this.language = data.language;
                this.currency = data.currency;
                this.$emit('getLanguage', this.language);
                this.$emit('getObject', data);
            },
            getCart() {
                this.$utils.UpdateCart(this.carts);
            },
            fixedHeader() {
                this.scroll = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
            },
            userLogin(data) {
                if (this.$utils.HasLogin()) {
                    //TODO 已登陆
                    console.log(data)
                } else {
                    let config = {};
                    config.props  = {
                        language: this.language,
                    };
                    config.component = Login;
                    config.parent = this;
                    config.hasModalCard = true;
                    config.trapFocus = true;
                    config.scroll  = "keep";
                    config.events  = {};
                    this.$buefy.modal.open(config)
                }
            },
            userLogout(data) {
                console.log(data);
                this.$utils.Logout();
            },
        }
    }
</script>

<style scoped>
    .ss_header {
        z-index: 5;
    }
</style>