<template>
    <div>
        <div class="filters">
            <!-- //TODO -->
        </div>
        <div class="items">
            <div class="card" v-for="(item, index) in goods.items" :key="index" v-on:mouseenter="item.hover = true" v-on:mouseleave="item.hover = false">
                <a :href= "api.CreateDetailLink(item.brand, item.category, item.name, item.id)">
                <div class="card-image">
                    <div class="flags">
                        <div class="left"></div>
                        <div class="right">
                            <b-icon icon="star-face"></b-icon>
                        </div>
                    </div>
                    <div v-for="(image, index) in item.images" :key="index">
                            <img class="images" v-if="image.direction === 1  && !item.hover" :src="api.QueryImageUrl(image.url)" alt="Placeholder image">
                            <img class="images" v-if="image.direction === -1 &&  item.hover" :src="api.QueryImageUrl(image.url)" alt="Placeholder image">
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
                    <div v-if="item.hover" class="color">
                        <b-tag class="color_warp" v-for="(color, index) in item.colors" :key="index" :style="{'background': color.rgb}"></b-tag>
                    </div>
                    <div v-else class="color_text">
                        <span>{{item.colors.length}} colors available</span>
                    </div>
                </div>
                </a>
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
                }
            },
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
    .card-image > .flags {
        z-index: 0;
        position: absolute;
        width: 100%;
    }
    .card-image > .flags > .left, .card-image > .flags > .right {
        float: left;
        height: 100px;
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
    }
    .card-content > .color, .card-content > .color_text {
        width: 100%;
        height: 40px;
        float: left;
        overflow: hidden;
        cursor: pointer;
        color: black;
    }
    .card-content > .color > .color_warp {
        width: 15px;
        height: 15px;
        border-radius: 100%;
        padding: 0;
        margin: 0 3px;
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
</style>