<template>
    <div>
        <div class="warp">
            <div class="operate">
                <Row class="rows">
                    <i-col span="6">
                        <i-button type="info" size="small" @click="actions.create.modal = true">{{this.$languages.Actions.create[this.language] + this.$languages.Manufacturer[this.language]}}</i-button>
                    </i-col>
                </Row>
            </div>
            <div class="page">
                <!--<Page :total="data.total" :current="page + 1" :page-size="perPage" :page-size-opts="[30, 60, 100]" size="small" @on-change="UpdatePage" @on-page-size-change="UpdatePerPage" show-sizer></Page>-->
            </div>
            <div class="show">
                <!--<i-table  size="small" border :columns="columns" :data="data.items"></i-table>-->
            </div>
            <!-- 新增 -->
            <div>
                <Modal v-model="actions.create.modal" :title="languages.Actions.create[language] + languages.Manufacturer[language]">
                    <Create :language="language"/>
                    <div slot="footer"></div>
                </Modal>
            </div>
        </div>
    </div>
</template>

<script>
    import Create  from '../manufacturer/Create'

    export default {
        name: "Manufacturer",
        components: {
            Create,
        },
        data() {
            return {
                data: {
                    total: 0,
                    items: []
                },
                languages: this.$languages,
                language: "chinese",
                format: "YYYY-MM-DD HH:mm:ss",
                page: 0,
                perPage: 30,
                actions: {
                    create: {
                        modal: false,
                    },
                }
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
    .warp > .page {
        margin: 5px 0;
        text-align: right;
    }
</style>