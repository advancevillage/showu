<template>
    <div class="notice" v-bind:style="{width: width + 'px', height: height + 'px'}">
        <ul></ul>
        <ul>
            <li  v-for="(item, index) in items" :key="index" v-bind:style="[compare(index) ? {display: 'block', marginLeft: ((width/3 - height - item.value.length*9) >> 1) + 'px'}:{display: 'none'}]" @mouseenter="hover = true" @mouseleave="hover = !hover">
                <img v-if="item.icon && item.icon.length > 0" :src="item.icon" v-bind:style="{width: height + 'px', height: height + 'px', padding: (height >> 2)+ 'px'}" />
                <a v-if="item.link && item.link.length > 0" :href="item.link">{{item.value}}</a>
                <span v-else>{{item.value}}</span>
            </li>
        </ul>
        <ul>
            <li v-bind:style="{float: 'right', marginRight: '1%'}"><Selector :items="countries" :width="width >> 4" :height="height >> 1" @get="getLanguage"/></li>
        </ul>
    </div>
</template>

<script>
    import Selector from "../Basic/Selector";

    export default {
        name: "Notice",
        components: {
            Selector,
        },
        props: {
            items: {
                type: Array,
                required: true,
            },
            countries: {
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
                default: 40,
            },
            interval: {
                type: Number,
                required: false,
                default: 2
            },
            language: {
                type: String,
                required: false,
                default: "en"
            }
        },
        mounted() {
            this.timer = setInterval(this.cycle, this.interval * 1000)
        },
        data() {
            return {
                active: 0,
                hover: false,
                timer: null
            }
        },
        beforeDestroy() {
            clearInterval(this.timer);
            this.timer = null;
        },
        methods: {
            compare(index) {
                return this.active === index
            },
            cycle() {
                if (!this.hover) {
                    this.active++
                    this.active %= this.items.length;
                }
            },
            getLanguage(data) {
                this.$emit('getLanguage', data)
            }
        }
    }
</script>

<style scoped>
    .notice {
        background: black;
        color: white;
    }
    .notice ul {
        float: left;
        width: 33.3%;
        height: 100%;
        overflow: hidden;
    }
    .notice ul li {
        float: left;
        text-align: center;
        width: 100%;
        height: 100%;
        line-height: 2.5rem;
        font-family: monospace;
        text-decoration: underline;
        text-decoration-color: white;
        cursor: pointer;
        letter-spacing: 2px;
    }
    .notice ul li > * {
        color: white;
        float: inherit;
        margin: 0 auto;
    }
    .notice ul li > *:hover {
        color: pink;
        text-decoration-color: pink;
    }
</style>