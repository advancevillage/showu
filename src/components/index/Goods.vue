<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <!-- 新增商品 -->
                    <i-col span="2">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{languages.Actions.create[language] + languages.Merchandise[language]}}</i-button>
                    </i-col>
                    <i-col span="1">
                        <i-button style="border: none" size="small" @click="refresh"><Icon type="ios-refresh-circle-outline" /></i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">
                <Page :total="goods.total" :current="page + 1" :page-size="perPage" :page-size-opts="[30, 60, 100]" size="small" @on-change="UpdatePage" @on-page-size-change="UpdatePerPage" show-sizer></Page>
            </div>
            <div class="show">
                <i-table  size="small" border :columns="columns" :data="goods.items"></i-table>
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
                        timeout: 10,
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
                goods: {
                    total: 0,
                    items: []
                },
                columns: [
                    {
                        key: "images",width: "100px", fixed: 'left',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            let items = [];
                            for (let i = 0; i < value.length; i++) {
                                let item = {};
                                item.attrs = { src: this.$api.ImageDomain + value[i].url};
                                item.style = {
                                    width: '60px',
                                    height: '60px',
                                };
                                items.push(h("img", item));
                                break;
                            }
                            return h("div", items);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.images[this.language];
                            return h("span", this.$languages.Merchandise.images[this.language])
                        }
                    },
                    {
                        key: "name",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.name[this.language];
                            return h("span", this.$languages.Merchandise.name[this.language])
                        }
                    },
                    {
                        key: "title",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.title[this.language];
                            return h("span", this.$languages.Merchandise.title[this.language])
                        }
                    },
                    {
                        key: "description",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.description[this.language];
                            return h("span", this.$languages.Merchandise.description[this.language])
                        }
                    },
                    {
                        key: "category",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value.name[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.category[this.language];
                            return h("span", this.$languages.Merchandise.category[this.language])
                        }
                    },
                    {
                        key: "brand",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value.name[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.brand[this.language];
                            return h("span", this.$languages.Merchandise.brand[this.language])
                        }
                    },
                    {
                        key: "origin",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.origin[this.language];
                            return h("span", this.$languages.Merchandise.origin[this.language])
                        }
                    },
                    {
                        key: "rank",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.rank[this.language];
                            return h("span", this.$languages.Merchandise.rank[this.language])
                        }
                    },
                    {
                        key: "status",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            let type  = "sell";
                            switch (value) {
                                case 0x111:
                                    type = "newIn";
                                    break;
                                case 0x112:
                                    type = "sell";
                                    break;
                                case 0x113:
                                    type = "sale";
                                    break;
                                case 0x114:
                                    type = "clearance";
                                    break;
                            }
                            return h("span", this.$languages.Cycle[type][this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.status[this.language];
                            return h("span", this.$languages.Merchandise.status[this.language])
                        }
                    },
                    {
                        key: "colors",width: "140px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            let items = [];
                            for ( let i = 0; i < value.length; i++) {
                                let item = {};
                                item.style = {
                                    width: '20px',
                                    height: '20px',
                                    backgroundColor: value[i].rgb,
                                    borderRadius: '100%'
                                };
                                items.push(h("Tag", item))
                            }
                            return h("div", items);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.color[this.language];
                            return h("span", this.$languages.Merchandise.color[this.language])
                        }
                    },
                    {
                        key: "sizes",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            let items = [];
                            for ( let i = 0; i < value.length; i++) {
                                let item = {};
                                item.style = {
                                    marginRight: "4px"
                                };
                                items.push(h("span", item, value[i].value))
                            }
                            return h("div", items);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.size[this.language];
                            return h("span", this.$languages.Merchandise.size[this.language])
                        }
                    },
                    {
                        key: "stocks",width: "90px", fixed: 'right',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            let stock = 0;
                            for ( let i = 0; i < value.length; i++) {
                                stock += value[i].total;
                            }
                            return h("span", stock);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.stock[this.language];
                            return h("span", this.$languages.Merchandise.stock[this.language])
                        }
                    },
                    {
                        key: "price",width: "100px", fixed: 'right',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.price[this.language];
                            return h("span", this.$languages.Merchandise.price[this.language])
                        }
                    },
                    {
                        key: "sale",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.sale[this.language];
                            return h("span", this.$languages.Merchandise.sale[this.language])
                        }
                    },
                    {
                        key: "purchase",width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.purchase[this.language];
                            return h("span", this.$languages.Merchandise.purchase[this.language])
                        }
                    },
                    {
                        key: "newIn", width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.newIn[this.language];
                            return h("span", this.$languages.Merchandise.newIn[this.language])
                        }
                    },
                    {
                        key: "clearance", width: "100px",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key] || [];
                            return h("span", value);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Merchandise.clearance[this.language];
                            return h("span", this.$languages.Merchandise.clearance[this.language])
                        }
                    },
                ],
                page: 0,
                perPage: 30,
                data: {}
            }
        },
        mounted: function() {
            this.QueryGoods();
        },
        methods: {
            //商品
            QueryGoods: async function() {
                const params = {
                    page: this.page,
                    perPage: this.perPage
                };
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryGoods(params, headers) || {total: 0, items: []};
                this.goods.total = data.total;
                this.goods.items = data.items;
            },
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
                        this.actions.create.timeout = 10;
                        this.actions.create.confirm = false;
                    } else {
                        this.actions.create.timeout--;
                    }
                }, 1000)
            },
            refresh() {
                this.QueryGoods();
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
                this.data.stocks = colorSizeInfo.stocks;
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
            },
            UpdatePage(page) {
                this.page = page - 1;
            },
            UpdatePerPage(perPage) {
                this.perPage = perPage;
            },
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
    .page {
        margin: 5px 0;
        text-align: right;
    }
    .create_warp {
        padding: 0 16px;
    }
</style>