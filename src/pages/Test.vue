<template>
    <div>
        <TagGroup :items="sizes.items" :width="sizes.width" @get="getSizes"/>
        <Selector :items="selector.items" :width="selector.width" :height="selector.height" :styles="selector.styles" @get="getCountry"/>
        <Menu/>
<!--        <ImageListGroup/>-->
        <Address/>
        <Goods :item="goods" @get="getGoods"/>
        <Goods :item="goods" @get="getGoods"/>
        <ColorGroup :items="colors.items" :width="colors.width" @get="getColors"/>
        <Carousel :items="banner.items" :width="banner.width" :height="banner.height" @get="getBanner"/>
        <Slide :items="slides.items" :width="slides.width" :height="slides.height" @get="getSlide"/>
        <Number :title="number.price" :max="number.max" :min="number.min"/>
<!--        <ListGroup :items="lists.items" :width="lists.width"/>-->
        <Notice :items="notice.items" :countries="selector.items" @getLanguage="getSlide"/>
    </div>
</template>

<script>
    import Selector from "../components/Basic/Selector";
    import TagGroup from "../components/Basic/TagGroup";
    import ColorGroup from "../components/Basic/ColorGroup";
    import Carousel from "../components/Basic/Carousel";
    import Slide from "../components/Basic/Slide";
    import Number from "../components/Basic/Number";
    // import ListGroup from "../components/Basic/ListGroup";
    import Notice from "../components/Business/Notice";
    import Menu   from "../components/Business/Menu"
    import Goods from "../components/Business/Goods";
    import Address from "../components/Business/Address"
    // import ImageListGroup from "../components/Basic/ImageListGroup";

    export default {
        name: "Index",
        components: {
            Carousel,
            Selector,
            TagGroup,
            ColorGroup,
            Slide,
            Number,
            // ListGroup,
            Notice,
            Menu,
            Goods,
            Address,
            // ImageListGroup,
        },
        data() {
            return {
                selector: {
                    items: [{value: "CN"}, {value: "EN"}, {value: "日本"}, {value: "韩国"}],
                    width: 60,
                    height: 20,
                    styles: {
                        width: '100%',
                        height: '30px',
                    }
                },
                sizes: {
                    items: [
                        { value: "1111",  selected: false},
                        { value: "12222", selected:false},
                        { value: "11111", selected: false},
                        { value: "1111",  selected: false},
                        { value: "12222", selected:false},
                        { value: "11111", selected: false},
                        { value: "1111",  selected: false},
                        { value: "12222", selected:false},
                        { value: "11111", selected: false},
                        { value: "1111",  selected: false},
                        { value: "12222", selected:false},
                        { value: "11111", selected: false},
                    ],
                    width: 200
                },
                colors: {
                    items: [
                        {name: "11", value: "#100000",selected: true},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#101100",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100ff0",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#1ff000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#ffffff",selected: false},
                        {name: "11", value: "#100000",selected: true},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#101100",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100ff0",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#1ff000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#ffffff",selected: false},
                        {name: "11", value: "#100000",selected: true},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#101100",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100ff0",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#1ff000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#ffffff",selected: false},
                        {name: "11", value: "#100000",selected: true},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#101100",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#100ff0",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#1ff000",selected: false},
                        {name: "11", value: "#100000",selected: false},
                        {name: "11", value: "#ffffff",selected: false}
                    ],
                    width: 200
                },
                banner: {
                    width: 1440,
                    height: 600,
                    items: [
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                    ]
                },
                slides: {
                    width: 200,
                    height: 200,
                    items: [
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                        {imageUrl: "https://i1.mifile.cn/a4/xmad_15535933141925_ulkYv.jpg"},
                    ]
                },
                number: {
                    width: 200,
                    height: 200,
                    min: 50,
                    max: 999,
                    price: "price"
                },
                lists: {
                    items: [
                        { value: "中国", fn: function (data) {
                                console.log(data);
                            }},
                        { value: "开宝", link: "/"},
                        { value: "Kelly", link: "/"},
                        { value: "Richard", link: "/"},
                    ],
                    width: 100,
                },
                notice: {
                    items: [
                        {value: "111444中国你好111444中国你好", link: "/", icon: "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg"},
                        {value: "222", icon: ""},
                        {value: "333", link: "/", icon: ""},
                        {value: "444中国你好", link: "/", icon: ""}
                    ],
                },
                goods: {
                    name: {en: "name"},
                    price: 123.5,
                    statePrice: 110,
                    imageUrl: "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588874077730&di=0e1ff22a90f71e9d2796205339940f21&imgtype=0&src=http%3A%2F%2Fbpic.588ku.com%2Felement_origin_min_pic%2F18%2F03%2F18%2Ff7ae017d4c92a900869d91a83e9f6161.jpg",
                    backImageUrl: "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                    state: 0,
                    nextState: 1,
                    stateImageUrl: "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1589603852944&di=a280d4108abcb3a807ff81f23e742299&imgtype=0&src=http%3A%2F%2Fpic1.16pic.com%2F00%2F24%2F54%2F16pic_2454237_b.jpg",
                    colors: [
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#aabbcc"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ff0000"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#aabbcc"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ff0000"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#ffff00"},
                        {name: {en: "en", zh_CN: "zh_CN"}, rgb: "#aabbcc"},
                    ],
                    sizes: [
                        "XSS", "XS", "S", "M", "L", "XL", "XLL"
                    ]
                }
            }
        },
        methods: {
            getCountry(data) {
                console.log(data);
            },
            getSizes(data) {
                console.log(data);
            },
            getColors(data) {
                console.log(data);
            },
            getBanner(data) {
                console.log(data);
            },
            getSlide(data) {
                console.log(data);
            },
            getGoods(data) {
                console.log(data);
            }
        }
    }
</script>

<style scoped>

</style>