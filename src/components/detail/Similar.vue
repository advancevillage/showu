<template>
    <div>
        <nav class="level">
            <div class="level-item has-text-centered">
            </div>
            <div class="level-item has-text-centered">
                <h2>{{similar.title}}</h2>
            </div>
            <div class="level-item has-text-centered">
            </div>
        </nav>
        <div class="similar">
            <swiper :options="similar.option">
                <div class="swiper-slide" v-for="(item, index) in similar.items" :key="index">
                    <div class="similar_item_warp">
                        <img class="similar_item_warp_img" :class="{'similar_item_warp_hover': similar.hover === index}" :src="item.imageUrl" v-on:mouseenter="similar.hover = index" v-on:mouseleave="similar.hover = -1">
                    </div>
                </div>
                <div class="swiper-pagination" slot="pagination"></div>
                <div class="swiper-button-prev" slot="button-prev"></div>
                <div class="swiper-button-next" slot="button-next"></div>
            </swiper>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Similar",
        data() {
            return {
                similar: {
                    title: "PEOPLE WHO BOUGHT THIS ITEM ALSO BOUGHT",
                    items: [
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
                        spaceBetween: 2,
                        slidesPerGroup: 2,
                        loop: false,
                        loopFillGroupWithBlank: true,
                        navigation: {
                            nextEl: '.swiper-button-next',
                            prevEl: '.swiper-button-prev'
                        }
                    }
                },
            }
        }
    }
</script>

<style scoped>
    .level {
        margin: 3% 0;
    }
    .level-item {
        border: 1px solid;
    }
    .similar_item_warp_img {
        width: 320px;
        height: 432px;
        padding: 10px;
    }
    .similar_item_warp_hover {
        width: 340px;
        height: 452px;
        padding: 0;
    }
</style>