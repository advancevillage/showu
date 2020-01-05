<template>
    <div>
        <Header/>
        <div id="container">
            <div>
                <div class="container_notes">
                    <div class="container_notes_top">
                    </div>
                    <div class="container_notes_mid">
                        <div class="container_notes_mid_left"></div>
                        <div class="container_notes_mid_center">
                            <div class="container_notes_mid_center_top"></div>
                            <div class="container_notes_mid_center_mid">
                                <p class="container_notes_mid_center_mid_desc">
                                    Show U !
                                </p>
                                <p class="container_notes_mid_center_mid_detail">
                                    happy new year 2020 ^_^
                                </p>
                            </div>
                            <div class="container_notes_mid_center_bottom">
                                <div class="container_notes_mid_center_bottom_link_button">
                                    <b-button rounded>Shop Now!</b-button>
                                </div>
                            </div>
                        </div>
                        <div class="container_notes_mid_right"></div>
                    </div>
                    <div class="container_notes_bottom">
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
        methods: {
            getCarouselImageUrl: function (value) {
                return `https://picsum.photos/id/43${value}/1230/500`
            },
            /*菜单页*/
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
    /*菜单栏 文字描述*/
    .container_notes {
        width: 100%;
        height: 660px;
        position: absolute;
        z-index: 10;
    }
    .container_notes_mid {
        width: 100%;
        height: 80%;
    }
    .container_notes_bottom, .container_notes_top {
        width: 100%;
        height: 10%;
    }
    .container_notes_mid_left, .container_notes_mid_right {
        width: 10%;
        height: 100%;
        float: left;
    }
    .container_notes_mid_center {
        width: 80%;
        height: 100%;
        float: left;
    }
    .container_notes_mid_center_top, .container_notes_mid_center_bottom {
        width: 100%;
        height: 20%;
    }
    .container_notes_mid_center_mid {
        width: 100%;
        height: 60%;
    }
    .container_notes_mid_center_mid_desc, .container_notes_mid_center_mid_detail {
        padding: 0 0 0 25%;
        font-size: -webkit-xxx-large;
        font-size: 100px;
        font-weight: 400;
        color: whitesmoke;
        font-style: oblique;
        font-family: -webkit-pictograph;
    }
    .container_notes_mid_center_mid_detail {
        padding: 0 0 0 25%;
        font-size: 50px;
    }
    .container_notes_mid_center_bottom_link_button {
        padding: 0 0 0 45%;
    }
    .container_notes_mid_center_bottom_link_button > .button {
        font-family: -webkit-pictograph;
        border: none;
        font-size: x-large;
        text-align: center;
        background-color: rgba(128, 128, 128, 1);
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