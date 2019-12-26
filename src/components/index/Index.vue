<template>
    <div>
        <Header/>
        <div id="container">
            <div>
                <!-- 菜单Tab页 -->
                <div class="container_menu">
                    <b-navbar class="container_menu_items" v-bind:style="containerMenuItemsStyle" v-on:mouseenter.native="categoryMouseEnter()" v-on:mouseleave.native="categoryMouseLeave()">
                        <template slot="start">
                            <b-navbar-item href="#" v-for="cat in containerMenu.categories" :key="cat.categoryId" v-on:mouseenter.native="categoryItemMouseEnter()" v-on:mouseleave="categoryItemMouseLeave()">
                                <span class="container_menu_item" v-bind:style="containerMenuItemStyle">{{cat.categoryName}}</span>
                            </b-navbar-item>
                        </template>
                        <template slot="end">
                            <b-navbar-item href="#" >
                                <span class="container_menu_item" v-bind:style="containerMenuItemStyle">{{containerAccountInfo.accountName}}</span>
                            </b-navbar-item>
                            <b-navbar-item href="#" >
                                <b-button class="container_menu_item_cart">{{containerAccountInfo.accountCartCount}}</b-button>
                            </b-navbar-item>
                        </template>
                    </b-navbar>
                    <div class="container_menu_item_context">
                        <div class="container_menu_item_context_list" v-bind:style="containerMenuItemContextListStyle">
                            <b-table class="container_menu_item_context_list_item" :data="containerMenuItemContext.data" :columns="containerMenuItemContext.columns"></b-table>
                        </div>
                        <div class="container_menu_item_context_images">
                        </div>
                    </div>
                </div>
                <div class="container_carousel">
                    <!-- Banner走马灯-->
                    <b-carousel :indicator="containerCarousel.indicator" :indicator-inside="containerCarousel.indicatorInside" :indicator-mode="containerCarousel.indicatorMode" :indicator-style="containerCarousel.indicatorStyle" :pause-info="containerCarousel.pauseInfo" :animated="containerCarousel.animated" :pause-hover="containerCarousel.pauseHover">
                        <b-carousel-item v-for="i in 6" :key="i">
                            <img class="container_carousel_image" :src="getCarouselImageUrl(i)">
                        </b-carousel-item>
                    </b-carousel>
                </div>
            </div>
            <!-- 新品展示-->
            <div class="container_newIn">
                <div class="container_newIn_items">
                    <div class="container_newIn_item" v-for="item in containerNewIn.newIns" :key="item.goodsId">
                        <div >
                            <div class="container_newIn_item_in">
                                <figure class="image is-640x480">
                                    <img :src="item.imageUrl" alt="Placeholder image">
                                </figure>
                            </div>
                            <div class="card-content">
                                <div class="content">
                                    {{item.goodsDescription}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- 热销展示-->
            <div class="container_hot">
                <div class="container_hot_items">
                    <!--<div class="container_hot_item" v-for="item in containerHot.hots" :key="item.goodsId">-->
                        <!--<div class="container_hot_item_in">-->
                            <!--<figure class="image is-256x172">-->
                                <!--<img :src="item.imageUrl" alt="hot image">-->
                            <!--</figure>-->
                        <!--</div>-->
                    <!--</div>-->
                    <div class="swiper-container">
                        <div class="swiper-wrapper">
                            <div class="swiper-slide container_hot_item" v-for="item in containerHot.hots" :key="item.goodsId">
                                <img :src="item.imageUrl">
                            </div>
                        </div>
                        <div class="swiper-pagination"></div>
                    </div>
                </div>
            </div>
            <!-- 买家秀-->
            <div class="container_buyer">

            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'

    export default {
        data() {
            return {
                containerCarousel: {
                    indicator: true,
                    indicatorInside: true,
                    indicatorMode: 'hover',
                    indicatorStyle: 'is-dots',
                    pauseInfo: false,
                    animated: 'fate',
                    pauseHover: true,
                    carousels: [
                        { title: 'Slide 1', color: 'info' },
                        { title: 'Slide 2', color: 'success' },
                        { title: 'Slide 3', color: 'warning' },
                        { title: 'Slide 4', color: 'danger' }
                    ]
                },
                containerMenu: {
                    position: "is-left",
                    size: "is-medium",
                    categories: [
                        {categoryName: "NewIn", categoryId: "1111111111"},
                        {categoryName: "NewIn", categoryId: "2222222222"},
                        {categoryName: "NewIn", categoryId: "3333333333"},
                    ]
                },
                containerAccountInfo: {
                    accountName: "richard",
                    accountId: "11111",
                    accountCartCount: 3
                },

                containerMenuItemContext: {
                    data: [
                        {'man': '羽绒服', 'women': '嘻嘻', 'student': '校服', 'parent': '老年鞋'},
                    ],
                    columns: [
                        { label: '男士', field: 'man',},
                        { label: '女士', field: 'women',},
                        { label: '学生', field: 'student',},
                        { label: '父母', field: 'parent',},
                    ]
                },
                containerNewIn: {
                    newIns: [
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "0000000000", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "1111111111", goodsDescription: "Lorem ipsum dolor sit amet"}
                    ]
                },
                containerHot: {
                    hots: [
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "000000000", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "111111111", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "222222222", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "333333333", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "444444444", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "555555555", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "666666666", goodsDescription: "Lorem ipsum dolor sit amet"},

                    ]
                },

                //样式区
                containerMenuItemsStyle: {
                    background: "rgba(192, 192, 192, 0)"
                },
                containerMenuItemStyle: {
                    color: "white",
                },
                containerMenuItemContextListStyle: {
                    display: "none"
                }
            }
        },
        name: "Index",
        components: {
            Header,
            Footer
        },
        methods: {
            getCarouselImageUrl: function (value) {
                return `https://picsum.photos/id/43${value}/1230/500`
            },
            categoryMouseEnter: function () {
                this.containerMenuItemsStyle.background = "rgba(192, 192, 192, 1)";
                this.containerMenuItemStyle.color = "black";
            },
            categoryMouseLeave: function () {
                this.containerMenuItemsStyle.background = "rgba(192, 192, 192, 0)";
                this.containerMenuItemStyle.color = "white";
            },
            categoryItemMouseEnter: function () {
                this.containerMenuItemContextListStyle.display = "block";
            },
            categoryItemMouseLeave: function () {
                this.containerMenuItemContextListStyle.display = "none";
            }
        }
    }
