<template>
    <div :style="'height:' + (30 + (sizes.length)/4 * 30) + 'px'">
        <div class="detail_size">
            <b-tag class="size" v-for="(item, index) in sizes" :key="index" v-bind:style="[selected === index ? {background: 'black', fontWeight: 'bolder', color: 'white'} : {}]" v-on:click.native="selected = index">
                {{item.value}}
            </b-tag>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Size",
        props: {
            sizes: {
                type: Array,
                required: true,
            },
        },
        data() {
            return {
                selected: 0,
            }
        }
    }
</script>

<style scoped>
    .size {
        width: 40px;
        height: 20px;
        margin: 0 2px;
        cursor: pointer;
    }
    .size:hover {
        background: darkgray;
    }
</style>