<template>
    <div>
        <Header/>
        <div id="container">
            <div class="container_warp">
                <div class="detail_banner">
                    <Banner/>
                </div>
                <div class="detail_warp">
                    <div class="left">
                        <div class="color">
                            <Color :colors="goods.colors"/>
                        </div>
                        <div class="size">
                            <Size :sizes="goods.sizes"/>
                        </div>
                        <div class="style">
                            <Style/>
                        </div>
                    </div>
                    <div class="mid">
                        <div class="top"></div>
                        <div class="center"></div>
                        <div class="bottom">
                            <div class="buttons">
                                <b-button class="add_cart" expanded>ADD TO BAG</b-button>
                            </div>
                        </div>
                    </div>
                    <div class="right">
                    </div>
                </div>
                <div class="detail_other">
                    <div class="detail_thumb">
                        <Thumb :thumbs="thumbs"/>
                    </div>
                    <div class="detail_desc">
                        <Description/>
                    </div>
                    <div class="detail_similar">
                        <Similar/>
                    </div>
                    <div class="detail_comment">
                        <Similar/>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from '../common/Header'
    import Footer from '../common/Footer'
    import Banner from './Banner'
    import Color  from './Color'
    import Size   from './Size'
    import Style  from './Style'
    import Thumb  from './Thumb'
    import Similar from './Similar'
    import Description   from './Description'

    export default {
        name: "Detail",
        components: {
            Header,
            Footer,
            Banner,
            Color,
            Size,
            Style,
            Thumb,
            Description,
            Similar
        },
        created() {
            this.gid = this.$route.query.gid || "";
        },
        data() {
            return {
                language: "chinese",
                gid: "",
                goods: {
                    colors: [],
                    sizes: [],
                    images: [],
                },
                thumbs: []
            }
        },
        mounted() {
            if (this.gid.length <= 0) {
                this.$router.push({path: '/404'})
                    .then(() => {
                        this.$router.go(1);
                    })
                    .catch(() => {
                        this.$router.go(-1);
                    });

            } else {
                this.QueryOneGoods();
            }
        },
        methods: {
            QueryOneGoods: async function() {
                const params = {};
                const headers = {
                    "x-language": this.language
                };
                this.goods = await this.$api.QueryOneGoods(this.gid, params, headers) || {};
                let images = this.goods.images || [];
                this.thumbs = [];
                for (let i = 0; i < images.length; i++) {
                    let value = {};
                    value.image = this.$api.QueryImageUrl(images[i].url);
                    this.thumbs.push(value);
                }
            }
        }
    }
</script>

<style scoped>
    .container_warp {
        width: 100%;
        float: left;
    }
    .detail_banner, .detail_warp {
        width: 100%;
        z-index: 5;
        height: 640px;
        position: absolute;
    }
    .detail_warp {
        z-index: 20;
        margin: 60px 0 0;
        overflow: hidden;
    }
    .detail_warp > .left, .detail_warp > .mid, .detail_warp > .right  {
        float: left;
        height: 100%;
    }
    .detail_warp > .left, .detail_warp > .right {
        width: 10%;
    }
    .detail_warp > .mid {
        width: 80%;
    }
    .detail_warp > .left > .color, .detail_warp > .left > .size, .detail_warp > .left > .style {
        width: 100%;
        height: 10%;
    }
    .detail_warp > .left > .color {
        height: 20%;
    }
    .detail_warp > .mid > .top, .detail_warp > .mid > .center, .detail_warp > .mid > .bottom {
        width: 100%;
        height: 10%;
    }
    .detail_warp > .mid > .center {
        height: 60%;
    }
    .detail_warp > .mid > .bottom > .buttons {
        margin: 0 40%;
    }
    .detail_warp > .mid > .bottom > .buttons > .add_cart {
        margin: 0;
        padding: 0;
        background: darkgray;
    }
    .detail_warp > .mid > .bottom > .buttons > .add_cart:hover {
        background: white;
    }
    .detail_other {
        width: 100%;
        min-height: 640px;
        margin-top: 640px;
        padding: 10px 2%;
        float: left;
    }
    .detail_desc {

    }
</style>