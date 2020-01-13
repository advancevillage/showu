<template>
    <div>
        <div id="container">
            <!-- 商品业务中台 -->
            <div class="container_warp">
                <div class="tree">
                    <Tree :data="tree" @on-select-change="handleTreeSelected" ref="tree">
                    </Tree>
                </div>
                <div class="tabs">
                    <Tabs v-model="pos" type="card" closable size="small" @on-tab-remove="handleDeleteTab">
                        <TabPane v-for="(tab, index) in tabs" :key="index" :label="tab.value">
                            <Brand v-if="tab.key === 0x107"/>
                        </TabPane>
                    </Tabs>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Footer from '../common/Footer'
    import Brand from "./Brand";
    // import Brand  from './Brand'    //品牌管理
    // import Color  from './Color'    //颜色管理
    // import Size   from './Size'     //尺码管理
    // import Category from './Category' //分类管理
    // import Goods  from './Goods'
    // import Images from './Image'    //商品管理
    // import Tag    from './Tag'      //标签管理
    // import Style  from './Style'    //款式管理


    export default {
        data() {
            return {
                tree: [
                    {key: 0x100, title: "商品管理", expand: true, children: [
                            {key: 0x101, title: "商品"},
                            {key: 0x102, title: "分类"},
                            {key: 0x103, title: "颜色"},
                            {key: 0x104, title: "图片"},
                            {key: 0x105, title: "尺码"},
                            {key: 0x106, title: "标签"},
                            {key: 0x107, title: "品牌"},
                            {key: 0x108, title: "生产商"},
                            {key: 0x109, title: "款式"}
                        ]},
                ],
                tabs: [
                    {key: 0x100, value: "商品管理"}
                ],
                pos: 0
            }
        },
        name: "Index",
        components: {
            Brand,
            Footer,
            // Images,
            // Brand,
            // Color,
            // Size,
            // Category,
            // Goods,
            // Tag,
            // Style
        },
        methods: {
            handleDeleteTab(index) {
                this.tabs.splice(index, 1);
            },
            handleCreateTab(key, value) {
                let item = {};
                item.key = key;
                item.value = value;
                this.tabs.push(item);
                this.pos = this.tabs.length - 1;
            },
            handleTest() {
                console.log(this.$refs.tree.getSelectedNodes());
            },
            handleTreeSelected() {
                let node = this.$refs.tree.getSelectedNodes();
                let i = 0;
                if (node.length < i + 1) {
                    return
                }
                let key = node[i].key;
                let value = node[i].title;
                this.handleCreateTab(key, value)
            }
        }
    }
</script>

<style scoped>
    .container_warp {
        margin: 0;
        padding: 0;
        width: 100%;
        max-height: 1024px;
    }
    .container_warp > .tree, .container_warp > .tabs {
        height: 100%;
        float: left;
        min-height: 1024px;
        width: 90%;
    }
    .container_warp > .tree {
        width: 10%;
        border-right: 1px solid black;
    }
    .container_warp > .tabs > .ivu-tabs {
        width: 100%;
    }
</style>