<template>
    <div>
        <div class="filters">
            <!-- //TODO -->
        </div>
        <div class="items">
            <div class="card" v-for="(item, index) in goods.items" :key="index" v-on:mouseenter="item.hover = true" v-on:mouseleave="item.hover = false">
                <div class="card-image">
                    <div class="tags">
                        <div class="left"></div>
                        <div class="right">
                            <svg class="star" width="15px" height="12px" viewBox="0 0 15 12" version="1.1"><g stroke-width="1" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"><g transform="translate(-384.000000, -173.000000)"><g transform="translate(373.000000, 160.000000)"><path d="M24.1870486,15.1337994 C23.0156479,13.7915995 21.0146777,13.6174702 19.6357465,14.7377957 C19.0576454,15.2115959 18.655296,15.8713213 18.4944667,16.6082814 C18.3352955,15.8721638 17.9348804,15.2124384 17.3587137,14.7377957 C15.9806115,13.6211213 13.9837864,13.7949698 12.8129383,15.1337994 C11.6169435,16.5248678 11.756771,18.6380112 13.125754,19.853546 C13.1564276,19.8807888 13.1873776,19.9074699 13.2191566,19.9335893 L17.900338,23.7840937 C18.2510121,24.0719688 18.7517383,24.0719688 19.1024124,23.7840937 L23.7808304,19.9335893 C25.1929223,18.7705741 25.4101247,16.6641713 24.2658052,15.228728 C24.2401057,15.1967106 24.2138535,15.1649742 24.1870486,15.1337994 L24.1870486,15.1337994 Z"></path></g></g></g></svg>
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
                        <span v-bind:style="{margin: '0 4px'}">{{languages.Country[language]}}{{item.newIn}}</span>
                        <span v-bind:style="{margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x112" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{margin: '0 4px'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x113" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{margin: '0 4px'}">{{languages.Country[language]}}{{item.sale}}</span>
                        <span v-bind:style="{margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <span v-if="item.status === 0x114" v-bind:style="{float: 'right'}">
                        <span v-bind:style="{margin: '0 4px'}">{{languages.Country[language]}}{{item.clearance}}</span>
                        <span v-bind:style="{margin: '0 4px', textDecoration: 'line-through'}">{{languages.Country[language]}}{{item.price}}</span>
                    </span>
                    <!-- 颜色 -->
                    <div v-if="item.hover" class="color">
                        <b-tag class="color_warp" v-for="(color, index) in item.colors" :key="index" :style="{'background': color.rgb}"></b-tag>
                    </div>
                    <div v-else class="color_text">
                        <span>{{item.colors.length}} colors available</span>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer">
        </div>
    </div>
</template>

<script>
    export default {
        name: "Items",
        data() {
            return {
                languages: this.$languages,
                api: this.$api,
                language: "chinese",
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
                console.log(this.goods);
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
    .card-image > .tags {
        z-index: 30;
        position: absolute;
        float: left;
    }
    .card-image > .tags > .left, .card-image > .tags > .right {
        float: left;
        height: 100px;
        width: 100px;
    }
    .card-image > .tags > .right {
        margin-left: 137px;
    }
    .card-image > .tags > .right > .star {
        margin-top: 20%;
        margin-left: 60%;
    }
    /* 描述 */
    .card-content > .title, .card-content > .price, .card-content > .color {
        font-size: large;
        text-align: center;
    }
    .card-content > .color, .card-content > .color_text {
        width: 100%;
        height: 40px;
        float: left;
        overflow: hidden;
        cursor: pointer;
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