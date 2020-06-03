<template>
    <div class="ss_step" v-if="items.length > 0" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <div class="ss_step_item" v-for="(item, index) in items" :key="index" v-bind:style="{width: 100.0/items.length + '%'}">
            <span class="ss_step_line_left" v-if="index > 0" v-bind:style="[index <= id ? {color: 'black'}:{}]"></span>
            <span :class="item.icon" class="ss_step_icon" v-bind:style="[index <= id ? {color: 'black'}:{}]"></span>
            <span class="ss_step_text" v-bind:style="[index <= id ? {color: 'black'}:{}]">{{item.label}}</span>
            <span class="ss_step_line_right" v-if="index < items.length - 1" v-bind:style="[index <= id ? {color: 'black'}:{}]"></span>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Step",
        props: {
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 1440
            },
            height: {
                type: Number,
                required: false,
                default: 200
            },
            id: {
                type: Number,
                required: false,
                default: -1,
            }
        },
    }
</script>

<style scoped>
    .ss_step {
        overflow: hidden;
        margin: 0;
        padding: 1% 0;
        width: 100%;
        text-align: center;
    }
    .ss_step_item {
        float: left;
        position: relative;
        line-height: 2rem;
        font-size: xx-large;
    }
    .ss_step_icon, .ss_step_line_left, .ss_step_line_right, .ss_step_text {
        color: lightgray;
    }
    .ss_step_line_left, .ss_step_line_right {
        border-bottom: 4px solid;
        display: block;
        position: absolute;
        top: 50%;
        width: 45%;
    }
    .ss_step_line_left {
        left: 0;
    }
    .ss_step_line_right {
        right: 0;
    }
    .ss_step_text {
        position: absolute;
        left: 0;
        bottom: -100%;
        font-size: small;
        font-family: monospace;
        text-align: center;
        width: 100%;
    }
</style>