</script>

<style scoped>
    #container {
        min-height: 720px;
        min-width: 1024px;
        width: 100%;
        height: 100%;
    }
    .container_carousel_image {
        min-height: 680px;
        width: 100%;
        height: 100%;
    }
    .container_menu {
        z-index: 25;
        position: absolute;
        width: 100%;
        height: 40px;
    }
    .container_menu_item {
        width: 100%;
        text-align: center;
    }
    .container_menu_item:focus,.container_menu_item:hover,.container_menu_item:active {
        border-bottom: solid 2px white;
    }
    .container_menu_items {
        padding: 5px 40px 0 40px;
    }
    .container_menu_item_cart {
        background-color: darkgray;
        border-radius: 50px;
    }
    .container_carousel {
        z-index: 5;
    }
    a.navbar-item:focus, a.navbar-item:focus-within, a.navbar-item:hover {
        background-color: rgba(128, 128, 128, 0);
    }
    .container_menu_item_context {
        width: 100%;
        height: 200px;
        padding: 0 40px;
    }
    .container_menu_item_context_list, container_menu_item_context_images {
        float: left;
        font-size: x-small;
    }
    .container_menu_item_context_list {
        width: 40%;
    }
    .container_newIn_items {
        width: 100%;
        height: 700px;
        padding: 20px 5%;
    }
    .container_newIn_item {
        float: left;
        width: 48%;
        height: 100%;
        margin: 0 1%;
    }
    .container_hot {
        width: 100%;
        height: 300px;
        overflow: hidden;
    }
    .container_hot_items {
        padding: 5px 2%;
    }
    .container_hot_item {
        width: 256px;
        height: 256px;
    }
    .container_newIn_item_in {
        padding: 10px;
    }
    .container_newIn_item_in:hover, .container_newIn_item_in:focus, .container_newIn_item_in:active {
        padding: 0;
    }
    .card-content {
        font-size: larger;
        padding: 0;
        text-align: center;
    }
    .swiper-slide {
        text-align: center;
        background: #fff;
        /* Center slide text vertically */
        display: -webkit-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        -webkit-box-pack: center;
        -ms-flex-pack: center;
        -webkit-justify-content: center;
        justify-content: center;
        -webkit-box-align: center;
        -ms-flex-align: center;
        -webkit-align-items: center;
        align-items: center;
    }
</style>