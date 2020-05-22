<template>
    <div class="user" v-bind:style="{width: width + 'px', height: height + 'px'}" @mouseenter="active = true" @mouseleave="active = !active">
        <button v-bind:style="[opacity ? {background: 'rgba(128,128,128,0)', border: '1px solid rgba(128,128,128,0)'}:{background: 'rgba(128,128,128,1)', border: '1px solid rgba(128,128,128,1)'}]">
            <span class="mdi mdi-account"></span>
            <em  v-if="active"></em>
            <div v-if="active">
                <ListGroup :items="items" :width="width << 1"/>
            </div>
        </button>
    </div>
</template>

<script>
    import ListGroup from "../Basic/ListGroup";

    export default {
        name: "User",
        components: {
            ListGroup
        },
        props: {
            items: {
                type: Array,
                required: true
            },
            width: {
                type: Number,
                required: false,
                default: 50
            },
            height: {
                type: Number,
                required: false,
                default: 50
            },
            opacity: {
                type: Boolean,
                required: false,
                default: false,
            }
        },
        data() {
            return {
                active: false,
            }
        }
    }
</script>

<style scoped>
    .user {
        margin: 0;
        padding: 0;
    }
    .user > button {
        width: 98%;
        height: 98%;
        border-radius: 6px;
        box-shadow: none;
        display: block;
        outline: none;
        font-family: monospace;
        background: rgb(128,128,128);
        border: 1px solid rgb(128,128,128);
        cursor: pointer;
        position: relative;
    }
    .user > button > span {
        zoom: 2.5;
    }
    .user > button > em {
        width: 0;
        height: 0;
        font-size: 0;
        opacity: 1;
        border: 4px solid rgba(128,128,128,0);
        border-bottom: 8px solid black;
        position: absolute;
        bottom: 0;
        left: 0;
        margin: 0 45%;
    }
    .user > button > div {
        position: absolute;
        border-top: 2px solid white;
        top: 105%;
        left: -55%;
    }
</style>