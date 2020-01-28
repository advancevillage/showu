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
                <InputNumber size="small" :min="purchase" v-model="price" @on-blur="Emit"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.newIn[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="newIn" @on-blur="Emit"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.sale[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="sale" @on-blur="Emit"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Price.clearance[language]}}</i-col>
            <i-col span="4">
                <InputNumber size="small" :min="purchase" :max="price" v-model="clearance" @on-blur="Emit"></InputNumber>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="4">{{languages.Cycle[language]}}</i-col>
            <i-col span="3">
                <i-select size="small" v-model="selected" @on-change="Emit">
                    <i-option v-for="(item, index) in cycle" :value="index" :key="index" :label="languages.Cycle[item.key][language]"></i-option>
                </i-select>
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
                cycle: [
                    {key: "newIn", value:0x111},
                    {key: "sell",  value:0x112},
                    {key: "sale",  value:0x113},
                    {key: "clearance", value:0x114},
                ],
                selected: 0,
                data: {}
            }
        },
        methods: {
            ComputePrice() {
                this.price = this.purchase + this.purchase * this.expired;
                this.newIn = this.purchase + 0.75 * this.purchase * this.expired;
                this.sale  = this.purchase + 0.50 * this.purchase * this.expired;
                this.clearance  = this.purchase + 0.20 * this.purchase * this.expired;
                this.Emit();
            },
            Emit: function () {
                this.data.purchase  = this.purchase;
                this.data.price     = this.price;
                this.data.newIn     = this.newIn;
                this.data.sale      = this.sale;
                this.data.clearance = this.clearance;
                this.data.status    = this.cycle[this.selected].value;
                this.$emit("priceInfo", this.data);
            }
        }
    }
</script>

<style scoped>

</style>