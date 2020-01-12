<template>
    <div>
        <div id="container">
            <!-- 商品业务中台 -->
            <b-tabs type="is-toggle" expanded>
                <b-tab-item v-for="item in tabs" :key="item.key" :label="item.value" class="mms">
                    <div v-if="item.key === '0x1'" class="goods">
                        <Goods/>
                    </div>
                    <div v-if="item.key === '0x2'" class="category">
                        <Category/>
                    </div>
                    <div v-if="item.key === '0x3'" class="color">
                        <Color/>
                    </div>
                    <div v-if="item.key === '0x4'" class="images">
                        <Images/>
                    </div>
                    <div v-if="item.key === '0x5'" class="size">
                        <Size/>
                    </div>
                    <div v-if="item.key === '0x6'" class="tag">
                        <Tag/>
                    </div>
                    <div v-if="item.key === '0x7'" class="brand">
                        <Brand/>
                    </div>
                    <div v-if="item.key === '0x9'" class="style">
                        <Style/>
                    </div>
                </b-tab-item>
            </b-tabs>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Footer from '../common/Footer'
    import Brand  from './Brand'    //品牌管理
    import Color  from './Color'    //颜色管理
    import Size   from './Size'     //尺码管理
    import Category from './Category' //分类管理
    import Goods  from './Goods'
    import Images from './Image'    //商品管理
    import Tag    from './Tag'      //标签管理
    import Style  from './Style'    //款式管理


    export default {
        data() {
            return {
                tabs: [
                    {key: "0x1", value: "商品"},
                    {key: "0x2", value: "分类"},
                    {key: "0x3", value: "颜色"},
                    {key: "0x4", value: "图片"},
                    {key: "0x5", value: "尺码"},
                    {key: "0x6", value: "标签"},
                    {key: "0x7", value: "品牌"},
                    {key: "0x8", value: "生产商"},
                    {key: "0x9", value: "款式"}

                ]
            }
        },
        name: "Index",
        components: {
            Images,
            Footer,
            Brand,
            Color,
            Size,
            Category,
            Goods,
            Tag,
            Style
        },
        methods: {

        }
    }
</script>

<style scoped>
    .mms {
        margin: 0;
        padding: 0;
        width: 100%;
        border: 1px solid red;
        min-height: 1024px;
    }
</style>