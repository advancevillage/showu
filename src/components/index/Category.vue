<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <!-- 新增分类 -->
                    <i-col span="2">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{this.$languages.Actions.create[this.language] + this.$languages.Category[this.language]}}</i-button>
                    </i-col>
                    <i-col span="1">
                        <i-button style="border: none" size="small" @click="refresh"><Icon type="ios-refresh-circle-outline" /></i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">

            </div>
            <div class="show">
                <Tree  class="tree" :data="categories.items" ref="tree" :render="renderTree"></Tree>
            </div>
            <!-- 新增分类 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Category[language]">
                    <Create :language="language" :categories="categories"/>
                    <div slot="footer"></div>
                </Modal>
            </div>
        </div>
    </div>
</template>

<script>
    import Create  from '../category/Create'

    export default {
        name: "Category",
        components: {
            Create
        },
        data() {
            return {
                categories: {
                    total: 0,
                    items: []
                },
                languages: this.$languages,
                language: "chinese",
                actions: {
                    create: {
                        modal: false,
                    },
                }
            }
        },
        mounted: function() {
            this.QueryCategories();
        },
        methods: {
            QueryCategories: async function() {
                const params = {
                    page: 0,
                    perPage: 30,
                    level: 1,
                };
                const headers = {
                    "x-language": this.language
                };
                this.categories = await this.$api.QueryCategories(params, headers) || { total: 0, items: []};
                for(let i in this.categories.items) {
                    this.categories.items[i].expand = true;
                    this.categories.items[i].value = this.categories.items[i].id;
                    this.categories.items[i].children = [];
                    this.categories.items[i].label = this.categories.items[i].name[this.language];
                    this.categories.items[i].title = this.categories.items[i].name[this.language];
                }
                this.handleChildCategory(this.categories.items);
            },
            QueryChildCategories: async function() {
                let node = this.$refs.tree.getSelectedNodes();
                let i = 0;
                if (node.length < i + 1) {
                    return
                }
                let category = node[i];
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryChildCategories(category.id, {}, headers) || [];
                category.children.length = 0;
                for (let i in data) {
                    data[i].children = [];
                    data[i].expand = true;
                    data[i].value = data[i].id;
                    data[i].label = data[i].name[this.language];
                    data[i].title = data[i].name[this.language];
                    category.children.push(data[i]);
                }
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
                        data[j].expand = false;
                        data[j].value = data[j].id;
                        data[j].label = data[j].name[this.language];
                        data[j].title = data[j].name[this.language];
                    }
                    item.children = data;
                    this.handleChildCategory(item.children);
                }
            },
            renderTree(h, params) {
                return h("span", {
                    style: {
                        display: 'inline-block',
                        width: '100%'
                    },
                },[
                    h("span", params.data.title),
                    h("Button", {
                        props: Object.assign({}, this.buttonProps, {
                            icon: "ios-open-outline",
                        }),
                        style: {
                            width: "20px",
                            height: "20px",
                            border: 0,
                            backgroundColor: "unset",
                            marginTop: "-10px",
                            marginLeft: "20px",
                            padding: 0,
                        },
                        on: {
                            click: () => {
                                console.log(params.data);
                            }
                        }
                    }),
                ]);
            },
            refresh() {
                this.QueryCategories();
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
    .tree {
        margin-left: 10px;
    }
</style>