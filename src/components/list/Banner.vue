<template>
    <div>
        <swiper :options="carousel" id="carousel">
            <div class="swiper-slide" v-for="item in 4" :key="item">
                <img class="image" :src="getBannerUrl(item)">
            </div>
            <div class="swiper-pagination" slot="pagination"></div>
        </swiper>
    </div>
</template>

<script>
    export default {
        name: "Banner",
        data() {
            return {
                carousel: {
                    autoplay: {
                        delay: 2000,
                        disableOnInteraction: false
                    },
                    loop: true,
                    pagination: {
                        el: ".swiper-pagination",
                        clickable: true,
                        renderBullet: function (index, className) {
                            return '<span class="' + className + '">' + (index + 1) + '</span>';
                        },
                    }
                }
            }
        },
        methods: {
            getBannerUrl (value) {
                return `https://picsum.photos/id/43${value}/1230/500`
            }
        }
    }
</script>

<style scoped>
    .image {
        width: 100%;
        height: 200px;
    }
</style>