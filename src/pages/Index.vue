<template>
    <div id="index">
        <div class="header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13"/>
        </div>
        <!-- 首页Banner -->
        <div class="banner" v-bind:style="{top: height * 0.04 + 'px'}">
            <Carousel :items="banners" :width="width" :height="height * 0.75"/>
        </div>
        <!-- 新品 -->
        <div class="new" v-bind:style="{marginTop: height * 0.8 + 'px'}">
            <Slide :items="newIns" :width="width * 0.45" :height="height >> 1"/>
        </div>
        <!-- 热销品 -->
        <!-- 尾部栏 -->
    </div>
</template>

<script>
    import Header   from "../components/Business/Header";
    import Carousel from "../components/Basic/Carousel";
    import Slide    from "../components/Basic/Slide";

    export default {
        name: "Index",
        components: {
            Header,
            Carousel,
            Slide,
        },
        data() {
            return {
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                banners: [],
                newIns: []
            }
        },
        mounted() {
            this.QueryBanners();
            this.QueryNewIns();
        },
        methods: {
            async QueryBanners() {
                const params  = {};
                const headers = {};
                let response = await this.$api.QueryBanners(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.banners = response.data.items;
                }
            },
            async QueryNewIns() {
                const params  = {};
                const headers = {};
                let response = await this.$api.QueryNewIns(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.newIns = response.data.items;
                }
            }
        }
    }
</script>

<style scoped>
    .header, .banner {
        position: absolute;
        z-index: 5;
    }
    .banner {
        z-index: 0;
        left: 0;
    }
    .new {
        float: left;
        width: 100%;
        margin-top: 80%;
    }
</style>