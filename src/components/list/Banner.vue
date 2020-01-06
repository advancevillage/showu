<template>
    <div>
        <b-carousel
            :arrow="banner.arrow"
            :pause-info="banner.pauseInfo"
            :pause-hover="banner.pauseHover"
            :indicator-mode="banner.indicatorMode"
            :indicator-style="banner.indicatorStyle"
            :indicator-inside="banner.indicatorInside">
            <b-carousel-item v-for="(item, i) in 6" :key="i">
            <span>
                <img class="image" :src="getBannerUrl(i)">
            </span>
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
                    indicator: true,
                    indicatorInside: true,
                    indicatorMode: 'hover',
                    indicatorPosition: 'is-top',
                    indicatorStyle: 'is-lines',
                    pauseInfo: false,
                    pauseHover: false,
                    arrow: false
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