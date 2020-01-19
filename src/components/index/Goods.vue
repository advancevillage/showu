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
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Merchandise[language]" width="600">
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
                                        <Row>
                                            <i-col span="6">
                                                <span>{{languages.Merchandise.color[language]}}</span>
                                                <i-button class="add" icon="ios-add-circle-outline" style="border: none" @click="actions.colors.modal = true"></i-button>
                                            </i-col>
                                        </Row>
                                        <CheckboxGroup v-model="actions.create.basic.colors">
                                            <Checkbox v-for="(item, index) in actions.colors.items" :label="index" :key="index" size="small" v-bind:style="{width: '70px', marginBottom: '5px'}">
                                                <Tooltip placement="top">
                                                    <i-button class="add" v-bind:style="{width: '20px', height: '20px', padding: 0}">{{item.name[language]}}</i-button>
                                                    <i-button slot="content" class="add" v-bind:style="{width: '20px', height: '20px', padding: 0, borderRadius: '100%', backgroundColor:item.rgba}"></i-button>
                                                </Tooltip>
                                            </Checkbox>
                                        </CheckboxGroup>
                                    </div>
                                    <div class="size">

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
                                    <ColorPicker v-model="actions.colors.rgba"/>
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
                            rank: 10,
                            colors: [

                            ]
                        },
                        pos: 0
                    },
                    process: [
                        {key: 0x1011, value: "basic"},
                        {key: 0x1012, value: "category"},
                        {key: 0x1013, value: "color_size"},
                        {key: 0x1014, value: "material"},
                        {key: 0x1015, value: "price"}
                    ],
                    categories: {
                        total: 0,
                        items: []
                    },
                    colors: {
                        total: 0,
                        items: [
                            {name: {chinese: "红色", english: ""}, rgba: "#ff0000"},
                        ],
                        name: {
                            english: "",
                            chinese: ""
                        },
                        rgba: "#19be6b",
                        modal: false
                    }
                }
            }
        },
        mounted: function() {
            this.QueryCategories();
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
            PushColor: function() {
                if (this.actions.colors.rgba.length <= 0) {
                    return
                }
                let value = {
                    name: {
                        chinese: "",
                        english: ""
                    },
                    rgba: ""
                };
                value.name[this.language] = this.actions.colors.name[this.language];
                value.rgba = this.actions.colors.rgba;
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
    .keyword, .tag {
        position: absolute;
        left: 30px;
        width: auto;
    }
    .color_size > .color, .color_size > .size {
        width: 100%;
        height: 50%;
    }
    .add {
        border: none;
    }
    .add:focus {
        box-shadow: none;
    }
</style>