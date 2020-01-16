<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <!-- 新增分类 -->
                    <i-col span="6">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{this.$languages.Actions.create[this.language] + this.$languages.Category[this.language]}}</i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">

            </div>
            <div class="show">
                <Tree :data="data.items" :render="renderTree" show-checkbox></Tree>
            </div>
            <!-- 新增分类 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Category[language]" @on-ok="CreateCategory">
                    <div class="create_category">
                        <i-form :model="actions.create" :label-width="80">
                            <!-- 名称-->
                            <Form-item :label="languages.Category[language]">
                                <Row>
                                    <i-col span="12">
                                        <i-input v-model="actions.create.name[language]" :placeholder="language"></i-input>
                                    </i-col>
                                </Row>
                            </Form-item>
                            <Form-item :label="languages.Category.parent[language]">
                                <Row>
                                    <i-col span="12">
                                        <Cascader :data="data.items" change-on-select @on-change="handleCategory"></Cascader>
                                    </i-col>
                                </Row>
                            </Form-item>
                        </i-form>
                    </div>
                </Modal>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Category",
        data() {
            return {
                data: {
                    total: 0,
                    items: []
                },
                languages: this.$languages,
                language: "chinese",
                status: 0x201,
                actions: {
                    create: {
                        modal: false,
                        parent: [],
                        child: [],
                        name: {
                            chinese: "",
                            english: ""
                        },
                        status: 0,
                        level: 1,
                    },
                    level: {

                    }
                }
            }
        },
        mounted: function() {
            this.QueryCategories();
        },
        methods: {
            QueryCategories: async function() {
                const params = {
                    status: this.status,
                };
                const headers = {
                    "x-language": this.language
                };
                this.data = await this.$api.QueryCategories(params, headers) || { total: 0, items: []};
                for(let i in this.data.items) {
                    this.data.items[i].value = this.data.items[i].id;
                    this.data.items[i].label = this.data.items[i].name[this.language];
                    this.data.items[i].children = this.data.items[i].child || []    ;
                }
            },
            CreateCategory: async function() {
                const headers = {
                    "x-language": this.language
                };
                let body = {};
                body.name   = this.actions.create.name;
                body.parent = this.actions.create.parent;
                body.child  = this.actions.create.child;
                body.level  = this.actions.create.level;
                let data = await this.$api.CreateCategory(body, headers);
                this.interceptor(data)

            },
            interceptor(data) {
                switch (data.code) {
                    case 200:
                        this.$Message.success(data.message);
                        break;
                    default:
                        this.$Message.error(data.message);
                }
            },
            renderTree(h, params) {
                return h("span", [
                    h("span", params.data.name[this.language]),
                ])
            },
            handleCategory(value, selectedData) {
                if (selectedData.length <= 0) {
                    return
                }
                let data = selectedData[0];
                this.actions.create.parent.push(data.id);
                this.actions.create.level = data.level + 1;
            }
        }
    }
</script>

<style scoped>
    .warp, .operate, .show {
        width: 100%;
        padding: 0 5px;
        margin-bottom: 5px;
    }
    .operate {
        height: 60px;
    }
    .create_category {
        margin: 5% 0;
    }
</style>