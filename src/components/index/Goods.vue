<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <!-- 新增商品 -->
                    <i-col span="6">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{languages.Actions.create[language] + languages.Merchandise[language]}}</i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">

            </div>
            <div class="show">
            </div>
            <!-- 新增商品 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Merchandise[language]" width="700">
                    <div class="create">
                        <Tabs name="goods" type="card" class="create_warp" v-model="actions.create.pos">
                            <TabPane v-for="(item, index) in actions.process" :key="index" :label="languages.Merchandise[item.value][language]" tab="goods">
                                <div v-if="item.key === 0x1011" class="basic">
                                    <Basic :language="language" v-on:basicInfo="basicInfo"/>
                                </div>
                                <div v-if="item.key === 0x1012" class="category">
                                    <Category :language="language" v-on:categoryInfo="categoryInfo"/>
                                </div>
                                <div v-if="item.key === 0x1013" class="color_size">
                                    <ColorSize :language="language" v-on:colorSizeInfo="colorSizeInfo"/>
                                </div>
                                <div v-if="item.key === 0x1014" class="brand">
                                    <Brand :language="language" v-on:brandInfo="brandInfo"/>
                                </div>
                                <div v-if="item.key === 0x1015" class="images">
                                    <Images :language="language" v-on:imagesInfo="imagesInfo"/>
                                </div>
                                <div v-if="item.key === 0x1016" class="price">
                                    <Price :language="language" v-on:priceInfo="priceInfo"/>
                                </div>
                            </TabPane>
                        </Tabs>
                    </div>
                    <div slot="footer">
                        <Row>
                            <i-col>
                                <i-button v-if="actions.create.pos === 0" type="default"
                                          @click="actions.create.modal = false">{{languages.Actions.cancel[language]}}</i-button>
                                <i-button v-if="actions.create.pos > 0" type="default"
                                          @click="actions.create.pos = actions.create.pos - 1">{{languages.Actions.previous[language]}}</i-button>
                                <i-button v-if="actions.create.pos < actions.process.length -1 " type="primary"
                                          @click="actions.create.pos = actions.create.pos + 1">{{languages.Actions.next[language]}}</i-button>
                                <i-button v-if="actions.create.pos === actions.process.length -1" type="primary" :class="{disabled: this.actions.create.confirm}"
                                          @click="CreateGoods">
                                    <span v-if="!actions.create.confirm">{{languages.Actions.confirm[language]}}</span>
                                    <span v-else>{{this.actions.create.timeout}}</span>
                                </i-button>
                            </i-col>
                        </Row>
                    </div>
                </Modal>
            </div>
        </div>
    </div>
</template>

<script>
    import Basic     from '../goods/Basic'
    import Brand     from '../goods/Brand'
    import Category  from '../goods/Category'
    import ColorSize from '../goods/ColorSize'
    import Images    from '../goods/Images'
    import Price     from '../goods/Price'

    export default {
        name: "Goods",
        components: {
            Basic,
            Category,
            ColorSize,
            Brand,
            Images,
            Price
        },
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                actions: {
                    create: {
                        modal: false,
                        pos: 0,
                        confirm: false,
                        timeout: 60,
                    },
                    process: [
                        {key: 0x1011, value: "basic"},
                        {key: 0x1012, value: "category"},
                        {key: 0x1013, value: "color_size"},
                        {key: 0x1014, value: "brand"},
                        {key: 0x1015, value: "images"},
                        {key: 0x1016, value: "price"}
                    ],
                },
                data: {}
            }
        },
        methods: {
            //商品
            CreateGoods: async function() {
                if (this.actions.create.confirm) {
                    return
                }
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.CreateGoods(this.data, headers);
                this.interceptor(data);
            },
            interceptor(data) {
                switch (data.code) {
                    case 200:
                        this.$Message.success(data.message);
                        this.actions.create.confirm = true;
                        this.delay();
                        break;
                    default:
                        this.$Message.error(data.message);
                }
            },
            delay() {
                if (!this.actions.create.confirm) {
                    return
                }
                let clock = window.setInterval( () => {
                    if (this.actions.create.timeout < 1) {
                        window.clearInterval(clock);
                        this.actions.create.timeout = 60;
                        this.actions.create.confirm = false;
                    } else {
                        this.actions.create.timeout--;
                    }
                }, 1000)
            },
            basicInfo: function (basicInfo) {
                this.data.name  = basicInfo.name;
                this.data.title = basicInfo.title;
                this.data.rank  = basicInfo.rank;
                this.data.tags  = basicInfo.tags;
                this.data.keywords  = basicInfo.keywords;
                this.data.description = basicInfo.description;
            },
            categoryInfo: function (categoryInfo) {
                this.data.category = categoryInfo;
            },
            colorSizeInfo: function (colorSizeInfo) {
                this.data.colors = colorSizeInfo.colors;
                this.data.sizes  = colorSizeInfo.sizes;
                this.data.stock  = colorSizeInfo.stock;
            },
            brandInfo: function (brandInfo) {
                this.data.brand = brandInfo.brand;
                this.data.origin = brandInfo.origin;
                this.data.materials = brandInfo.materials;
                this.data.manufacturer = brandInfo.manufacturer;
            },
            imagesInfo: function (imagesInfo) {
                this.data.images = imagesInfo;
            },
            priceInfo: function (priceInfo) {
                this.data.purchase  = priceInfo.purchase;
                this.data.price     = priceInfo.price;
                this.data.newIn     = priceInfo.newIn;
                this.data.sale      = priceInfo.sale;
                this.data.clearance = priceInfo.clearance;
                this.data.status    = priceInfo.status;
            }
        }
    }
</script>

<style scoped>
    .warp, .operate, .show {
        width: 100%;
        padding: 0 5px;
    }
    .operate {
        height: 60px;
    }
    .create {
        margin: 5% 0;
    }
    .create_warp {
        padding: 0 16px;
    }
</style>