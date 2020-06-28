<template>
    <div class="list-group" v-bind:style="{width: width + 'px', height: 'auto'}">
        <ul>
            <li v-for="(item, index) in items" :key="index">
                <a v-if="item.link" :href="item.link">
                    <span v-if="item.value[language]">{{item.value[language]}}</span>
                    <span v-else-if="item.value">{{item.value}}</span>
                    <span v-else>{{item}}</span>
                </a>
                <span v-else-if="item.value[language] && item.fn" @click="item.fn(item)">{{item.value[language]}}</span>
                <span v-else-if="item.value[language] && !item.fn">{{item.value[language]}}</span>
                <span v-else-if="item.value && item.fn" @click="item.fn(item)">{{item.value}}</span>
                <span v-else-if="item.value && !item.fn">{{item.value}}</span>
                <span v-else>{{item}}</span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "ListGroup",
        props: {
            width:  {
                type: Number,
                required: false,
                default: 50
            },
            height:  {
                type: Number,
                required: false,
                default: 50
            },
            items: {
                type: Array,
                required: true,
            },
            language: {
                type: String,
                required: false,
                default: "en"
            }
            // (17 * items.length) + 'px'}
        },
    }
</script>

<style scoped>
    .list-group {
        text-align: center;
        font-family: serif;
        overflow: auto;
        font-size: smaller;
        text-transform: capitalize;
    }
    .list-group ul {
        background: lightgray;
        color: black;
        cursor: pointer;
    }
    .list-group ul li a {
        color: black;
    }
    .list-group a {
        width: 100%;
        display: inline-block;
    }
    .list-group a:hover, .list-group li:hover {
        background: darkgray;
        color: white;
        font-weight: bolder;
    }
</style>