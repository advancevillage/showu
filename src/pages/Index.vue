<template>
    <div id="index">
        <div class="header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13" @getObject="getLanguage"/>
        </div>
        <!-- 首页Banner -->
        <div class="banner" v-bind:style="{top: height * 0.04 + 'px'}">
            <Carousel :items="banners" :width="width" :height="height * 0.75"/>
        </div>
        <!-- 新品 -->
        <div class="new" v-bind:style="{marginTop: height * 0.8 + 'px'}">
            <Split :item="{name: languages.NOUN.NEW_IN, link: '/newIns'}" :language="language" :width="width * 0.98" :height="height / 10"/>
            <Slide :items="newIns" :width="width * 0.45" :height="height >> 1" :cpt=true :direction=false :step=200 @getGoods="getGoods" />
        </div>
        <!-- 热销品 -->
        <div class="hot">
            <Split :item="{name: languages.NOUN.HOT, link: '/hots'}" :language="language" :width="width * 0.98" :height="height / 10"/>
            <Slide :items="hots" :width="width * 0.2" :height="height * 0.4" :cpt=true :direction=false :step=50 @getGoods="getGoods" />
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
    import Split    from "../components/Basic/Split";

    export default {
        name: "Index",
        components: {
            Header,
            Carousel,
            Slide,
            Split,
            Footer,
        },
        data() {
            return {
                languages: this.$languages,
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                banners: [],
                newIns: [],
                hots: [],
                language: "en"
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
            },
            getLanguage(data) {
                this.language = data.language;
            },
            getGoods(data) {
                this.$bus.$emit(this.$utils.SIG.AddCart, data);
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
        padding: 0 1%;
        margin-bottom: 1%;
    }
    .hot {
        margin-top: 0;
    }
    .ss_footers {
        float: left;
        margin: 0;
        padding: 0;
    }
</style>