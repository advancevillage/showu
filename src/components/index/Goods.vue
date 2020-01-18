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
                        <Tabs type="card" class="create_warp">
                            <TabPane v-for="(item, index) in actions.process" :key="index" :label="languages.Merchandise[item.value][language]">
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
</style>