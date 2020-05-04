<template>
    <div class="slide">
        <ul class="slide-auto" v-bind:style="{width: width * items.length + 'px', marginLeft: marginLeft + 'px'}">
            <li v-for="(item, index) in items" :key="index" v-bind:style="{width: width + 'px', height: height + 'px'}">
                <a v-if="item.link" :href="item.link">
                    <img :src="'https://picsum.photos/id/43' + index + '/1230/500'" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
                </a>
                <img v-else :src="'https://picsum.photos/id/43' + index + '/1230/500'" v-bind:style="{width: width + 'px', height: height + 'px',}"/>
            </li>
        </ul>
        <span class="indicator" v-bind:style="{display: 'inline-block'}">
            <button v-for="(item, index) in items" :key="index" v-on:click="get(index)">{{index + 1}}</button>
        </span>
    </div>
</template>

<script>
    export default {
        name: "Banner",
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
        },
        data() {
            return {
                marginLeft: 0
            }
        },
        methods: {
            get(index) {
                this.marginLeft = 0 - index * this.width;
                this.marginLeft %= this.width * this.items.length;
                let data = {}
                data.index = index;
                data.value = this.items[index];
                this.$emit('click', data)
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
        z-index: 100;
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
</style>