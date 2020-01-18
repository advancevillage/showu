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
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Merchandise[language]" width="600" @on-ok="CreateGoods">
                    <div class="create">
                        <Tabs name="goods" type="card" class="create_warp">
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
                                    </Form>
                                </div>
                            </TabPane>
                        </Tabs>
                    </div>
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
                            keywords: [

                            ],
                            keyword: {
                                english: "",
                                chinese: "",
                            }
                        }
                    },
                    process: [
                        {key: 0x1011, value: "basic"},
                        {key: 0x1012, value: "category"},
                        {key: 0x1013, value: "color_size"},
                        {key: 0x1014, value: "material"},
                        {key: 0x1015, value: "price"}
                    ],
                }
            }
        },
        methods: {
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
    .keyword {
        position: absolute;
        left: 30px;
        width: auto;
    }
</style>