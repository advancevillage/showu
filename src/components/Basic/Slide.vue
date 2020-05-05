<template>
    <div class="slide">
        <button v-if="((width + interval) * items.length) > clientWidth" v-bind:style="{top: (height >> 1) + 'px', left: '15px'}" @click="prev">&lt;</button>
        <ul class="slide-auto" v-bind:style="{width: (width * items.length + interval * items.length) + 'px', marginLeft: marginLeft + 'px'}">
            <li v-for="(item, index) in items" :key="index" v-bind:style="{width: width + 'px', height: height + 'px', marginRight: interval + 'px'}" @click="get(index)">
                <a v-if="item.link" :href="item.link">
                    <img :src="item.imageUrl" class="slide-item" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                </a>
                <img v-else :src="item.imageUrl" class="slide-item" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
            </li>
        </ul>
        <button v-if="((width + interval) * items.length) > clientWidth" v-bind:style="{top: (height/2) + 'px', right: '15px'}" @click="next">&gt;</button>
    </div>
</template>

<script>
    export default {
        name: "Slide",
        props: {
            //items = [] item = items[x]
            //item = {
            //  imageUrl: "",  图片连接
            //  link: "",  链接
            //}
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 200,
            },
            height: {
                type: Number,
                required: false,
                default: 200,
            },
            interval: {
                type: Number,
                required: false,
                default: 2,
            }
        },
        data() {
            return {
                clientWidth: document.body.clientWidth,
                marginLeft: 0,
            }
        },
        mounted() {},
        methods: {
            next() {
                this.marginLeft -= (this.width + this.interval);
                this.marginLeft %= (this.width + this.interval) * this.items.length;
            },
            prev() {
                this.marginLeft += (this.width + this.interval);
                this.marginLeft %= (this.width + this.interval) * this.items.length;
            },
            get(index) {
                this.$emit('get', this.items[index]);
            }
        }
    }
</script>

<style scoped>
    .slide {
        position: relative;
        margin: 1%;
        text-align: center;
        color: #000;
        overflow: hidden;
    }
    .slide > * {
        float: left;
    }
    .slide button {
        display: inline-block;
        width: 20px;
        height: 20px;
        border-radius: 100%;
        outline: none;
        box-shadow: none;
        text-align: center;
        position: absolute;
        border: none;
        background: darkgray;
        cursor: pointer;
        opacity: 0.5;
    }
    .slide button:hover {
        opacity: 1;
        background: black;
        color: white;
    }
    .slide-auto {
        width: 96%;
    }
    .slide-auto li {
        display: inline-block;
    }
    .slide-item {
        cursor: pointer;
        padding: 2px;
    }
    .slide-item:hover {
        padding: 0;
        border: 1px solid darkgray;
    }
</style>