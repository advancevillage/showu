<template>
    <div>
        <Header/>
        <div id="container">
            <div>
                <!-- 菜单Tab页 -->
                <div class="container_menu">
                    <b-navbar class="container_menu_items">
                        <template slot="start">
                            <b-navbar-item href="#" v-for="cat in containerMenu.categories" :key="cat.categoryId">
                                <span class="container_menu_item">{{cat.categoryName}}</span>
                            </b-navbar-item>
                        </template>
                        <template slot="end">
                            <b-navbar-item href="#" >
                                <span class="container_menu_item">{{containerAccountInfo.accountName}}</span>
                            </b-navbar-item>
                            <b-navbar-item href="#" >
                                <b-button class="container_menu_item_cart">{{containerAccountInfo.accountCartCount}}</b-button>
                            </b-navbar-item>
                        </template>
                    </b-navbar>
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

            </div>
            <!-- 热销展示-->
            <div class="container_hot">

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
                }
            }
        },
        name: "Index",
        components: {
            Header,
            Footer
        },
        methods: {
            getCarouselImageUrl(value) {
                return `https://picsum.photos/id/43${value}/1230/500`
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
        /*opacity: 0.5;*/
        width: 100%;
        height: 40px;
    }
    .container_menu_item {
        color: white;
        width: 100%;
        text-align: center;
    }
    .container_menu_items {
        padding: 5px 40px 0 40px;
        background-color: rgba(128, 128, 128, 0.3);
    }
    .container_menu_item_cart {
        background-color: darkgray;
        border-radius: 50px;
    }
    .container_carousel {
        z-index: 5;
    }
</style>