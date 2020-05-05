<template>
    <div>
        <Selector :items="selector.items" :width="selector.width" :height="selector.height" :styles="selector.styles" @get="getCountry"/>
        <TagGroup :items="sizes.items" :width="sizes.width" @get="getSizes"/>
        <ColorGroup :items="colors.items" :width="colors.width" @get="getColors"/>
        <Carousel :items="banner.items" :width="banner.width" :height="banner.height" @get="getBanner"/>
        <Slide :items="slides.items" :width="slides.width" :height="slides.height" @get="getSlide"/>
        <Number :title="number.price" :max="number.max" :min="number.min"/>
    </div>
</template>

<script>
    import Selector from "../components/Basic/Selector";
    import TagGroup from "../components/Basic/TagGroup";
    import ColorGroup from "../components/Basic/ColorGroup";
    import Carousel from "../components/Basic/Carousel";
    import Slide from "../components/Basic/Slide";
    import Number from "../components/Basic/Number";

    export default {
        name: "Index",
        components: {
            Carousel,
            Selector,
            TagGroup,
            ColorGroup,
            Slide,
            Number,
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
                        {name: "11", value: "#ffffff",selected: false}
                    ],
                    width: 200
                },
                banner: {
                    width: 1440,
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
        }
    }
</script>

<style scoped>

</style>