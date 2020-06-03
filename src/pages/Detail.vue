<template>
    <div class="ss_detail">
        <div class="ss_header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13"/>
        </div>
        <div class="ss_attr" v-bind:style="{top: height * 0.15 + 'px'}">
            <TagGroup :items="goods.sizes" :width="width >> 3" :height="height * 0.05" :title="languages.GOODS.SIZE[language]"/>
            <ColorGroup :items="goods.colors" :width="width >> 3" :height="height * 0.05" :title="languages.GOODS.COLOR[language]"/>
        </div>
        <div class="ss_goods" v-bind:style="{top: height * 0.04 + 'px'}">
            <Carousel :items="goods.thumbs" :width="width" :height="height * 0.75" :action="addCart"/>
            <div class="ss_thumb">
                <Slide :items="goods.thumbs" :width="width / goods.thumbs.length" :height="height * 0.2" :step=20 />
            </div>
            <div class="ss_desc">
                <Fragment :items="goods.desc" :width="width * 0.98"/>
            </div>
            <div class="ss_similar">
                <Slide :items="similar" :width="width >> 2" :height="height * 0.5" :cpt=true :direction=true :step=150 />
            </div>
            <!-- 尾部栏 -->
            <div class="ss_footers">
                <Footer :width="width"/>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from '../components/Business/Header'
    import Carousel from "../components/Basic/Carousel";
    import Slide from "../components/Basic/Slide";
    import TagGroup from "../components/Basic/TagGroup";
    import ColorGroup from "../components/Basic/ColorGroup";
    import Fragment from "../components/Basic/Fragment";
    import Footer from "../components/Business/Footer";

    export default {
        name: "Detail",
        components: {
            Fragment,
            Footer,
            ColorGroup,
            TagGroup,
            Slide,
            Header,
            Carousel,
        },
        data() {
            return {
                languages: this.$languages,
                language: "zh_CN",
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                goods: {
                    thumbs: [],
                    sizes: [],
                    colors: [],
                    desc: []
                },
                similar: [],
                addCart: {
                    fn: this.AddCart,
                }
            }
        },
        mounted() {
            this.QueryOneGoods();
            this.QuerySimilarGoods();
        },
        methods: {
            async QuerySimilarGoods() {
                const params  = {};
                const headers = {};
                let response = await this.$api.QuerySimilarGoods(headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.similar = response.data.items;
                    console.log(this.similar);
                }
            },
            async QueryOneGoods() {
                const params  = {};
                const headers = {};
                let response = await this.$api.QueryOneGoods("", headers, params);
                if (response.hasOwnProperty("code") && parseInt(response.code) > 299) {
                    console.log(response);
                } else {
                    this.goods = response.data;
                    console.log(this.goods);
                }
            },
            AddCart() {
                //添加购物车
                console.log("add cart");
            }
        }
    }
</script>

<style scoped>
    .ss_detail {
        position: relative;
    }
    .ss_header, .ss_goods, .ss_attr {
        position: absolute;
        z-index: 5;
        left: 0;
        top: 0;
    }
    .ss_goods {
        z-index: 0;
        left: 0;
        width: 100%;
    }
    .ss_attr {
        z-index: 4;
    }
    .ss_desc, .ss_similar {
        width: 100%;
        height: 100%;
        padding: 1%;
        margin: 0;
    }
    .ss_footers {
        float: left;
        margin: 0;
        padding: 0;
    }
</style>