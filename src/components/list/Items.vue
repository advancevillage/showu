<template>
    <div>
        <div class="filters">
            <!-- //TODO -->
        </div>
        <div class="items">
            <div class="card" v-for="(item, index) in goods.items" :key="index" v-on:mouseenter="item.hover = true" v-on:mouseleave="item.hover = false">
                <div class="card-image">
                    <div class="flags">
                        <div class="left"></div>
                        <div class="right">
                            <b-icon icon="star-face"></b-icon>
                        </div>
                    </div>
                    <a :href= "api.CreateDetailLink(item.brand, item.category, item.name, item.id)">
                        <div v-for="(image, index) in item.images" :key="index">
                                <img class="images" v-if="image.direction === 1  && !item.hover" :src="api.QueryImageUrl(image.url)" alt="Placeholder image">
                                <img class="images" v-if="image.direction === -1 &&  item.hover" :src="api.QueryImageUrl(image.url)" alt="Placeholder image">
                        </div>
                    </a>
                    <div  v-if="item.hover" class="sizes" v-on:mouseenter="item.sizeHover = true" v-on:mouseleave="item.sizeHover = false">
                        <div  v-if="item.sizeHover">
                            <span class="size" v-for="(size, index) in item.sizes" :key="index" v-on:mouseenter="item.selectedSize = index" @click="AddCart(item)">{{size.value}}</span>
                        </div>
                        <div v-else>
                            <span><b-icon icon="cart"></b-icon></span>
                        </div>
                    </div>
                </div>
                <div class="card-content">
                    <span class="title">{{item.title[language]}}</span>
                    <!-- 价格 -->
                    <span v-if="item.status === 0x111" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{color: 'black', margin: '0 4px'}">{{languages.Country[language]}}{{item.newIn}}</span>
                        <span v-bind:style="{color: 'black', margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x112" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{color: 'black', margin: '0 4px'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x113" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{color: 'black', margin: '0 4px'}">{{languages.Country[language]}}{{item.sale}}</span>
                        <span v-bind:style="{color: 'black', margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x114" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{color: 'black', margin: '0 4px'}">{{languages.Country[language]}}{{item.clearance}}</span>
                        <span v-bind:style="{color: 'black', margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <!-- 颜色 -->
                    <div v-if="item.colors.length > 0 && item.hover" class="color">
                        <span class="color_name">{{item.colors[item.selectedColor].name[language]}}</span>
                        <ul>
                            <li class="color_warp" v-for="(color, index) in item.colors" :key="index" v-bind:style="[item.selectedColor === index ? {border: '1px solid darkgray'} : {}]" v-on:click="item.selectedColor = index">
                                <span class="color_item" :style="{'background': color.rgb}"></span>
                            </li>
                        </ul>
                    </div>
                    <div v-else class="color_text">
                        <span>{{item.colors.length}} {{languages.List.color[language]}}</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer">
        </div>
    </div>
</template>

<script>

    import BIcon from "buefy/src/components/icon/Icon";
    export default {
        name: "Items",
        components: {BIcon},
        props: {
            language: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                languages: this.$languages,
                api: this.$api,
                page: 0,
                perPage: 30,
                goods: {
                    total: 0,
                    items: []
                },
            }
        },
        mounted: function() {
            this.QueryGoods();
        },
        methods: {
            QueryGoods: async function() {
                const params = {
                    page: this.page,
                    perPage: this.perPage
                };
                const headers = {
                    "x-language": this.language
                };
                this.goods = await this.$api.QueryGoods(params, headers) || {total: 0, items: []};
                for (let i = 0; i < this.goods.items.length; i++) {
                    this.$set(this.goods.items[i], 'hover', false);
                    this.$set(this.goods.items[i], 'sizeHover', false);
                    this.$set(this.goods.items[i], 'selectedColor', 0);
                    this.$set(this.goods.items[i], 'selectedSize', 0);
                }
            },
            AddCart(item) {
                item = item || {};
                let cart = {};
                //goods
                cart.gid    = item.id;
                cart.name   = item.name;
                cart.status = item.status;
                cart.count  = 1;
                switch (cart.status) {
                    case 0x111:
                        cart.price = item.newIn;
                        break;
                    case 0x112:
                        cart.price = item.price;
                        break;
                    case 0x113:
                        cart.price = item.sale;
                        break;
                    case 0x114:
                        cart.price = item.clearance;
                        break
                }
                //size
                cart.sizeId = item.sizes[item.selectedSize].id;
                cart.sizeValue  = item.sizes[item.selectedSize].value;
                //color
                cart.colorId   = item.colors[item.selectedColor].id;
                cart.colorName = item.colors[item.selectedColor].name;
                //front image
                cart.frontImage = item.images[0].url;
                this.$utils.AddCart(cart);
            }
        }

    }
</script>

<style scoped>
    .filters {
        width: 100%;
        height: 50px;
    }
    .items {
        width: 100%;
        height: 90%;
        float: left;
        padding: 0 2%;
    }
    /* 列表页 图片 w/h=4/5 */
    .images {
        width: 337px;
        height: 422px;
    }
    .card-image > .sizes {
        position: absolute;
        height: 6%;
        top: 90%;
        background: rgba(192,192,192, 0.6);
        width: 95%;
        margin: 2%;
        text-align: center;
        line-height: 2rem;
        cursor: pointer;
    }
    .card-image > .sizes  .size {
        margin: 0 5px;
        color: white;
        font-weight: bolder;
    }
    .card-image > .sizes  .size:hover {
        color: black;
    }
    .card-image > .flags {
        z-index: 0;
        position: absolute;
        width: 100%;
    }
    .card-image > .flags > .left, .card-image > .flags > .right {
        float: left;
        height: auto;
        width: 100px;
    }
    .card-image > .flags > .right {
        float: right;
        color: white;
    }
    .card-image > .flags > .right > .icon {
        margin-left: 70%;
        margin-top: 5%;
    }
    /* 描述 */
    .card-content > .title, .card-content > .color {
        font-size: large;
        text-align: center;
        color: black;
        font-family: serif;
        line-height: 1rem;
    }
    .card-content > .color > .color_name {
        font-size: small;
        text-align: left;
        width: 100%;
        display: block;
        line-height: 1.5rem;
        color: darkgray;
        font-family: serif;
    }
    .card-content > .color, .card-content > .color_text {
        width: 100%;
        height: auto;
        float: left;
        overflow: hidden;
        cursor: pointer;
        color: darkgray;
        font-family: serif;
        line-height: 3rem;
    }
    .card-content > .color  .color_warp {
        width: 20px;
        height: 20px;
        border-radius: 100%;
        padding: 4px;
        float: left;
        display: block;
    }
    .card-content > .color .color_item {
         width: 10px;
         height: 10px;
         border-radius: 100%;
         padding: 0;
         margin: 0;
         display: block;
     }
    .card-content > .color > .color_warp:hover {
        border-radius: 0;
    }
    .card-content {
        padding: 0.5rem;
    }
    .card {
        width: 337px;
        height: 510px;
        float: left;
        margin-right: 1%;
        margin-bottom: 1%;
    }
    .ver {
        position: absolute;
        top: 0;
        left: 50%;
        animation: ver-animation 2s 0.5s 2;
        animation-timing-function: cubic-bezier(0.06, .46, 0, 1.04)
    }
    .ver .hor {
        animation: hor-animation 2s linear .5s 2;
    }

    @keyframes hor-animation{
        0%{
            transform: translateX(0px)
        }
        100%{
            transform: translateX(400px)
        }
    }
</style>