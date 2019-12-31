<template>
    <div>
        <Header/>
        <div id="container">
            <div>
                <!-- 菜单页 -->
                <div class="container_menu">
                    <b-navbar class="container_menu_items" :class="{'container_menu_items_hover': containerMenu.hover}" v-on:mouseenter.native="containerMenuItemsMouseEnter()" v-on:mouseleave.native="containerMenuItemsMouseLeave()">
                        <template slot="start">
                            <b-navbar-item :key="index" href="#" v-for="(cat, index) in containerMenu.categories"
                                           v-on:mouseenter.native="containerMenuItemMouseEnter(index)"
                                           v-on:mouseleave.native="containerMenuItemMouseLeave()">
                                <span class="container_menu_item" :class="{'container_menu_item_hover': showContainerMenuItem(index) }">{{cat.categoryName}}</span>
                            </b-navbar-item>
                        </template>
                        <template slot="end">
                            <b-navbar-item href="#" >
                                <span class="container_menu_item">{{containerMenu.user.userNickName}}</span>
                            </b-navbar-item>
                            <b-navbar-item href="#" >
                                <b-button class="container_menu_item_cart">{{containerMenu.user.userCartCount}}</b-button>
                            </b-navbar-item>
                        </template>
                    </b-navbar>
                    <div class="container_menu_item_context" :class="{'container_menu_item_context_show': showContainerMenuItemContext() }"  v-on:mouseenter="containerMenuItemContextMouseEnter()" v-on:mouseleave="containerMenuItemContextMouseLeave()">
                            <div class="container_menu_item_context_list">
                                <div class="container_menu_item_context_list_item" v-for="(item, index) in containerMenu.itemContext.list" :key="index">
                                    {{item.categories}}
                                </div>
                            </div>
                            <div class="container_menu_item_context_images">
                            </div>
                    </div>
                </div>
                <div class="container_carousel">
                    <!-- Banner走马灯-->
                    <b-carousel :arrow="containerCarousel.arrow" :indicator="containerCarousel.indicator" :indicator-inside="containerCarousel.indicatorInside" :indicator-mode="containerCarousel.indicatorMode" :indicator-style="containerCarousel.indicatorStyle" :pause-info="containerCarousel.pauseInfo" :animated="containerCarousel.animated" :pause-hover="containerCarousel.pauseHover">
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
                            <div class="container_newIn_item_in_desc">
                                <div class="content">
                                    {{item.goodsDescription}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <hr style="margin: 1.5rem"/>
            <!-- 热销展示-->
            <div class="container_hot">
                <div class="container_hot_items">
                    <swiper :options="containerHot.option">
                        <div class="swiper-slide" v-for="(item, index) in containerHot.hots" :key="index">
                            <div class="container_hot_item">
                                <img class="container_hot_item_img" :class="{'container_hot_item_hover': containerHot.hover === index}" :src="item.imageUrl" v-on:mouseenter="containerHot.hover = index" v-on:mouseleave="containerHot.hover = -1">
                            </div>
                        </div>
                        <div class="swiper-pagination" slot="pagination"></div>
                        <div class="swiper-button-prev" slot="button-prev"></div>
                        <div class="swiper-button-next" slot="button-next"></div>
                    </swiper>
                </div>
            </div>
            <hr style="margin: 1.5rem"/>
            <!-- 买家秀-->
            <div class="container_buyer">
                <div class="container_buyer_items">
                    <swiper :options="containerBuyer.option">
                        <div class="swiper-slide" v-for="(item, index) in containerBuyer.buyers" :key="index">
                            <div class="container_buyer_item">
                                <img class="container_buyer_item_img" :class="{'container_buyer_item_hover': containerBuyer.hover === index}" :src="item.imageUrl" v-on:mouseenter="containerBuyer.hover = index" v-on:mouseleave="containerBuyer.hover = -1">
                            </div>
                        </div>
                        <div class="swiper-pagination" slot="pagination"></div>
                        <div class="swiper-button-prev" slot="button-prev"></div>
                        <div class="swiper-button-next" slot="button-next"></div>
                    </swiper>
                </div>
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
                    arrow: false,
                    indicator: true,
                    indicatorInside: true,
                    indicatorMode: 'hover',
                    indicatorStyle: 'is-dots',
                    pauseInfo: false,
                    animated: 'fate',
                    pauseHover: true
                },
                containerMenu: {
                    position: "is-left",
                    size: "is-medium",
                    categories: [
                        {categoryName: "NewIn", categoryId: "1111111111"},
                        {categoryName: "NewIn", categoryId: "2222222222"},
                        {categoryName: "NewIn", categoryId: "3333333333"},
                    ],
                    hover: false,
                    item: {
                        hover: -1
                    },
                    itemContext: {
                        hover: -1,
                        list: [
                            {categories: [1, 2, 3]},
                            {categories: [4, 5, 6]},
                            {categories: [7, 8 ,9]}
                        ]
                    },
                    user: {
                        userNickName: "richard",
                        userId: "11111",
                        userCartCount: 3
                    },

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
                    ],
                    hover: -1,
                    option: {
                        slidesPerView: 4,
                        spaceBetween: 1,
                        slidesPerGroup: 2,
                        loop: false,
                        loopFillGroupWithBlank: true,
                        navigation: {
                            nextEl: '.swiper-button-next',
                            prevEl: '.swiper-button-prev'
                        }
                    }
                },
                containerBuyer: {
                    option: {
                        slidesPerView: 4,
                        spaceBetween: 1,
                        slidesPerGroup: 2,
                        loop: false,
                        loopFillGroupWithBlank: true,
                        navigation: {
                            nextEl: '.swiper-button-next',
                            prevEl: '.swiper-button-prev'
                        }
                    },
                    buyers: [
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "000000000", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "111111111", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "222222222", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "333333333", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "444444444", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "555555555", goodsDescription: "Lorem ipsum dolor sit amet"},
                        {imageUrl: "https://res.cloudinary.com/everlane/image/upload/c_fill,dpr_2.0,f_auto,h_580,q_auto,w_580/v1/i/f9bb5b3f_54e4.jpg", goodsId: "666666666", goodsDescription: "Lorem ipsum dolor sit amet"},
                    ],
                    hover: -1,
                }
            }
        },
        name: "Index",
        components: {
            Header,
            Footer
        },
        mounted() {
            window.addEventListener('scroll',this.handleScroll, true)
        },
        methods: {
            getCarouselImageUrl: function (value) {
                return `https://picsum.photos/id/43${value}/1230/500`
            },
            /*菜单页*/
            containerMenuItemsMouseEnter() {
                this.containerMenu.hover = true;
            },
            containerMenuItemsMouseLeave() {
                this.containerMenu.hover = false;
            },
            containerMenuItemMouseEnter(index) {
                this.containerMenu.item.hover = index;
                this.containerMenu.itemContext.hover = index;
            },
            containerMenuItemMouseLeave() {
                this.containerMenu.item.hover = -1;
            },
            containerMenuItemContextMouseEnter() {
                this.containerMenu.hover = true;
                this.containerMenu.item.hover = this.containerMenu.itemContext.hover;
            },
            containerMenuItemContextMouseLeave() {
                this.containerMenu.hover = false;
                this.containerMenu.item.hover = -1;
                this.containerMenu.itemContext.hover = -1;
            },
            showContainerMenuItem(index) {
                return this.containerMenu.hover && this.containerMenu.item.hover === index
            },
            showContainerMenuItemContext() {
                return this.containerMenu.hover && this.containerMenu.item.hover !== -1
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
    /*菜单页 菜单栏*/
    .container_menu {
        z-index: 25;
        position: absolute;
        width: 100%;
        height: 40px;
    }
    .container_menu_items {
        padding: 5px 40px 0 40px;
        background: rgba(192, 192, 192, 0);
    }
    .container_menu_items_hover {
        background: rgba(192, 192, 192, 1);
    }
    .container_menu_item {
        width: 100%;
        text-align: center;
        color: white;
    }
    .container_menu_item_hover {
        font-weight: bolder;
        border-bottom: 2px solid white;
    }
    .container_menu_item_cart {
        background-color: darkgray;
        border-radius: 50px;
    }
    .container_menu_item_context {
        width: 100%;
        height: 240px;
        padding: 0 40px;
        display: none;
    }
    .container_menu_item_context_show {
        display: block;
        background: rgba(216, 216, 216, 0.9);
        border-top: 2px solid white;
    }
    .container_menu_item_context_list {
        float: left;
        width: 45%;
        height: 240px;
    }
    .container_menu_item_context_list_item {
        width: 25%;
        height: 220px;
        float: left;
        margin: 10px;
    }
    .container_menu_item_context_images {
        float: left;
        width: 55%;
        height: 240px;
    }
    a.navbar-item:focus, a.navbar-item:focus-within, a.navbar-item:hover {
        background-color: rgba(128, 128, 128, 0);
    }
    /*菜单页 走马灯*/
    .container_carousel {
        z-index: 5;
    }
    /*新品区*/
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
    .container_newIn_item_in {
        padding: 10px;
    }
    .container_newIn_item_in:hover, .container_newIn_item_in:focus, .container_newIn_item_in:active {
        padding: 0;
    }
    /*热销区*/
    .container_hot, .container_buyer {
        width: 100%;
        height: 550px;
        overflow: hidden;
        padding: 0 2%;
    }
    .container_hot_item, .container_buyer_item {
        width: 340px;
        height: 452px;
    }
    .container_hot_item_img, .container_buyer_item_img {
        width: 320px;
        height: 432px;
        padding: 10px;
    }
    .container_hot_item_hover, .container_buyer_item_hover {
        width: 340px;
        height: 452px;
        padding: 0;
    }
    /*买家秀*/
    .container_buyer {
        height: 500px;
    }
</style>