<template>
    <div class="ss_summary" v-bind:style="{width: width + 'px'}">
        <ul>
            <li class="ss_summary_title">{{languages.NOUN.SUMMARY[language]}}</li>
            <li class="ss_summary_detail" v-for="(item, index) in items" :key="index">
                <span class="ss_summary_detail_label">{{item.label}}</span>
                <span class="ss_summary_detail_price">{{item.symbol + item.value}}</span>
            </li>
        </ul>
        <Pay :width="width" :height="height" @selectPay="pay"/>
    </div>
</template>

<script>
    import Pay from "./Pay";

    export default {
        name: "Summary",
        components: {
            Pay
        },
        props: {
            language: {
                type: String,
                required: false,
                default: "en"
            },
            width: {
                type: Number,
                required: false,
                default: 300
            },
            height: {
                type: Number,
                required: false,
                default: 200
            }
        },
        data() {
            return {
                languages: this.$languages,
                items: [
                    {label: "11", value: 0.99, symbol: "$"},
                    {label: "11", value: 0.99, symbol: "$"},
                    {label: "11", value: 0.99, symbol: "$"},
                ]
            }
        },
        methods: {
            pay(payInfo) {
                console.log(payInfo)
            }
        }
    }
</script>

<style scoped>
    .ss_summary {
        color: white;
        width: 100%;
    }
    .ss_summary > ul {
        background: #404040;
    }
    .ss_summary_detail, .ss_summary_title {
        width: 100%;
        display: inline-block;
        padding: 1% 5%;
        text-align: center;
        color: #fff;
        line-height: 2.5rem;
        font-size: x-large;
        font-family: monospace;
        letter-spacing: 2px;
    }
    .ss_summary_detail_label, .ss_summary_detail_price{
        display: inline-block;
        float: left;
        font-size: medium;
    }
    .ss_summary_detail_price {
        float: right;
    }
</style>