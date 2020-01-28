<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <!-- 新增品牌 -->
                    <i-col span="6">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{this.$languages.Actions.create[this.language] + this.$languages.Brand[this.language]}}</i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">
                <Page :total="data.total" :current="page + 1" :page-size="perPage" :page-size-opts="[30, 60, 100]" size="small" @on-change="UpdatePage" @on-page-size-change="UpdatePerPage" show-sizer></Page>
            </div>
            <div class="show">
                <i-table  size="small" border :content="self" :columns="columns" :data="data.items"></i-table>
            </div>
            <!-- 新增品牌 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Brand[language]">
                    <Create :language="language"/>
                    <div slot="footer"></div>
                </Modal>
            </div>
            <!-- 编辑品牌 -->
            <div>
                <Modal v-model="actions.update.modal" :title="languages.Actions.update[language] + languages.Brand[language]" @on-ok="UpdateBrand">
                    <div class="update_brand">
                        <i-form :model="actions.update" :label-width="80">
                            <!-- 品牌名称-->
                            <Form-item :label="languages.Brand[language]">
                                <Row>
                                    <i-col span="12">
                                        <i-input v-model="actions.update.name[language]" :placeholder="language"></i-input>
                                    </i-col>
                                </Row>
                            </Form-item>
                            <!-- 品牌状态-->
                            <Form-item :label="languages.Status[language]">
                                <Row>
                                    <i-col span="8">
                                        <Select v-model="actions.update.status" size="small">
                                            <Option v-for="item in actions.status" :value="item.value" :key="item.value">{{ languages.Status[item.label][language] }}</Option>
                                        </Select>
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
    import api    from '../../axios/api'
    import Create from '../brand/Create'

    export default {
        name: "Brand",
        components: {
            Create,
        },
        data: function () {
            return {
                self: this,
                data: {
                    total: 0,
                    items: []
                },
                languages: this.$languages,
                language: "chinese",
                format: "YYYY-MM-DD HH:mm:ss",
                page: 0,
                perPage: 30,
                status: 0x701,
                columns: [
                    {
                        key: "name", fixed: 'left',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Brand.name[this.language];
                            return h("span", this.$languages.Brand.name[this.language])
                        }
                    },
                    {
                        key: "id",
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Brand.id[this.language];
                            return h("span", this.$languages.Brand.id[this.language])
                        }
                    },
                    {
                        key: "createTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment.unix(value).format(this.format))
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Times.create[this.language];
                            return h("span", this.$languages.Times.create[this.language])
                        }
                    },
                    {
                        key: "updateTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment.unix(value).format(this.format))
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Times.update[this.language];
                            return h("span", this.$languages.Times.update[this.language])
                        }
                    },
                    {
                        key: "deleteTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            if (value > 0) {
                                return h("span", this.$moment.unix(value).format(this.format))
                            } else {
                                return h("span")
                            }
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Times.delete[this.language];
                            return h("span", this.$languages.Times.delete[this.language])
                        }
                    },
                    {
                        key: "action",
                        align: "center",
                        render: (h, params) => {
                            return h("div", [
                                h("Button", {
                                    props: { type: 'primary', size: 'small' },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.actions.update.index =  params.index;
                                            this.actions.update.id    =  params.row.id;
                                            this.actions.update.name.chinese = params.row.name.chinese;
                                            this.actions.update.name.english = params.row.name.english;
                                            this.actions.update.status = params.row.status;
                                            this.actions.update.modal  = true;
                                        }
                                    }
                                }, this.$languages.Actions.update[this.language]),
                                h("Button", {
                                    props: { type: 'error', size: 'small' },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.actions.delete.index = params.index;
                                            this.actions.delete.id    = params.row.id;
                                            this.DeleteBrand();
                                        }
                                    }
                                }, this.$languages.Actions.delete[this.language]),
                            ]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Actions[this.language];
                            return h("span", this.$languages.Actions[this.language])
                        }
                    }
                ],
                actions: {
                    create: {
                        modal: false,
                        name: {
                            english: "",
                            chinese: ""
                        },
                        status: 0x701,
                    },
                    update: {
                        modal: false,
                        index: -1,
                        id: "",
                        name: {
                            english: "",
                            chinese: ""
                        },
                        status: 0,
                        createTime: 0,
                        updateTime: 0,
                        deleteTime: 0
                    },
                    delete: {
                        id: "",
                        index: -1,
                    },
                    status: [
                        {label: 'normal',  value: 0x701},
                        {label: 'deleted', value: 0x702}
                    ]
                }
            }
        },
        mounted: function () {
            this.QueryBrands()
        },
        methods: {
            QueryBrands: async function() {
                const params = {
                    status: this.status,
                    page: this.page,
                    perPage: this.perPage
                };
                const headers = {
                    "x-language": this.language
                };
                this.data = await api.QueryBrands(params, headers) || { total: 0, items: []};
            },
            UpdateBrand: async function() {
                const headers = {
                    "x-language": this.language
                };
                let body = {};
                body.name = this.actions.update.name;
                body.status = this.actions.update.status;
                let data = await  api.UpdateBrand(this.actions.update.id, body, headers);
                this.interceptor(data);
                data = await api.QueryBrand(this.actions.update.id);
                this.data.items[this.actions.update.index].id = data.id;
                this.data.items[this.actions.update.index].name = data.name;
                this.data.items[this.actions.update.index].status = data.status;
                this.data.items[this.actions.update.index].createTime = data.createTime;
                this.data.items[this.actions.update.index].updateTime = data.updateTime;
                this.data.items[this.actions.update.index].deleteTime = data.deleteTime;
            },
            DeleteBrand: async function() {
                const headers = {
                    "x-language": this.language
                };
                let data = await  api.DeleteBrand(this.actions.delete.id, headers);
                this.interceptor(data);
                this.data.items.splice(this.actions.delete.index, 1);
            },
            UpdatePage(page) {
                this.page = page - 1;
                this.refresh();
            },
            UpdatePerPage(perPage) {
                this.perPage = perPage;
                this.refresh();
            },
            refresh() {
                this.QueryBrands()
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
    .warp > .page {
        margin: 5px 0;
        text-align: right;
    }
    .operate > .rows {
        margin-bottom: 5px;
    }

    .create_brand, .update_brand {
        margin: 5% 0;
    }

</style>