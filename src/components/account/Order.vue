<template>
    <div>
        <!-- 订单详情页 -->
        <div v-if="sn.length">
            <a href="/account?href=order" style="margin: 0;padding: 0;"><span class="order_back"><em></em>{{languages.Order.backDetail[language]}}</span></a>
            <div v-if="order.hasOwnProperty('id')" class="order_detail">
                <div class="order_detail_list" v-for="i in 3" :key=i>
                    <ul v-if="i === 1">
                        <!-- 订单信息 -->
                        <li><span class="column">{{languages.Order.id[language]}}</span><span>{{order.id}}</span></li>
                        <li><span class="column">{{languages.Order.state[language]}}</span>
                            <span :class="order.nextState">{{languages.State[order.nextState][language]}}</span>
                        </li>
                        <li><span class="column">{{languages.Order.orderTime[language]}}</span><span>{{moment.unix(order.orderTime).format(format)}}</span></li>
                        <li><span class="column">{{languages.Order.goodsCount[language]}}</span><span>{{order.goodsCount}}</span></li>
                        <li><span class="column">{{languages.Order.shipMoney[language]}}</span><span>{{order.shipping}}</span></li>
                        <li><span class="column">{{languages.Order.taxMoney[language]}}</span><span>{{order.tax}}</span></li>
                        <li><span class="column">{{languages.Order.payMoney[language]}}</span><span>{{order.total}}</span></li>
                        <li>
                            <span class="column"></span>
                            <button v-if="!goPay" v-on:click="goPay = true">{{languages.Cart.pay[language]}}</button>
                        </li>
                    </ul>
                    <ul v-else-if="i === 2">
                        <!-- 支付信息 -->
                        <li><span class="column">{{languages.Order.payMethod[language]}}</span><span>{{order.pay.type}}</span></li>
                        <li><span class="column"></span><span><img style="height: 25px;" :src="queryCreditCardLogo(order.pay.details.cardType)"/></span></li>
                        <li><span class="column">{{languages.Order.cardNumber[language]}}</span><span>{{order.pay.details.bin + "******" + order.pay.details.lastFour}}</span></li>
                    </ul>
                    <ul v-else-if="i === 3">
                        <!-- 物流信息 -->
                        <li><span class="column">{{languages.Order.address[language]}}</span><span>{{ order.address.fullName}}</span></li>
                        <li v-if="order.address.line1.length > 0"><span class="column"></span><span>{{ order.address.line1}}</span></li>
                        <li v-if="order.address.line2.length > 0"><span class="column"></span><span>{{ order.address.line2}}</span></li>
                        <li><span class="column"></span><span>{{ order.address.city}}&nbsp;&nbsp;{{ order.address.province}}&nbsp;&nbsp;{{ order.address.country}}</span></li>
                        <li><span class="column"></span><span>{{ order.address.phone}}</span></li>
                        <li><span class="column"></span><span>{{ order.address.zipCode}}</span></li>
                    </ul>
                    <ul v-else></ul>
                </div>
            </div>
            <div v-if="order.hasOwnProperty('id') && goPay" class="pay_plugin">
                <Pay v-on:selectPay="selectPay"></Pay>
            </div>
            <div v-if="order.hasOwnProperty('id')" class="goods_detail">
                <div class="cart-items" v-for="(item, index) in order.stocks" :key="index">
                    <div class="card">
                        <div class="card-image">
                            <figure>
                                <img style="width: 312px; height: 418px;" :src="api.QueryImageUrl(item.frontImage)" alt="Placeholder image">
                            </figure>
                        </div>
                        <div class="content">
                            <ul>
                                <li>111</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- 订单列表页 -->
        <div v-else>
            <b-table :data="orders.items" class="order" hoverable striped :selected.sync="selected">
                <template slot-scope="props">
                    <b-table-column :label="languages.Order.goodsList[language]" centered width="60">
                        <img style="margin: 0 2px; height: 30px" v-for="(item,index) in props.row.stocks" :key=index :src="api.QueryImageUrl(item.frontImage)"/>
                    </b-table-column>
                    <b-table-column :label="languages.Order.id[language]" centered width="40">
                        <a style="border: none; font-weight: bolder; color: black" :href="'/account?href=order&sn=' + props.row.id">{{ props.row.id }}</a>
                    </b-table-column>
                    <b-table-column :label="languages.Order.state[language]" centered width="40">
                        {{ languages.State[props.row.nextState][language] }}
                    </b-table-column>
                    <b-table-column :label="languages.Order.payMoney[language]" centered width="40">
                        {{ props.row.total }}
                    </b-table-column>
                    <b-table-column :label="languages.Order.payMethod[language]" centered width="40">
                        <span><img style="height: 20px;" :src="queryCreditCardLogo(props.row.pay.details.cardType)"/></span>
                    </b-table-column>
                    <b-table-column :label="languages.Order.address[language]" centered width="40">
                        <span style="text-align: left">{{ props.row.address.line1}}&nbsp;&nbsp;</span>
                        <span style="text-align: left">{{ props.row.address.city}}&nbsp;&nbsp;</span>
                        <span style="text-align: left">{{ props.row.address.province}}&nbsp;&nbsp;</span>
                        <span style="text-align: left">{{ props.row.address.country}}</span>
                    </b-table-column>
                    <b-table-column :label="languages.Order.goodsCount[language]" centered width="40">
                        {{ props.row.goodsCount }}
                    </b-table-column>
                    <b-table-column :label="languages.Order.orderTime[language]" centered width="40">
                        {{moment.unix(props.row.orderTime).format(format)}}
                    </b-table-column>
                    <b-table-column :label="languages.Order.actions[language]" centered width="40">
                        <span>{{ props.row.orderId }}</span>
                        <span>{{ props.row.orderId }}</span>
                        <span>{{ props.row.orderId }}</span>
                    </b-table-column>
                </template>
            </b-table>
        </div>
    </div>
