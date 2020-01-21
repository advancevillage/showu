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
                                    <Form :model="actions.create.basic" :label-width="100">
                                        <!--商品名称-->
                                        <FormItem :label="languages.Merchandise.name[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-input v-model="actions.create.basic.name[language]" :placeholder="language" maxlength="50" show-word-limit></i-input>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                        <!--商品标题-->
                                        <FormItem :label="languages.Merchandise.title[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-input v-model="actions.create.basic.title[language]" :placeholder="language" maxlength="100" show-word-limit type="textarea"></i-input>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                        <!--商品描述-->
                                        <FormItem :label="languages.Merchandise.description[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-input v-model="actions.create.basic.description[language]" :placeholder="language" maxlength="300" show-word-limit type="textarea"></i-input>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                        <!--商品关键字-->
                                        <FormItem :label="languages.Merchandise.keyword[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-input v-model="actions.create.basic.keyword[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateKeyword"></i-input>
                                                </i-col>
                                                <i-col span="4" class="keyword">
                                                    <Tag v-for="(item,index) in actions.create.basic.keywords" :key="index">{{item[language]}}<Icon type="ios-close" @click="DeleteKeyword(index)"/></Tag>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                        <!--商品标签-->
                                        <FormItem :label="languages.Merchandise.tag[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-input v-model="actions.create.basic.tag[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateTag"></i-input>
                                                </i-col>
                                                <i-col span="4" class="tag">
                                                    <Tag v-for="(item,index) in actions.create.basic.tags" :key="index">{{item[language]}}<Icon type="ios-close" @click="DeleteTag(index)"/></Tag>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                        <!--商品排位-->
                                        <FormItem :label="languages.Merchandise.rank[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <i-select v-model="actions.create.basic.rank">
                                                        <i-option v-for="index in actions.create.basic.rank" :value="index" :key="index">{{index}}</i-option>
                                                    </i-select>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                    </Form>
                                </div>
                                <div v-if="item.key === 0x1012" class="category">
                                    <Form :model="actions.create.basic" :label-width="100">
                                        <FormItem :label="languages.Merchandise.category[language]">
                                            <Row>
                                                <i-col span="20">
                                                    <Cascader :data="actions.categories.items" change-on-select @on-change="handleCategory"></Cascader>
                                                </i-col>
                                            </Row>
                                        </FormItem>
                                    </Form>
                                </div>
                                <div v-if="item.key === 0x1013" class="color_size">
                                    <div class="color">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="6">
                                                <span>{{languages.Merchandise.color[language]}}</span>
                                                <i-button size="small" class="add" icon="ios-add-circle-outline" style="border: none" @click="actions.colors.modal = true"></i-button>
                                            </i-col>
                                        </Row>
                                        <CheckboxGroup v-model="actions.create.basic.colors">
                                            <Checkbox v-for="(item, index) in actions.colors.items" :label="index" :key="index" size="small" v-bind:style="{width: '70px', marginBottom: '5px'}">
                                                <Tooltip placement="top">
                                                    <i-button class="add" v-bind:style="{width: '20px', height: '20px', padding: 0}">{{item.name[language]}}</i-button>
                                                    <i-button slot="content" class="add" v-bind:style="{width: '20px', height: '20px', padding: 0, borderRadius: '100%', backgroundColor:item.rgb}"></i-button>
                                                </Tooltip>
                                            </Checkbox>
                                        </CheckboxGroup>
                                    </div>
                                    <div class="size">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="3">
                                                <span>{{languages.Merchandise.size[language]}}</span>
                                            </i-col>
                                            <i-col span="5">
                                                <i-select size="small" v-model="actions.sizes.group" @on-change="QuerySizes">
                                                    <i-option v-for="(item, index) in actions.sizes.groups" :value="item" :key="index" :label="languages.Size[item][language]"></i-option>
                                                </i-select>
                                            </i-col>
                                        </Row>
                                        <CheckboxGroup v-model="actions.create.basic.sizes">
                                            <Checkbox v-for="(item, index) in actions.sizes.items" :value="index" :key="index" :label="index" size="small" v-bind:style="{width: '70px', marginBottom: '5px'}">
                                                {{item.value}}
                                            </Checkbox>
                                        </CheckboxGroup>
                                    </div>
                                    <div class="stock">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="4">
                                                <span>{{languages.Merchandise.stock[language]}}</span>
                                                <i-button size="small" class="add" icon="ios-refresh-circle" style="border: none" @click="handleStock"></i-button>
                                            </i-col>
                                        </Row>
                                        <i-table row-key="id" height="140" size="small" border :columns="actions.stock.columns" :data="actions.stock.data"></i-table>
                                    </div>
                                </div>
                                <div v-if="item.key === 0x1014" class="brand">
                                    <Row v-bind:style="{marginBottom: '10px'}">
                                        <i-col span="3">
                                            <span>{{languages.Merchandise.brand[language]}}</span>
                                        </i-col>
                                        <i-col span="8">
                                            <i-select size="small" v-model="actions.create.basic.brand">
                                                <i-option v-for="(item, index) in actions.brands.items" :value="index" :key="index" :label="item.name[language]"></i-option>
                                            </i-select>
                                        </i-col>
                                    </Row>
                                    <Row v-bind:style="{marginBottom: '10px'}">
                                        <i-col span="3">
                                            <span>{{languages.Merchandise.manufacturer[language]}}</span>
                                        </i-col>
                                        <i-col span="8">
                                            <i-select size="small" v-model="actions.create.basic.manufacturer" @on-change="actions.manufacturers.current = actions.manufacturers.items[actions.create.basic.manufacturer]">
                                                <i-option v-for="(item, index) in actions.manufacturers.items" :value="index" :key="index" :label="item.name[language]"></i-option>
                                            </i-select>
                                        </i-col>
                                        <i-col span="3">
                                            <i-button size="small" class="add" icon="ios-add-circle-outline" style="border: none"></i-button>
                                        </i-col>
                                    </Row>
                                    <div v-bind:style="{marginLeft: '12%'}">
                                        <Row>
                                            <i-col span="8">
                                                <Tag>{{languages.Manufacturer.name[language]}}:
                                                    {{actions.manufacturers.current.name[language]}}
                                                </Tag>
                                            </i-col>
                                        </Row>
                                        <Row>
                                            <i-col span="8">
                                                <Tag>
                                                    {{languages.Manufacturer.contact[language]}}:
                                                    {{actions.manufacturers.current.contact}}
                                                </Tag>
                                            </i-col>
                                        </Row>
                                        <Row>
                                            <i-col span="8">
                                                <Tag>
                                                    {{languages.Manufacturer.email[language]}}:
                                                    {{actions.manufacturers.current.contactEmail}}
                                                </Tag>
                                            </i-col>
                                        </Row>
                                        <Row>
                                            <i-col span="8">
                                                <Tag>
                                                    {{languages.Manufacturer.phone[language]}}:
                                                    {{actions.manufacturers.current.contactPhone}}
                                                </Tag>
                                            </i-col>
                                        </Row>
                                        <Row>
                                            <i-col span="8">
                                                <Tag>
                                                    {{languages.Manufacturer.address[language]}}:
                                                    {{actions.manufacturers.current.address[language]}}
                                                </Tag>
                                            </i-col>
                                        </Row>
                                    </div>
                                    <Row v-bind:style="{marginBottom: '10px', marginTop: '10px'}">
                                        <i-col span="3">
                                            <span>{{languages.Merchandise.origin[language]}}</span>
                                        </i-col>
                                        <i-col span="16">
                                            <span>{{actions.manufacturers.current.address[language]}}</span>
                                        </i-col>
                                    </Row>
                                    <Row v-bind:style="{marginBottom: '10px'}">
                                        <i-col span="3">
                                            <span>{{languages.Merchandise.material[language]}}</span>
                                        </i-col>
                                        <i-col span="8">
                                            <i-input size="small" v-model="actions.create.basic.material[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateMaterial"></i-input>
                                        </i-col>
                                        <i-col span="4" class="material">
                                            <Tag  v-for="(item,index) in actions.create.basic.materials" :key="index">{{item[language]}}<Icon type="ios-close" @click="DeleteMaterial(index)"/></Tag>
                                        </i-col>
                                    </Row>
                                </div>
                                <div v-if="item.key === 0x1015" class="images">
                                    <div v-bind:style="{'float': 'left', 'width': '40%'}">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="6">
                                                <span>{{languages.Images.main_front[language]}}</span>
                                            </i-col>
                                        </Row>
                                        <div class="upload_list" v-for="item in actions.uploads.items" :key="item.uid">
                                            <template v-if="item.status === 'finished'">
                                                <img :src="item.url">
                                                <div class="upload_list_cover">
                                                    <Icon type="ios-eye-outline"></Icon>
                                                    <Icon type="ios-trash-outline"></Icon>
                                                </div>
                                            </template>
                                            <template v-else>
                                                <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                                            </template>
                                        </div>
                                        <Upload
                                                ref="upload"
                                                :show-upload-list="false"
                                                :format="['jpg','jpeg','png']"
                                                :max-size="2048"
                                                :on-progress="handleUpload"
                                                :on-success="uploadSuccess"
                                                multiple
                                                type="drag"
                                                action="//jsonplaceholder.typicode.com/posts/"
                                                style="display: inline-block;width:128px;">
                                            <div style="width: 128px;height:128px;line-height: 128px;">
                                                <Icon type="ios-camera" size="128"></Icon>
                                            </div>
                                        </Upload>
                                    </div>
                                    <div v-bind:style="{'float': 'left', 'width': '40%'}">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="6">
                                                <span>{{languages.Images.main_back[language]}}</span>
                                            </i-col>
                                        </Row>
                                        <div class="upload_list" v-for="item in actions.uploads.items" :key="item.uid">
                                            <template v-if="item.status === 'finished'">
                                                <img :src="item.url">
                                                <div class="upload_list_cover">
                                                    <Icon type="ios-eye-outline"></Icon>
                                                    <Icon type="ios-trash-outline"></Icon>
                                                </div>
                                            </template>
                                            <template v-else>
                                                <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                                            </template>
                                        </div>
                                        <Upload
                                                ref="upload"
                                                :show-upload-list="false"
                                                :format="['jpg','jpeg','png']"
                                                :max-size="2048"
                                                :on-progress="handleUpload"
                                                :on-success="uploadSuccess"
                                                multiple
                                                type="drag"
                                                action="//jsonplaceholder.typicode.com/posts/"
                                                style="display: inline-block;width:128px;">
                                            <div style="width: 128px;height:128px;line-height: 128px;">
                                                <Icon type="ios-camera" size="128"></Icon>
                                            </div>
                                        </Upload>
                                    </div>
                                    <div v-bind:style="{'float': 'left', 'width': '100%'}">
                                        <Row v-bind:style="{marginBottom: '10px'}">
                                            <i-col span="6">
                                                <span>{{languages.Images.minor[language]}}</span>
                                            </i-col>
                                        </Row>
                                        <div class="upload_list" v-for="item in actions.uploads.items" :key="item.uid">
                                            <template v-if="item.status === 'finished'">
                                                <img :src="item.url">
                                                <div class="upload_list_cover">
                                                    <Icon type="ios-eye-outline"></Icon>
                                                    <Icon type="ios-trash-outline"></Icon>
                                                </div>
                                            </template>
                                            <template v-else>
                                                <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                                            </template>
                                        </div>
                                        <Upload
                                                ref="upload"
                                                :show-upload-list="false"
                                                :format="['jpg','jpeg','png']"
                                                :max-size="2048"
                                                :on-progress="handleUpload"
                                                :on-success="uploadSuccess"
                                                multiple
                                                type="drag"
                                                action="//jsonplaceholder.typicode.com/posts/"
                                                style="display: inline-block;width:96px;">
                                            <div style="width: 96px;height:96px;line-height: 96px;">
                                                <Icon type="ios-camera" size="96"></Icon>
                                            </div>
                                        </Upload>
                                    </div>
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
                                <i-button v-if="actions.create.pos === actions.process.length -1" type="primary"
                                          @click="CreateGoods">{{languages.Actions.confirm[language]}}</i-button>
                            </i-col>
                        </Row>
                    </div>
                </Modal>
            </div>
            <!-- 新增颜色 -->
            <div>
                <Modal v-model="actions.colors.modal" :title="languages.Actions.create[language] + languages.Color[language]" @on-ok="PushColor">
                    <Form :model="actions.create.basic" :label-width="100">
                        <!--颜色名称-->
                        <FormItem :label="languages.Color.name[language]">
                            <Row>
                                <i-col span="20">
                                    <i-input v-model="actions.colors.name[language]" :placeholder="language" maxlength="20" show-word-limit></i-input>
                                </i-col>
                            </Row>
                        </FormItem>
                        <!--颜色色值-->
                        <FormItem :label="languages.Color.rgba[language]">
                            <Row>
                                <i-col span="20">
                                    <ColorPicker v-model="actions.colors.rgb"/>
                                </i-col>
                            </Row>
                        </FormItem>
                    </Form>
                </Modal>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Goods",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                actions: {
                    create: {
                        modal: false,
                        basic: {
                            name: {
                                english: "",
                                chinese: ""
                            },
                            title: {
                                english: "",
                                chinese: ""
                            },
                            description: {
                                english: "",
                                chinese: ""
                            },
                            keywords: [],
                            keyword: {
                                english: "",
                                chinese: "",
                            },
                            tags: [],
                            tag: {
                                english: "",
                                chinese: "",
                            },
                            materials: [],
                            material: {
                                english: "",
                                chinese: "",
                            },
                            rank: 10,
                            colors: [

                            ],
                            sizes: [

                            ],
                            brand: 0,
                            manufacturer: 0,
                        },
                        pos: 0
                    },
                    process: [
                        {key: 0x1011, value: "basic"},
                        {key: 0x1012, value: "category"},
                        {key: 0x1013, value: "color_size"},
                        {key: 0x1014, value: "brand"},
                        {key: 0x1015, value: "images"},
                        {key: 0x1016, value: "price"}
                    ],
                    categories: {
                        total: 0,
                        items: []
                    },
                    colors: {
                        total: 0,
                        items: [],
                        name: {
                            english: "",
                            chinese: ""
                        },
                        rgb: "#19be6b",
                        modal: false
                    },
                    sizes: {
                        groups: [
                            "digital_size",
                            "letter_size",
                        ],
                        group: "digital_size",
                        total: 0,
                        items: []
                    },
                    stock: {
                        columns: [
                            {
                                key: "color",  tree: true,
                                renderHeader: (h, params) => {
                                    params.column.title = this.languages.Color[this.language];
                                    return h("span", this.languages.Color[this.language])
                                }
                            },
                            {
                                key: "size",
                                renderHeader: (h, params) => {
                                    params.column.title = this.languages.Size[this.language];
                                    return h("span", this.languages.Size[this.language])
                                }
                            },
                            {
                                key: "stock",
                                render: (h, params) => {
                                    let key = params.column.key;
                                    let value = params.row[key];
                                    return h("div", [
                                        h("InputNumber", {
                                            props: { min: 0, max: 200, size: 'small', value: value},
                                        }, value)
                                    ])
                                },
                                renderHeader: (h, params) => {
                                    params.column.title = this.languages.Stock[this.language];
                                    return h("span", this.languages.Stock[this.language])
                                }
                            }
                        ],
                        data: []
                    },
                    brands: {
                        total: 0,
                        items: [],
                    },
                    manufacturers: {
                        total: 0,
                        items: [],
                        current: {
                            name: {
                                chinese: "",
                                english: ""
                            },
                            address: {
                                chinese: "",
                                english: ""
                            },
                            contact: "",
                            contactEmail: "",
                            contactPhone: "",
                        }
                    },
                    uploads: {
                        items: [],
                    }
                }
            }
        },
        mounted: function() {
            this.QueryCategories();
            this.QueryColors();
            this.QuerySizes();
            this.QueryBrands();
            this.QueryManufacturers();
        },
        methods: {
            //分类
            QueryCategories: async function() {
                const params = {
                    status: 0x201,
                };
                const headers = {
                    "x-language": this.language
                };
                this.actions.categories = await this.$api.QueryCategories(params, headers) || {total: 0, items: []};
                for(let i in this.actions.categories.items) {
                    this.actions.categories.items[i].value = this.actions.categories.items[i].id;
                    this.actions.categories.items[i].label = this.actions.categories.items[i].name[this.language];
                    this.actions.categories.items[i].children = [];
                }
                this.handleChildCategory(this.actions.categories.items);
            },
            //颜色
            QueryColors: async function() {
                const params = {
                    status: 0x301,
                };
                const headers = {
                    "x-language": this.language
                };
                let value = await this.$api.QueryColors(params, headers) || {total: 0, items: []};
                this.actions.colors.total = value.total;
                this.actions.colors.items = value.items;
            },
            //尺码
            QuerySizes: async function() {
                const params = {
                    status: 0x501,
                    group: this.languages.Size[this.actions.sizes.group][this.language]
                };
                const headers = {
                    "x-language": this.language
                };
                let value = await this.$api.QuerySizes(params, headers) || {total: 0, items: []};
                this.actions.sizes.total = value.total;
                this.actions.sizes.items = value.items;
                this.actions.create.basic.sizes = [];
            },
            //品牌
            QueryBrands: async function() {
                const params = {
                    status: 0x701,
                };
                const headers = {
                    "x-language": this.language
                };
                this.actions.brands = await this.$api.QueryBrands(params, headers) || {total: 0, items: []};
            },
            //生产商
            QueryManufacturers: async function() {
                const params = {
                    status: 0x801,
                };
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryManufacturers(params, headers) || {total: 0, items: []};
                this.actions.manufacturers.total = data.total;
                this.actions.manufacturers.items = data.items;
                this.actions.manufacturers.current = this.actions.manufacturers.items[this.actions.create.basic.manufacturer];
            },
            //商品
            CreateGoods: async function() {

            },
            CreateKeyword: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.actions.create.basic.keyword[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.actions.create.basic.keywords.length <= 4) {
                    this.actions.create.basic.keywords.push(value);
                }
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.keywords.length; i++) {
                    len = len + this.actions.create.basic.keywords[i][this.language].length + 15;
                }
                this.actions.create.basic.keyword[this.language] = "";
                this.actions.create.basic.keyword[this.language] = this.actions.create.basic.keyword[this.language].padStart(len)
            },
            DeleteKeyword: function (index) {
                if (index < 0 || index >= this.actions.create.basic.keywords.length) {
                    return
                }
                this.actions.create.basic.keywords.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.keywords.length; i++) {
                    len = len + this.actions.create.basic.keywords[i][this.language].length + 15;
                }
                this.actions.create.basic.keyword[this.language] = "";
                this.actions.create.basic.keyword[this.language] = this.actions.create.basic.keyword[this.language].padStart(len)
            },
            CreateTag: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.actions.create.basic.tag[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.actions.create.basic.tags.length <= 4) {
                    this.actions.create.basic.tags.push(value);
                }
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.tags.length; i++) {
                    len = len + this.actions.create.basic.tags[i][this.language].length + 15;
                }
                this.actions.create.basic.tag[this.language] = "";
                this.actions.create.basic.tag[this.language] = this.actions.create.basic.tag[this.language].padStart(len)
            },
            DeleteTag: function (index) {
                if (index < 0 || index >= this.actions.create.basic.tags.length) {
                    return
                }
                this.actions.create.basic.tags.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.tags.length; i++) {
                    len = len + this.actions.create.basic.tags[i][this.language].length + 15;
                }
                this.actions.create.basic.tag[this.language] = "";
                this.actions.create.basic.tag[this.language] = this.actions.create.basic.tag[this.language].padStart(len)
            },
            CreateMaterial: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.actions.create.basic.material[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.actions.create.basic.materials.length <= 4) {
                    this.actions.create.basic.materials.push(value);
                }
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.materials.length; i++) {
                    len = len + this.actions.create.basic.materials[i][this.language].length + 15;
                }
                this.actions.create.basic.material[this.language] = "";
                this.actions.create.basic.material[this.language] = this.actions.create.basic.material[this.language].padStart(len)
            },
            DeleteMaterial: function (index) {
                if (index < 0 || index >= this.actions.create.basic.materials.length) {
                    return
                }
                this.actions.create.basic.materials.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.actions.create.basic.materials.length; i++) {
                    len = len + this.actions.create.basic.materials[i][this.language].length + 15;
                }
                this.actions.create.basic.material[this.language] = "";
                this.actions.create.basic.material[this.language] = this.actions.create.basic.material[this.language].padStart(len)
            },
            PushColor: function() {
                if (this.actions.colors.rgb.length <= 0) {
                    return
                }
                let value = {
                    name: {
                        chinese: "",
                        english: ""
                    },
                    rgb: ""
                };
                value.name[this.language] = this.actions.colors.name[this.language];
                value.rgb = this.actions.colors.rgb;
                this.actions.colors.items.push(value);
            },
            handleCategory(value, selectedData) {
                console.log(selectedData, value);
            },
            handleChildCategory: async function(items) {
                const headers = {
                    "x-language": this.language
                };
                items = items || [];
                if (items.length === 0) {
                    return
                }
                for (let i = 0; i < items.length; i++) {
                    let item = items[i];
                    let data = await this.$api.QueryChildCategories(item.id, {}, headers) || [];
                    for (let j in data) {
                        data[j].children = [];
                        data[j].value = data[j].id;
                        data[j].label = data[j].name[this.language];
                    }
                    item.children = data;
                    this.handleChildCategory(item.children);
                }
            },
            handleStock: function () {
                this.actions.stock.data = [];
                let colorLen = this.actions.create.basic.colors.length;
                let sizeLen  = this.actions.create.basic.sizes.length;
                for (let i = 0; i < colorLen && sizeLen > 0; i++) {
                    let c = this.actions.create.basic.colors[i];
                    let item = {};
                    for (let j = 0; j < sizeLen; j++) {
                        let s = this.actions.create.basic.sizes[j];
                        let id = '0' + i + j;
                        if ( j <= 0) {
                            item.color = this.actions.colors.items[c].name[this.language];
                            item.size  = this.actions.sizes.items[s].value;
                            item.stock = 0;
                            item.id    = id;
                            item.children = [];
                        } else {
                            let value = {};
                            value.color = this.actions.colors.items[c].name[this.language];
                            value.size  = this.actions.sizes.items[s].value;
                            value.id    = id;
                            value.stock = 0;
                            item.children.push(value);
                        }
                    }
                    this.actions.stock.data.push(item);
                }
            },
            handleUpload: function(event, file, fileList) {
                this.actions.uploads.items = fileList;
            },
            uploadSuccess (res, file) {
                console.log(res, file);
                file.url = 'https://o5wwk8baw.qnssl.com/7eb99afb9d5f317c912f08b5212fd69a/avatar';
                file.name = '7eb99afb9d5f317c912f08b5212fd69a';
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
    .create_warp {
        padding: 0 16px;
    }
    .keyword, .tag, .material {
        position: absolute;
        left: 30px;
        width: auto;
    }
    .material {
        left: 120px;
        top: -1px;
    }
    .color_size > .color, .color_size > .size, .color_size > .stock {
        width: 100%;
        height: 100px;
        margin-bottom: 5px;
    }
    .add {
        border: none;
    }
    .add:focus {
        box-shadow: none;
    }
    .upload_list {
        display: inline-block;
        width: 130px;
        height: 130px;
        text-align: center;
        line-height: 130px;
        border: 1px solid transparent;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        position: relative;
        box-shadow: 0 1px 1px rgba(0,0,0,.2);
        margin-right: 4px;
    }
    .upload_list img{
        width: 100%;
        height: 100%;
    }
    .upload_list_cover{
        display: none;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0,0,0,.6);
    }
    .demo-upload-list:hover .upload_list_cover{
        display: block;
    }
    .upload_list_cover i{
        color: #fff;
        font-size: 20px;
        cursor: pointer;
        margin: 0 2px;
    }
</style>