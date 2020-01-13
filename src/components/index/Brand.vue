<template>
    <div>
        <div class="brand_warp">
            <i-table size="small" border :content="self" :columns="columns" :data="data"></i-table>
        </div>
    </div>
</template>

<script>
    import api from '../../axios/api'

    export default {
        name: "Brand",
        data() {
            return {
                self: this,
                data: [],
                language: "english",
                format: "YYYY-MM-DD HH:mm:ss",
                columns: [
                    {title: "品牌名称", key: "brandName", fixed: 'left',
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", value[this.language]);
                        }
                    },
                    {title: "品牌标识", key: "brandId",},
                    {title: "品牌状态", key: "brandStatus",
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
                    {title: "创建时间", key: "brandCreateTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment(value).format(this.format))
                        }
                    },
                    {title: "更新时间", key: "brandUpdateTime", sortable: true,
                        render: (h, params) => {
                            let key = params.column.key;
                            let value = params.row[key];
                            return h("span", this.$moment(value).format(this.format))
                        }
                    },
                    {title: "删除时间", key: "brandDeleteTime", sortable: true,
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
                ]
            }
        },
        mounted: function () {
            this.QueryBrands()
        },
        methods: {
            QueryBrands: async function() {
                const params = {
                    status: 0x701
                };
                this.data = await api.QueryBrands(params) || []
            },
        }
    }
</script>

<style scoped>

</style>