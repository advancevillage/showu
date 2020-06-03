<template>
    <div class="slide" v-bind:style="{height: height + 'px'}">
        <button v-if="((width + interval) * items.length) > clientWidth" v-bind:style="{top: (height >> 1) + 'px', left: '15px'}" @click="prev(1)" @mouseenter="stop = true" @mouseleave="stop = false">&lt;</button>
        <ul class="slide-auto" v-bind:style="{width: (width * slides.length + interval * items.length) + 'px', marginLeft: marginLeft + 'px'}">
            <li v-for="(item, index) in slides" :key="index" v-bind:style="{width: width + 'px', height: height + 'px', marginRight: interval + 'px'}" @click="get(index)" @mouseenter="stop = true" @mouseleave="stop = false">
                <div v-if="!cpt">
                    <a v-if="item.link" :href="item.link">
                        <img :src="item.imageUrl" class="slide-item" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                    </a>
                    <img v-else :src="item.imageUrl" class="slide-item" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                </div>
                <div v-else>
                    <Goods :item="item" :width="width" :height="height"/>
                </div>
            </li>
        </ul>
        <button v-if="((width + interval) * items.length) > clientWidth" v-bind:style="{top: (height/2) + 'px', right: '15px'}" @click="next(1)" @mouseenter="stop = true" @mouseleave="stop = false">&gt;</button>
    </div>
</template>

<script>
    import Goods from "../Business/Goods";

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
            },
            step: {
                type: Number,
                required: false,
                default: 100,
            },
            direction: {
                type: Boolean,
                required: false
            },
            cpt:  {
                type: Boolean,
                required: false,
                default: false
            }
        },
        components: {
            Goods,
        },
        data() {
            return {
                clientWidth: document.body.clientWidth,
                marginLeft: 0,
                slides: [],
                left: 0,
                right: 0,
                clock: null,
                stop: false,
            }
        },
        watch: {
            items(data) {
                for (let i = 0; i < data.length * 2; i++) {
                    this.slides.push(data[i % data.length])
                }
            }
        },
        mounted() {
            for (let i = 0; i < this.items.length * 2; i++) {
                this.slides.push(this.items[i % this.items.length])
            }
            this.trigger();
        },
        beforeDestroy() {
            window.clearInterval(this.clock)
        },
        methods: {
            next(slow) {
                this.right = isNaN(this.right) ? 0 : this.right + 1;
                this.right %= (this.items.length * slow);
                this.marginLeft = ((this.width + this.interval) * -this.right) / slow;
            },
            prev(slow) {
                this.left = isNaN(this.left) ? 0 : this.left + 1;
                this.left %= (this.items.length * slow);
                this.marginLeft = -(this.width + this.interval) * this.items.length + this.left * (this.width + this.interval) / slow
            },
            get(index) {
                this.$emit('get', this.items[index % this.items.length]);
            },
            trigger() {
                this.clock = window.setInterval(()=> {
                    if (!this.stop) {
                        let fn = this.direction ? this.prev : this.next;
                        fn(this.step);
                    }
                }, 100)
            }
        }
    }
</script>

<style scoped>
    .slide {
        position: relative;
        margin: 0;
        color: #000;
        overflow: hidden;
        padding: 0;
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
        z-index: 10;
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