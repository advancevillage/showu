<template>
    <div>
        <div class="brand_warp">
            <div class="operate">
                <i-button type="info" size="small" @click="actions.create.modal = true">{{this.$languages.Actions.create[this.language] + this.$languages.Brand[this.language]}}</i-button>
            </div>
            <div class="page">
                <Page :total="data.total" :current="page + 1" :page-size="perPage" :page-size-opts="[30, 60, 100]" size="small" @on-change="UpdatePage" @on-page-size-change="UpdatePerPage" show-sizer></Page>
            </div>
            <div class="show">
                <i-table height="900" size="small" border :content="self" :columns="columns" :data="data.items"></i-table>
            </div>
            <!-- 新增品牌 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Brand[language]" @on-ok="CreateBrand">
                    <div class="create_brand">
                        <i-form :model="actions.create" :label-width="80">
                            <!-- 品牌名称-->
                            <Form-item :label="languages.Brand[language]">
                                <Row>
                                    <i-col span="12">
                                        <i-input v-model="actions.create.brandName.chinese" placeholder="chinese"></i-input>
                                    </i-col>
                                </Row>
                                <Row>
                                    <i-col span="12">
                                        <i-input v-model="actions.create.brandName.english" placeholder="english"></i-input>
                                    </i-col>
                                </Row>
                            </Form-item>
                            <!-- 品牌状态-->
                            <Form-item :label="languages.Status[language]">
                                <Row>
                                    <i-col span="8">
                                        <Select v-model="actions.create.brandStatus" size="small">
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
    import api from '../../axios/api'

    export default {
        name: "Brand",
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
                        key: "brandName", fixed: 'left',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Brand.brandName[this.language];
                            return h("span", this.$languages.Brand.brandName[this.language])
                        }
                    },
                    {
                        key: "brandId",
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Brand.brandId[this.language];
                            return h("span", this.$languages.Brand.brandId[this.language])
                        }
                    },
                    {
                        key: "brandStatus",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            let str = this.$languages.Status.unknown[this.language];
                            switch (value) {
                                case 0x701:
                                    str = this.$languages.Status.normal[this.language];
                                    break;
                                case 0x702:
                                    str = this.$languages.Status.deleted[this.language];
                                    break;
                                default:
                                    str = this.$languages.Status.unknown[this.language];
                            }
                            return h("span", str)
                        },
                        renderHeader: (h, params) => {
                            params.column.title = this.$languages.Brand.brandStatus[this.language];
                            return h("span", this.$languages.Brand.brandStatus[this.language])
                        }
                    },
                    {
                        key: "brandCreateTime", sortable: true,
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
                        key: "brandUpdateTime", sortable: true,
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
                        key: "brandDeleteTime", sortable: true,
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
                ],
                actions: {
                    create: {
                        modal: false,
                        brandName: {
                            english: "",
                            chinese: ""
                        },
                        brandStatus: 0x701,
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
                this.data = await api.QueryBrands(params) || { total: 0, items: []};
            },
            CreateBrand: async function() {
                let body = {};
                console.log(this.actions.create.brandName);
                body.brandName = this.actions.create.brandName;
                body.brandStatus = this.actions.create.brandStatus;
                let data = await api.CreateBrand(body);
                this.interceptor(data);
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
                this.refresh();
            },
        }
    }
</script>

<style scoped>
    .brand_warp, .operate, .show {
        width: 100%;
        padding: 0 5px;
    }
    .operate {
        height: 30px;
    }
    .create_brand {
        /*width: 400px;*/
        /*height: 400px;*/
        margin: 5% 0;
    }
    .brand {
        margin: 1%;
        width: 60%;
    }
    .brand_warp > .page {
        margin: 5px 0;
        text-align: right;
    }
</style>