</template>

<script>
    import Pay  from '../pay/Pay'
    export default {
        name: "Order",
        props: {
           sn: {
               type: String,
               required: false,
               default: ""
           }
        },
        components: {
            Pay,
        },
        mounted() {
            if (this.sn.length <= 0 ) {
                this.QueryOrder();
            } else {
                this.QueryOneOrder(this.sn);
            }
        },
        data() {
            return {
                api: this.$api,
                languages: this.$languages,
                moment: this.$moment,
                language: "chinese",
                format: "YYYY-MM-DD HH:mm:ss",
                selected: {},
                orders: {
                    items: [],
                    total: 0,
                },
                order: {},
                goPay: false,
            }
        },
        methods: {
            async QueryOrder() {
                const params = {
                    "page": 0,
                    "perPage": 999,
                };
                const headers = {
                    "x-language": this.language,
                };
                this.orders = await this.$api.QueryOrder(headers, params) || {items: [], total: 0};
            },
            async QueryOneOrder(sn) {
                const params = {};
                const headers = {
                    "x-language": this.language,
                };
                this.order = await this.$api.QueryOneOrder(sn, headers, params) || {};
                console.log(this.order);
            },
            queryCreditCardLogo(card) {
                let url = "";
                switch (card.toLowerCase()) {
                    case "visa":
                        url = "https://www.braintreepayments.com/images/visa-logo.svg";
                    break;
                    case "mastercard":
                        url = "https://www.braintreepayments.com/images/mastercard-logo.svg";
                        break;
                    case "jcb":
                        url = "https://www.braintreepayments.com/images/jcb-logo.svg"
                        break;
                    case "discover":
                        url = "https://www.braintreepayments.com/images/discover-logo.svg"
                        break;
                    case "maestro":
                        url = "https://www.braintreepayments.com/images/maestro-logo.svg"
                        break;
                    case "american express":
                        url = "https://www.braintreepayments.com/images/amex-logo.svg"
                        break;
                    case "unionpay":
                        url = "https://www.braintreepayments.com/images/unionpay-logo.svg"
                        break;
                    default:
                        url = card
                        break;
                }
                return url;
            },
            selectPay(payInfo) {
                console.log(payInfo);
            },
        }
    }
</script>

<style scoped>
    .order {
        font-family: serif;
        line-height: 1rem;
        font-size: small;

    }
    .order_detail, .goods_detail, .pay_plugin {
        width: 100%;
        height: auto;
        float: left;
        border-top: 1px solid black;
        margin-bottom: 2%;
        padding-top: 2%;
        padding-bottom: 2%;
        display: block;
    }
    .order_detail_list{
        width: 33%;
        height: 100%;
        float: left;
        font-size: smaller;
    }
    .order_detail_list ul{
        display: block;
        border: none;
    }
    .order_detail_list ul li {
        height: 25px;
    }
    .column, .order_detail_list ul li span {
        text-align: right;
        display: inline-block;
        width: 30%;
        font-size: smaller;
    }
    .order_detail_list ul li button {
        font-family: serif;
        background: #000000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: xx-small;
        height: 25px;
        outline: none;
        margin: 5% 10% 0;
        width: auto;
        min-width: 30px;
        padding: 0 2%;
    }
    .order_detail_list ul li button:hover{
        background: #1524d9;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        color: white;
    }
    .pending_ship {
        color: orange;
        font-weight: bolder;
    }
    .pending_pay {
        color: red;
        font-weight: bolder;
    }
    .card-content {
        padding: 0;
    }
    .cart-items {
        float: left;
        margin: 0 1%;
        width: 31%;
    }
    .order_back {
        width: 100%;
        display: block;
        line-height: 1.5rem;
        cursor: pointer;
        font-size: small;
        font-family: serif;
        font-weight: bolder;
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
</style>