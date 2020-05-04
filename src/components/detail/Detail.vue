<template>
    <div>
        <Header/>
        <div id="container">
            <div class="container_warp">
                <div class="detail_banner">
                    <Banner :items="banner.items" :width="banner.width" @click="getBannerSelect"/>
                </div>
                <div class="detail_warp">
                    <div class="left">
                        <div class="color">
                            <Color :colors="goods.colors"/>
                        </div>
                        <div class="size">
                            <Size :sizes="goods.sizes"/>
                        </div>
                    </div>
                    <div class="mid">
                        <div class="top"></div>
                        <div class="center"></div>
                        <div class="bottom">
                            <div class="buttons">
                                <b-button class="add_cart">
                                    <b-icon icon="cart-plus"></b-icon>
                                </b-button>
                            </div>
                        </div>
                    </div>
                    <div class="right">
                    </div>
                </div>
                <div class="detail_other">
                    <div class="detail_thumb">
                        <Thumb :items="thumbs.items" :width="thumbs.width" :height="thumbs.height" @click="getThumbSelect"/>
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
    import Banner from '../Banner'
    import Color  from './Color'
    import Size   from './Size'
    // import Thumb  from './Thumb'
    import Thumb from "../Carousel";
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
                languages: this.$languages,
                gid: "",
                goods: {
                    colors: [],
                    sizes: [],
                    images: [],
                },
                thumbs: {
                    width: 200,
                    height: 200,
                    items: []
                },
                banner: {
                    width: document.body.clientWidth,
                    items: [{},{}, {}, {}, {}, {}]
                }
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
                for (let i = 0; i < images.length; i++) {
                    let value = {};
                    value.imageUrl = this.$api.QueryImageUrl(images[i].url);
                    this.thumbs.items.push(value);
                }
            },
            getThumbSelect(data) {
                console.log(data);
            },
            getBannerSelect(data) {
                console.log(data);
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
        height: 60%;
        position: absolute;
    }
    .detail_warp {
        z-index: 20;
        margin: 60px 0 0;
        overflow: hidden;
    }
    .detail_warp > .left, .detail_warp > .mid, .detail_warp > .right  {
        float: left;
        height: 80%;
    }
    .detail_warp > .left, .detail_warp > .right {
        width: 10%;
    }
    .detail_warp > .mid {
        width: 80%;
    }
    /*.detail_warp > .left > .color, .detail_warp > .left > .size, .detail_warp > .left > .style {*/
    /*    width: 100%;*/
    /*    height: 10%;*/
    /*}*/
    .detail_warp > .mid > .top, .detail_warp > .mid > .center, .detail_warp > .mid > .bottom {
        width: 100%;
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
        outline: none;
        border: 0;
        transition: all 150ms cubic-bezier(0.77,0,0.175,1);
        border-radius: 0.25rem;
        cursor: pointer;
        display: inline-block;
        font-weight: 500;
        text-decoration: none;
        font-size: 1.2rem;
        width: 100%;
        height: 1.5rem;
        box-shadow: none;
        font-family: serif;
        zoom: 1.5;
    }
    .detail_warp > .mid > .bottom > .buttons > .add_cart:hover {
        background: white;
    }
    .detail_other {
        width: 100%;
        /*min-height: 60px;*/
        margin-top: 620px;
        z-index: 30;
        padding: 10px 2%;
        float: left;
    }
    .detail_desc {

    }
</style>