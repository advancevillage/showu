<template>
    <div>
        <div class="color">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Merchandise.color[language]}}</span>
                    <i-button size="small" class="custom_button" icon="ios-add-circle-outline" style="border: none" @click="colors.modal = true"></i-button>
                </i-col>
            </Row>
            <CheckboxGroup v-model="colors.selected">
                <Checkbox v-for="(item, index) in colors.items" :label="index" :key="index" size="small" v-bind:style="{width: '70px', marginBottom: '5px'}">
                    <Tooltip placement="top">
                        <i-button class="custom_button" v-bind:style="{width: '20px', height: '20px', padding: 0}">{{item.name[language]}}</i-button>
                        <i-button slot="content" class="custom_button" v-bind:style="{width: '20px', height: '20px', padding: 0, borderRadius: '100%', backgroundColor:item.rgb}"></i-button>
                    </Tooltip>
                </Checkbox>
            </CheckboxGroup>
        </div>
        <div class="size">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="3">
                    <span>{{languages.Merchandise.size[language]}}</span>
                </i-col>
                <i-col span="5">
                    <i-select size="small" v-model="sizes.group" @on-change="QuerySizes">
                        <i-option v-for="(item, index) in sizes.groups" :value="item" :key="index" :label="languages.Size[item][language]"></i-option>
                    </i-select>
                </i-col>
            </Row>
            <CheckboxGroup v-model="sizes.selected">
                <Checkbox v-for="(item, index) in sizes.items" :value="index" :key="index" :label="index" size="small" v-bind:style="{width: '70px', marginBottom: '5px'}">
                    {{item.value}}
                </Checkbox>
            </CheckboxGroup>
        </div>
        <div class="stock">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="4">
                    <span>{{languages.Merchandise.stock[language]}}</span>
                    <i-button size="small" class="custom_button" icon="ios-refresh-circle" style="border: none" @click="handleStock"></i-button>
                </i-col>
            </Row>
            <i-table row-key="id" height="140" size="small" border :columns="stock.columns" :data="stock.data"></i-table>
        </div>
        <!-- 新增颜色 -->
        <div>
            <Modal v-model="colors.modal" :title="languages.Actions.create[language] + languages.Color[language]" @on-ok="PushColor">
                <Form :label-width="100">
                    <!--颜色名称-->
                    <FormItem :label="languages.Color.name[language]">
                        <Row>
                            <i-col span="20">
                                <i-input v-model="colors.name[language]" :placeholder="language" maxlength="20" show-word-limit></i-input>
                            </i-col>
                        </Row>
                    </FormItem>
                    <!--颜色色值-->
                    <FormItem :label="languages.Color.rgba[language]">
                        <Row>
                            <i-col span="20">
                                <ColorPicker v-model="colors.rgb"/>
                            </i-col>
                        </Row>
                    </FormItem>
                </Form>
            </Modal>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ColorSize",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                languages: this.$languages,
                colors: {
                    total: 0,
                    items: [],
                    name: {
                        english: "",
                        chinese: ""
                    },
                    rgb: "#19be6b",
                    selected: [],
                    modal: false,
                    status: 0x301,
                },
                sizes: {
                    groups: [
                        "digital_size",
                        "letter_size",
                    ],
                    group: "digital_size",
                    total: 0,
                    items: [],
                    selected: [],
                    status: 0x501,
                },
                stock: {
                    columns: [
                        {
                            key: "color",  tree: true,
                            renderHeader: (h, params) => {
                                params.column.title = this.languages.Color[this.language];
                                return h("span", this.languages.Color[this.language])
                            }
                        },
                        {
                            key: "size",
                            renderHeader: (h, params) => {
                                params.column.title = this.languages.Size[this.language];
                                return h("span", this.languages.Size[this.language])
                            }
                        },
                        {
                            key: "stock",
                            render: (h, params) => {
                                return h("div", [
                                    h("InputNumber", {
                                        props: { min: 0, max: 200, size: 'small', value: params.row.stock},
                                        on: {
                                            "on-blur": () => {
                                                let i = parseInt(params.row.id[1]);
                                                let j = parseInt(params.row.id[2]);
                                                //依据handleStock的处理方式
                                                if (j > 0) {
                                                    this.stock.data[i].children[j-1].stock = params.row.stock;
                                                } else {
                                                    this.stock.data[i].stock = params.row.stock;
                                                }
                                                this.Emit();
                                            },
                                            "on-change": (value) => {
                                                params.row.stock = value;
                                            }
                                        }
                                    }, params.row.stock)
                                ])
                            },
                            renderHeader: (h, params) => {
                                params.column.title = this.languages.Stock[this.language];
                                return h("span", this.languages.Stock[this.language])
                            }
                        }
                    ],
                    data: []
                },
                data: {}
            }
        },
        mounted: function() {
            this.QueryColors();
            this.QuerySizes();
        },
        methods: {
            //颜色
            QueryColors: async function() {
                const params = {
                    status: this.colors.status,
                };
                const headers = {
                    "x-language": this.language
                };
                let value = await this.$api.QueryColors(params, headers) || {total: 0, items: []};
                this.colors.total = value.total;
                this.colors.items = value.items;
            },
            //尺码
            QuerySizes: async function() {
                const params = {
                    status: this.sizes.status,
                    group: this.languages.Size[this.sizes.group][this.language]
                };
                const headers = {
                    "x-language": this.language
                };
                let value = await this.$api.QuerySizes(params, headers) || {total: 0, items: []};
                this.sizes.total = value.total;
                this.sizes.items = value.items;
                this.sizes.selected = [];
            },
            PushColor: function() {
                if (this.colors.rgb.length <= 0) {
                    return
                }
                let value = {
                    name: {
                        chinese: "",
                        english: ""
                    },
                    rgb: ""
                };
                value.name[this.language] = this.colors.name[this.language];
                value.rgb = this.colors.rgb;
                this.colors.items.push(value);
            },
            handleStock: function () {
                this.stock.data = [];
                let colorLen = this.colors.selected.length;
                let sizeLen  = this.sizes.selected.length;
                for (let i = 0; i < colorLen && sizeLen > 0; i++) {
                    let c = this.colors.selected[i];
                    let item = {};
                    for (let j = 0; j < sizeLen; j++) {
                        let s = this.sizes.selected[j];
                        let id = '0' + i + j;
                        if ( j <= 0) {
                            item.color = this.colors.items[c].name[this.language];
                            item.size  = this.sizes.items[s].value;
                            item.stock = 0;
                            item.id    = id;
                            item.colorId = this.colors.items[c].id;
                            item.sizeId  = this.sizes.items[s].id;
                            item.children = [];
                        } else {
                            let value = {};
                            value.color = this.colors.items[c].name[this.language];
                            value.size  = this.sizes.items[s].value;
                            value.id    = id;
                            value.stock = 0;
                            value.colorId = this.colors.items[c].id;
                            value.sizeId  = this.sizes.items[s].id;
                            item.children.push(value);
                        }
                    }
                    this.stock.data.push(item);
                }
            },
            Emit: function () {
                let colors = [];
                for (let i = 0; i < this.colors.selected.length; i++) {
                    colors.push(this.colors.items[this.colors.selected[i]]);
                }
                this.data.colors = colors;
                let sizes = [];
                for (let j = 0; j < this.sizes.selected.length; j++) {
                    sizes.push(this.sizes.items[this.sizes.selected[j]]);
                }
                this.data.sizes  = sizes;
                let stocks = [];
                for (let i = 0; i < this.stock.data.length; i++) {
                    let value = {};
                    value.colorId = this.stock.data[i].colorId;
                    value.sizeId  = this.stock.data[i].sizeId;
                    value.total   = this.stock.data[i].stock;
                    stocks.push(value);
                    for (let j = 0; j < this.stock.data[i].children.length; j++) {
                        let value = {};
                        value.colorId = this.stock.data[i].children[j].colorId;
                        value.sizeId  = this.stock.data[i].children[j].sizeId;
                        value.total   = this.stock.data[i].children[j].stock;
                        stocks.push(value);
                    }
                }
                this.data.stocks = stocks;
                this.$emit("colorSizeInfo", this.data);
            }
        }
    }
</script>

<style scoped>
    .color, .size, .stock {
        width: 100%;
        height: 100px;
        margin-bottom: 5px;
    }
    .custom_button {
        border: none;
    }
    .custom_button:focus {
        box-shadow: none;
    }
</style>