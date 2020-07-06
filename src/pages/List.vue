<template>
    <div id="list">
        <div class="ss_header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13" :opacity=false />
        </div>
        <div class="ss_content">
             <div class="ss_banner">
                 <Carousel :items="banners" :width="width * 0.98" :height="height * 0.25"/>
             </div>
            <div class="ss_filter">
                <TagGroup :items="sizes" :width="width / 5" />
                <TagGroup :items="sizes" :width="width / 5" />
                <TagGroup :items="sizes" :width="width / 5" />
                <TagGroup :items="sizes" :width="width / 5" />
                <ColorGroup :items="colors" :width="width / 5" />
            </div>
            <div class="ss_list">
                <div class="ss_goods" v-for="(item, index) in goods" :key="index">
                    <Goods :item="item" :width="width >> 2" @get="getGoods"/>
                </div>
            </div>
        </div>
        <!-- 尾部栏 -->
        <div class="ss_footers">
            <Footer :width="width"/>
        </div>
    </div>
</template>

<script>
    import Header   from "../components/Business/Header";
    import Footer   from "../components/Business/Footer";
    import Carousel from "../components/Basic/Carousel";
    import TagGroup from "../components/Basic/TagGroup";
    import ColorGroup from "../components/Basic/ColorGroup";
    import Goods from "../components/Business/Goods";

    export default {
        name: "List",
        components: {
            Goods,
            ColorGroup,
            TagGroup,
            Header,
            Footer,
            Carousel,
        },
        data() {
            return {
                languages: this.$languages,
                language: "en",
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                banners: [],
                sizes: [],
                colors: [],
                goods: []
            }
        },
        mounted() {
            this.QueryBanners();
            this.QuerySizes();
            this.QueryColors();
            this.QueryGoods();
        },
        methods: {
            async QueryBanners() {
                const params  = {
                    pos: "list",
                    cat: 1111,
                };
                const headers = {};
                let response = await this.$api.QueryBanners(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.banners = response.data.items;
                }
            },
            async QuerySizes() {
                const params  = {
                    pos: "list",
                    cat: 1111,
                };
                const headers = {};
                let response = await this.$api.QuerySizes(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.sizes = response.data.items;
                }
            },
            async QueryColors() {
                const params  = {
                };
                const headers = {};
                let response = await this.$api.QueryColors(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.colors = response.data.items;
                }
            },
            async QueryGoods() {
                const params  = {
                };
                const headers = {};
                let response = await this.$api.QueryGoods(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.goods = response.data.items;
                }
            },
            getGoods(data) {
                this.$bus.$emit(this.$utils.SIG.AddCart, data);
            }
        }
    }
</script>

<style scoped>
    .ss_header, .ss_footers, .ss_content{
        float: left;
    }
    .ss_content {
        width: 100%;
        height: 100%;
        padding: 1%;
    }
    .ss_filter, .ss_list {
        float: left;
        height: 100%;
    }
    .ss_filter {
        width: 21%;
    }
    .ss_filter > div {
        margin: 1% 0 0;
    }
    .ss_list {
        width: 79%;
    }
    .ss_goods {
        float: left;
        margin: 0.5% 0.5% 0;
    }
</style>