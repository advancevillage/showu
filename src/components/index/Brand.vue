<template>
    <div>
        <div class="brand_warp">
            <div class="operate">
                <i-button type="info" size="small" @click="actions.brandCreate.modal = true">{{actions.brandCreate.title}}</i-button>
            </div>
            <div class="page">
                <Page :total="100" :current="page + 1" :page-size="perPage" :page-size-opts="[30, 50, 150]" size="small" @on-change="UpdatePage" @on-page-size-change="UpdatePerPage" show-sizer></Page>
            </div>
            <div class="show">
                <i-table height="900" size="small" border :content="self" :columns="columns" :data="data"></i-table>
            </div>

            <!-- 新增品牌 -->
            <div>
                <Modal v-model="actions.brandCreate.modal"
                       @on-ok="CreateBrand">
                    <div class="create_brand">
                        <div class="brand">
                            <Input v-model="actions.brandCreate.brandName[language]" size="small" :placeholder="actions.brandCreate.brandName[language]" maxlength="50"/>
                        </div>
                        <div class="brand">
                            <Select v-model="actions.brandCreate.brandStatus" size="small">
                                <Option v-for="item in actions.status" :value="item.value" :key="item.value">{{ item.label }}</Option>
                            </Select>
                        </div>
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
                data: [],
                language: "english",
                format: "YYYY-MM-DD HH:mm:ss",
                page: 0,
                perPage: 25,
                status: 0x701,
                columns: [
                    {
                        title: "品牌名称", key: "brandName", fixed: 'left',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        }
                    },
                    {title: "品牌标识", key: "brandId",},
                    {
                        title: "品牌状态", key: "brandStatus",
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            let str = '无效';
                            switch (value) {
                                case 0x701:
                                    str = '正常';
                                    break;
                                case 0x702:
                                    str = '被删除';
                                    break;
                                default:
                                    str = '无效'
                            }
                            return h("span", str)
                        }
                    },
                    {
                        title: "创建时间", key: "brandCreateTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment(value).format(this.format))
                        }
                    },
                    {
                        title: "更新时间", key: "brandUpdateTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment(value).format(this.format))
                        }
                    },
                    {
                        title: "删除时间", key: "brandDeleteTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            if (value > 0) {
                                return h("span", this.$moment(value).format(this.format))
                            } else {
                                return h("span")
                            }
                        }
                    },
                ],
                actions: {
                    brandCreate: {
                        title: "新增品牌",
                        modal: false,
                        brandName: {
                            english: "please input brand name",
                            chinese: "请输入品牌名称"
                        },
                        brandStatus: 0,
                    },
                    status: [
                        {label: '正常', value: 0x701},
                        {label: '被删除', value: 0x702}
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
                this.data = await api.QueryBrands(params) || []
            },
            CreateBrand: async function() {
                let body = {};
                body.brandName = this.actions.brandCreate.brandName;
                body.brandStatus = this.actions.brandCreate.brandStatus;
                let data = await api.CreateBrand(body);
                switch (data.code) {
                    case 200:
                        this.$Message.success(data.message);
                        break;
                    default:
                        this.$Message.error(data.message);
                }
                this.RefreshData();
            },
            UpdatePage(page) {
                this.page = page - 1;
                this.RefreshData();
            },
            UpdatePerPage(perPage) {
                this.perPage = perPage;
                this.RefreshData();
            },
            RefreshData() {
                this.QueryBrands()
            }
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
        width: 400px;
        height: 400px;
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