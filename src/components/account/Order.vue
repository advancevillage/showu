<template>
    <div>
        <!-- 订单详情页 -->
        <div v-if="sn.length">

        </div>
        <!-- 订单列表页 -->
        <div v-else>
            <b-table :data="orders.items" class="order" hoverable striped :selected.sync="selected">
                <template slot-scope="props">

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
                        <span v-if="props.row.pay.details.cardType.toLowerCase()      === 'visa'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/visa-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'mastercard'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/mastercard-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'jcb'"><img src="https://www.braintreepayments.com/images/jcb-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'discover'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/discover-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'maestro'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/maestro-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'american express'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/amex-logo.svg"/></span>
                        <span v-else-if="props.row.pay.details.cardType.toLowerCase() === 'unionpay'"><img style="height: 20px;" src="https://www.braintreepayments.com/images/unionpay-logo.svg"/></span>
                        <span v-else>{{props.row.pay.details.cardType}}</span>
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
    export default {
        name: "Order",
        props: {
           sn: {
               type: String,
               required: false,
               default: ""
           }
        },
        mounted() {
            this.QueryOrder();
        },
        data() {
            return {
                languages: this.$languages,
                moment: this.$moment,
                language: "chinese",
                format: "YYYY-MM-DD HH:mm:ss",
                selected: {},
                orders: {
                    items: [],
                    total: 0,
                }
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
                console.log(this.orders);
            }
        }
    }
</script>

<style scoped>
    .order {
        font-family: serif;
        line-height: 1rem;
        font-size: small;

    }
</style>