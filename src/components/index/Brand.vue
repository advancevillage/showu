<template>
    <div>
        <div class="brand_warp">
            <div class="brand_wrap_list">
                <b-table
                    :paginated="true"
                    :per-page="perPage"
                    :current-page.sync="page"
                    :hoverable="true"
                    :data="data">
                    <template slot-scope="props">
                        <b-table-column field="brandId" label="品牌标识" centered searchable>
                            <span class="tag is-dark" >
                                {{ props.row.brandId }}
                            </span>
                        </b-table-column>
                        <b-table-column field="brandName" label="品牌名称" centered>
                            <span class="tag is-light" >
                                {{ FormatName(props.row.brandName)}}
                            </span>
                        </b-table-column>
                        <b-table-column field="brandStatus" label="品牌状态" centered>
                            <span class="tag" :class="brandStatus.type">
                                {{ FormatStatus(props.row.brandStatus)}}
                                {{ brandStatus.value}}
                            </span>
                        </b-table-column>
                        <b-table-column field="brandCreateTime" label="创建时间" centered>
                            <span class="tag is-info">
                                {{ FormatTimestamp(props.row.brandCreateTime)}}
                            </span>
                        </b-table-column>
                        <b-table-column field="brandCreateTime" label="更新时间" centered>
                            <span class="tag is-warning">
                                {{ FormatTimestamp(props.row.brandUpdateTime)}}
                            </span>
                        </b-table-column>
                        <b-table-column field="brandCreateTime" label="删除时间" centered>
                            <span v-if="props.row.brandDeleteTime > 0" class="tag is-danger">
                                {{ FormatTimestamp(props.row.brandDeleteTime)}}
                            </span>
                        </b-table-column>
                    </template>
                </b-table>
            </div>
            <div class="brand_wrap_operate">

            </div>
        </div>
    </div>
</template>

<script>
    import api from '../../axios/api'

    export default {
        name: "Brand",
        data() {
            return {
                data: [],
                brandStatus: {
                    type: "",
                    value: ""
                },
                perPage: 50,
                page: 1,
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
            FormatTimestamp: function (timestamp)  {
                timestamp = timestamp || 0;
                return this.$moment(timestamp).format('YYYY-MM-DD HH:mm:ss')
            },
            FormatStatus: function (status) {
                switch (status) {
                    case 0x701:
                        this.brandStatus.value = "正常";
                        this.brandStatus.type = "is-success";
                        break;
                    case 0x702:
                        this.brandStatus.value = "被删除";
                        this.brandStatus.type = "is-danger";
                        break;
                    default:
                        this.brandStatus.value = "无效";
                        this.brandStatus.type = "is-primary";
                }
            },
            FormatName: function (name) {
                name = name || {};
                return name.english
            }
        }
    }
</script>

<style scoped>
    .brand_wrap_list, .brand_wrap_operate {
        height: 100%;
        border: 1px solid pink;
        float: left;
        min-height: 1024px;
    }
    .brand_wrap_list {
        width: 80%;
    }
    .brand_wrap_operate {
        width: 20%;
    }
</style>