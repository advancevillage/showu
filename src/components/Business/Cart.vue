<template>
    <div  class="add-cart" v-bind:style="{width: width + 'px', height: height + 'px'}" @mouseenter="active = true" @mouseleave="active = !active">
        <button v-bind:style="[opacity ? {background: 'rgba(128,128,128,0)', border: '1px solid rgba(128,128,128,0)'}:{background: 'rgba(128,128,128,1)', border: '1px solid rgba(128,128,128,1)'}]">
            <span class="mdi mdi-cart" @click="go('/cart')"></span>
            <em v-if="active  && items.length > 0"></em>
            <div v-if="active && items.length > 0" >
                <ImageListGroup :items="items" :width="(width + 10) << 2" @update="computeCount" @incr="computeCount" @decr="computeCount" />
                <button class="checkout" @click="go('/checkout')">{{languages.OPERATE.CHECKOUT[language]}}</button>
            </div>
        </button>
    </div>
</template>

<script>
    import ImageListGroup from "../Basic/ImageListGroup";

    export default {
        name: "Cart",
        components: {
            ImageListGroup,
        },
        props: {
            items: {
                type: Array,
                required: true,
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
            language: {
                type: String,
                required: false,
                default: "en"
            },
            opacity: {
                type: Boolean,
                required: false,
                default: false
            }
        },
        watch: {
            items() {
                this.computeCount()
            }
        },
        data() {
            return {
                active: false,
                languages: this.$languages,
                total: 0,
            }
        },
        methods: {
            computeCount() {
                this.total = 0;
                for (let i = 0; i < this.items.length; i++) {
                    this.total += this.items[i].count;
                }
                this.$emit('getCart')
            },
            go(url) {
                this.$router.push({path: url})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
            },
        }
    }
</script>

<style scoped>
    .add-cart {
        margin: 0;
        padding: 0;
    }
    .add-cart > button {
        width: 98%;
        height: 98%;
        border-radius: 6px;
        box-shadow: none;
        display: block;
        outline: none;
        font-family: monospace;
        cursor: pointer;
        position: relative;
    }
    .add-cart > button > span {
        zoom: 2.5;
    }
    .add-cart > button > em {
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
    .add-cart > button > div {
        position: absolute;
        border-top: 2px solid white;
        top: 105%;
        left: -260%;
        z-index: 5;
    }
    .add-cart > button > p {
        position: absolute;
        width: 15px;
        height: 15px;
        background: white;
        top: 5%;
        right: -10%;
        border-radius: 100%;
        font-weight: bolder;
        color: red;
    }
    .checkout {
        background: #000000;
        border-radius: 0.25rem;
        border: 0;
        cursor: pointer;
        color: white;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        font-size: 0.875rem;
        width: 100%;
        height: 1.5rem;
        outline: none;
        text-transform:capitalize;
        font-family: monospace;
    }
    .checkout:hover {
        background: #1524d9;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        color:white;
    }
</style>