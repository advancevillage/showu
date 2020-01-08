<template>
    <div>
        <b-carousel
                :indicator="banner.indicator"
                :autoplay="banner.autoplay"
                :arrow="banner.arrow"
                :pause-info="banner.pauseInfo"
                :pause-hover="banner.pauseHover"
                :indicator-mode="banner.indicatorMode"
                :indicator-style="banner.indicatorStyle"
                :indicator-inside="banner.indicatorInside">
            <b-carousel-item>
            <a href="/detail">
                <img class="image" :src="getBannerUrl()">
            </a>
            </b-carousel-item>
        </b-carousel>
    </div>
</template>

<script>
    export default {
        name: "Banner",
        data() {
            return {
                banner: {
                    indicator: false,
                    indicatorInside: true,
                    indicatorMode: 'hover',
                    indicatorPosition: 'is-top',
                    indicatorStyle: 'is-lines',
                    pauseInfo: false,
                    pauseHover: false,
                    arrow: false,
                    autoplay: false
                }
            }
        },
        methods: {
            getBannerUrl () {
                return `https://picsum.photos/id/435/1230/500`
            }
        }
    }
</script>

<style scoped>
    .image {
        width: 100%;
        height: 640px;
    }
</style>