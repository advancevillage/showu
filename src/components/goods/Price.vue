<template>
    <div>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.purchase[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="1" v-model="purchase" @on-change="ComputePrice"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.price[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" v-model="price"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.newIn[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="newIn"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.sale[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="sale"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.clearance[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="clearance"></InputNumber>
            </i-col>
        </Row>
    </div>
</template>

<script>
    export default {
        name: "Price",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                languages: this.$languages,
                // language: "chinese",
                purchase: 1,            // 进价
                price: 1,               // 售价
                newIn: 1,               // 上新价
                sale: 1,                // 促销价
                clearance: 1,           // 清仓价
                expired: 1,
            }
        },
        mounted() {
            this.ComputePrice();
        },
        methods: {
            ComputePrice() {
                this.price = this.purchase + this.purchase * this.expired;
                this.newIn = this.purchase + 0.75 * this.purchase * this.expired;
                this.sale  = this.purchase + 0.50 * this.purchase * this.expired;
                this.clearance  = this.purchase + 0.20 * this.purchase * this.expired;
            }
        }
    }
</script>

<style scoped>

</style>