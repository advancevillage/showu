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
            <span>NewIn</span>
            <Slide :items="newIns" :width="width * 0.45" :height="height >> 1" :step=200 />
        </div>
        <!-- 热销品 -->
        <div class="hot">
            <span>NewIn</span>
            <Slide :items="hots" :width="width * 0.2" :height="height >> 2" :step=15 />
        </div>
        <!-- 尾部栏 -->
        <div class="ss_footers">
            <Footer :width="width"/>
        </div>
    </div>
</template>

<script>
    import Header   from "../components/Business/Header";
    import Carousel from "../components/Basic/Carousel";
    import Slide    from "../components/Basic/Slide";
    import Footer   from "../components/Business/Footer";

    export default {
        name: "Index",
        components: {
            Header,
            Carousel,
            Slide,
            Footer,
        },
        data() {
            return {
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                banners: [],
                newIns: [],
                hots: []
            }
        },
        mounted() {
            this.QueryBanners();
            this.QueryNewIns();
            this.QueryHots();
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
            },
            async QueryHots() {
                const params  = {};
                const headers = {};
                let response = await this.$api.QueryHots(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.hots = response.data.items;
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
    .new, .hot {
        float: left;
        width: 100%;
        margin-top: 80%;
    }
    .hot {
        margin-top: 0;
    }
    .new > span, .hot > span {
        display: inline-block;
        width: 98%;
        text-align: center;
        border-bottom: 2px solid darkgray;
        margin: 1% 1% 0;
        font-size: x-large;
        letter-spacing: 2px;
        font-family: monospace;
        text-transform:uppercase;
    }
    .ss_footers {
        float: left;
        margin: 0;
        padding: 0;
    }
</style>