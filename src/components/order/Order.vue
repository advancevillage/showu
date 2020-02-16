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
                                <img src="http://i76.imgup.net/accepted_c22e0.png">
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

                    </div>
                </div>
                <!-- 商品列表 -->
                <div style="float:left; width: 100%; margin: 5% 0">

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

    export default {
        name: "Order",
        components: {
            Header,
            Footer
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
                    items: [
                        {},
                        {}
                    ],
                }
            }
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
        width: 60%;
        padding-left: 10%;
    }
    .order_summary {
        width: 40%;
        border-left: 1px solid black;
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
        width: 200px;
    }
</style>