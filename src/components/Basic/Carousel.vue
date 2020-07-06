<template>
    <div class="slide" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <ul class="slide-auto" v-bind:style="{width: width * items.length + 'px', marginLeft: marginLeft + 'px'}">
            <li v-for="(item, index) in items" :key="index" v-bind:style="{width: width + 'px', height: height + 'px'}" @mouseenter="hover = true" @mouseleave="hover = !hover">
                <a v-if="item.link" :href="item.link">
                    <img :src="item.imageUrl" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                </a>
                <img v-else :src="item.imageUrl" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                <div v-if="item.button" class="container" v-bind:style="{height: (height >> 2) + 'px'}">
                    <button>{{item.button.value}}</button>
                </div>
            </li>
        </ul>
        <span class="action" v-if="action">
            <button @click="action.fn"><span class="mdi mdi-cart"></span></button>
        </span>
        <span class="indicator" v-bind:style="{display: 'inline-block'}">
            <button v-for="(item, index) in items" :key="index" v-on:click="get(index)" v-bind:style="[index === active ? {background: 'black', color: 'white'}:{}]">{{index + 1}}</button>
        </span>
    </div>
</template>

<script>
    export default {
        name: "Carousel",
        props: {
            items: {
                type: Array,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 1440,
            },
            height: {
                type: Number,
                required: false,
                default: 620,
            },
            action: {
                type: Object,
                required: false
            },
            interval: {
                type: Number,
                required: false,
                default: 5
            },
            language: {
                type: String,
                required: false,
                default: "en"
            },
            setIndex: {
                type: Number,
                required: false,
                default: 0,
            }
        },
        watch: {
            setIndex(v) {
                this.get(v);
            }
        },
        data() {
            return {
                marginLeft: 0,
                clock: null,
                hover: false,
                active: this.setIndex
            }
        },
        mounted() {
            this.clock = window.setInterval(()=> {
                if (!this.hover) {
                    this.marginLeft = 0 - this.active * this.width;
                    this.marginLeft %= this.width * this.items.length;
                    this.active++;
                    this.active %= this.items.length;
                }
            }, this.interval * 1000)
        },
        beforeDestroy() {
            window.clearInterval(this.clock)
        },
        methods: {
            get(index) {
                this.marginLeft = 0 - index * this.width;
                this.marginLeft %= this.width * this.items.length;
                this.active = index;
                this.$emit('get', this.items[index])
            }
        }
    }
</script>

<style scoped>
    .slide {
        position: relative;
        margin: 0;
        text-align: center;
        color: #000;
        overflow: hidden;
    }
    .slide > * {
        float: left;
    }
    .indicator {
        width: 100%;
        position: relative;
        margin-top: -40px;
    }
    .indicator > button {
        cursor: pointer;
        width: 20px;
        height: 20px;
        border-radius: 100%;
        margin: 2px;
        text-align: center;
        border: none;
        box-shadow: none;
        outline: none;
    }
    .indicator > button:hover {
        background: black;
        color: white;
    }
    .slide-auto {
        width: 100%;
        height: 100%;
    }
    .slide-auto li {
        display: inline-block;
    }
    .container {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
    }
    .container span {
        display: inline-block;
        font-family: monospace;
        font-size: x-large;
        text-align: center;
        zoom: 2;
    }
    .container button {
        background: lightgray;
        color: black;
        display: block;
        width: 10%;
        height: 50px;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: none;
        outline: none;
        margin-left: 48%;
        text-align: center;
    }
    .container button:hover {
        background: darkgray;
        font-weight: bolder;
    }
    .action {
        position: absolute;
        top: 66%;
        left: 48%;
    }
    .action button {
        width: 100px;
        height: 50px;
        overflow: hidden;
        border-radius: 10px;
        cursor: pointer;
        font-family: monospace;
        line-height: 3rem;
        box-shadow: none;
        outline: none;
        border: 0;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
    }
    .action button:hover {
        background: #1524d9;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        color:white;
    }
    .action button > span {
        zoom: 3;
    }
</style>