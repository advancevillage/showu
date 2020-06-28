<template>
    <div class="goods" v-bind:style="{width: width + 'px', height: height + 'px'}" @mouseenter="zoom = 0.85" @mouseleave="zoom = 1">
        <div class="image">
            <div class="tags">
                <span v-if="0 === item.state" v-bind:style="{width: width/6 + 'px', height: width/6 + 'px'}">
                    <img :src="item.stateImageUrl"/>
                </span>
            </div>
            <img v-if="decoration" :src="item.imageUrl" v-bind:style="{width: width + 'px', height: (zoom * height) + 'px'}" @mouseenter="decoration = false" @mouseleave="decoration = true" @click="goto(item)"/>
            <img v-else :src="item.backImageUrl" v-bind:style="{width: width + 'px', height: (zoom * height) + 'px'}" @mouseenter="decoration = false" @mouseleave="decoration = true" @click="goto(item)"/>
            <div v-if="zoom < 1" class="sizes" @mouseenter="sizeSelected = true" @mouseleave="sizeSelected = false">
                <span v-if="sizeSelected" v-bind:style="{height: width >> 3 + 'px'}">
                    <ul v-bind:style="[((width - 25 * item.sizes.length) >> 1) <= 0 ? {}: {marginLeft: ((width - 25 * item.sizes.length) >> 1) + 'px'}]">
                        <li v-for="(size, index) in item.sizes" :key="index" @click="get(index)">
                            {{size}}
                        </li>
                    </ul>
                </span>
                <span v-else class="mdi mdi-cart-arrow-down"></span>
            </div>
            <div v-if="rock" class="cart-warp">
                <span class="cart mdi mdi-gift"></span>
            </div>
        </div>
        <div class="detail" v-bind:style="{width: width + 'px', height: (0.2 * height) + 'px'}">
            <span v-bind:style="{float: 'right'}"><span v-bind:style="{float: 'right', margin: '0 5%'}">{{item.statePrice}}</span><span v-if="item.statePrice < item.price" v-bind:style="{textDecoration: 'line-through', margin: '0 5%', float: 'right'}">{{item.price}}</span></span>
            <span v-bind:style="{float: 'left'}">{{item.name[language]}}</span>
            <div>
                <div class="color-warp" v-for="(color, index) in item.colors" :key="index" v-bind:style="[colorSelected === index ? {border: '1px solid darkgray'}:{}]" @mouseenter="colorHover = index" @mouseleave="colorHover = -1" @click="colorSelected = index">
                    <em v-bind:style="[colorHover === index ? {opacity:1}:{opacity:0}]">{{color.name[language]}}</em>
                    <span v-bind:style="{backgroundColor: color.rgb}"></span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
     export default {
        name: "Goods",
        props: {
            item: {
                type: Object,
                required: true,
            },
            width: {
                type: Number,
                required: false,
                default: 337
            },
            height: {
                type: Number,
                required: false,
                default: 510
            },
            language: {
                type: String,
                required: false,
                default: "en"
            }
        },
        data() {
            return {
                zoom: 1,
                colorSelected: 0,
                sizeSelected: false,
                decoration: true,   //正面:true 背面: false
                colorHover: -1,
                rock: false
            }
         },
         methods:{
            get(index) {
                this.animation();
                let data = this.item;
                data.colorSelected = this.colorSelected;
                data.sizeSelected  = index;
                this.$emit('get', data);
            },
            animation() {
                let timeout = 1;
                let clock = window.setInterval( () => {
                    if (timeout < 1) {
                     window.clearInterval(clock);
                     this.rock = false;
                    } else {
                     timeout--;
                     this.rock = true;
                    }
                }, 330)
            },
            goto(item) {
                if (!item.link) {
                    return
                }
                this.$router.push({path: item.link})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });
             }
         }
    }
</script>

<style scoped>
    .goods {
        border: 1px solid lightgray;
        position: relative;
        margin: 0;
        padding: 1px;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .goods:hover {}
    .image {
        width: 100%;
        position: relative;
    }
    .detail {
        height: 20%;
        width: 100%;
    }
    .detail > span {
        display: inline-block;
        padding: 0 4%;
        width: 50%;
    }
    .detail > div {
        float: left;
        width: 100%;
        padding: 1%;
    }
    .color-warp {
        width: 15px;
        height: 15px;
        float: left;
        border-radius: 100%;
        cursor: pointer;
        margin: 2px;
        line-height: 1em;
        padding: 0;
        position: relative;
    }
    .color-warp > span {
        width: 10px;
        height: 10px;
        border-radius: 100%;
        display: inline-block;
        position: absolute;
        top: 2px;
        left: 1px;
    }
    .color-warp > em {
        visibility: visible;
        position: absolute;
        background-color: #555;
        color: #fff;
        text-align: center;
        padding: 2px 5px;
        border-radius: 6px;
        z-index: 1;
        opacity: 0.8;
        -webkit-transition: opacity .6s;
        transition: opacity .6s;
        bottom: 110%;
        left: -10%;
    }
    .tags {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        float: left;
        margin: 0;
        padding: 0;
    }
    .tags > span, .sizes > span {
        display: inline-block;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        transform: rotate(-45deg);
        font-family: monospace;
        line-height: 2rem;
        text-align: center;
        color: black;
    }
    .sizes {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        float: left;
        margin: 0;
        padding: 0;
        background-color: rgba(192, 192, 192, 0.75);
    }
    .sizes:hover {
        background-color: rgba(192, 192, 192, 1);
    }
    .sizes > span {
        transform: none;
        line-height: 2rem;
        width: 100%;
        vertical-align: middle;
    }
    .sizes li {
        float: left;
        display: inline-block;
        margin: 0 4px;
        cursor: pointer;
        text-align: center;
        font-size: medium;
        color: black;
        max-width: 25px;
    }
    .sizes li:hover {
        color: white;
        font-weight: bolder;
    }

    @keyframes hor-animation{
        0%{
            transform: translateX(0px)
        }
        100%{
            transform: translateX(50px)
        }
    }

    @keyframes ver-animation{
        0%{
            transform: translateY(0px)
        }
        100%{
            transform: translateY(-50px)
        }
    }
    .cart-warp{
        position: relative;
        animation: ver-animation 330ms 5ms 1;
        animation-timing-function: cubic-bezier(.25, .1, .25, 1)
    }
    .cart-warp .cart{
        position: absolute;
        bottom: 30px;
        left: 50%;
        animation: hor-animation 330ms linear 5ms 1;
    }
</style>