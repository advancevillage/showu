<template>
    <div class="ss_fragment" v-bind:style="{width: width + 'px'}">
        <div v-for="(item, index) in items" :key="index" v-bind:style="{width: (width * 0.99)/ items.length + 'px'}">
            <ul class="ss_group">
                <li v-for="(group, seq) in item.group" :key="seq">
                    <span v-if="!group.link" v-bind:style="{width: (width * 0.9)/ items.length + 'px'}">{{group.value}}</span>
                    <a v-else :href="group.link"><span v-if="group.link" v-bind:style="{width: (width * 0.9)/ items.length + 'px'}">{{group.value}}</span></a>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Fragment",
        props: {
            items: {
                type: Array,
                required: true
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
            }
        },
        data() {
            return {
            }
        }
    }
</script>

<style scoped>
    .ss_fragment {
        overflow: hidden;
        width: 100%;
        border: 1px solid darkgray;
        height: auto;
    }
    .ss_fragment > div {
        float: left;
        height: 100%;
        text-align: left;
    }
    .ss_group {
        margin: 0;
        width: 100%;
        height: 100%;
        padding: 1% 0 0 10%;
        text-align: left;
    }
    .ss_group li {
        list-style: disc;
    }
    .ss_group span {
        word-break: break-all;
        display: inline-block;
        overflow-wrap: break-word;
    }
    .ss_group a {
        color: black;
    }
</style>