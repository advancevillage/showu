<template>
    <div>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="3">
                <span>{{languages.Merchandise.brand[language]}}</span>
            </i-col>
            <i-col span="8">
                <i-select size="small" v-model="brands.selected">
                    <i-option v-for="(item, index) in brands.items" :value="index" :key="index" :label="item.name[language]"></i-option>
                </i-select>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="3">
                <span>{{languages.Merchandise.manufacturer[language]}}</span>
            </i-col>
            <i-col span="8">
                <i-select size="small" v-model="manufacturers.selected" @on-change="manufacturers.current = manufacturers.items[manufacturers.selected]">
                    <i-option v-for="(item, index) in manufacturers.items" :value="index" :key="index" :label="item.name[language]"></i-option>
                </i-select>
            </i-col>
            <i-col span="3">
                <i-button size="small" class="custom_button" icon="ios-add-circle-outline" style="border: none"></i-button>
            </i-col>
        </Row>
        <div v-bind:style="{marginLeft: '12%'}">
            <Row>
                <i-col span="8">
                    <Tag>{{languages.Manufacturer.name[language]}}:
                        {{manufacturers.current.name[language]}}
                    </Tag>
                </i-col>
            </Row>
            <Row>
                <i-col span="8">
                    <Tag>
                        {{languages.Manufacturer.contact[language]}}:
                        {{manufacturers.current.contact}}
                    </Tag>
                </i-col>
            </Row>
            <Row>
                <i-col span="8">
                    <Tag>
                        {{languages.Manufacturer.email[language]}}:
                        {{manufacturers.current.contactEmail}}
                    </Tag>
                </i-col>
            </Row>
            <Row>
                <i-col span="8">
                    <Tag>
                        {{languages.Manufacturer.phone[language]}}:
                        {{manufacturers.current.contactPhone}}
                    </Tag>
                </i-col>
            </Row>
            <Row>
                <i-col span="8">
                    <Tag>
                        {{languages.Manufacturer.address[language]}}:
                        {{manufacturers.current.address[language]}}
                    </Tag>
                </i-col>
            </Row>
        </div>
        <Row v-bind:style="{marginBottom: '10px', marginTop: '10px'}">
            <i-col span="3">
                <span>{{languages.Merchandise.origin[language]}}</span>
            </i-col>
            <i-col span="16">
                <span>{{manufacturers.current.address[language]}}</span>
            </i-col>
        </Row>
        <Row v-bind:style="{marginBottom: '10px'}">
            <i-col span="3">{{languages.Merchandise.material[language]}}</i-col>
            <i-col span="8">
                <i-input size="small" v-model="material[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateMaterial"></i-input>
            </i-col>
            <i-col span="4" class="material">
                <Tag v-for="(item,index) in materials" :key="index">{{item[language]}}<Icon type="ios-close" @click="DeleteMaterial(index)"/></Tag>
            </i-col>
        </Row>
    </div>
</template>

<script>
    export default {
        name: "Brand",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                brands: {
                    total: 0,
                    items: [],
                    status: 0x701,
                    selected: 0,
                },
                manufacturers: {
                    total: 0,
                    items: [],
                    selected: 0,
                    current: {
                        name: {
                            chinese: "",
                            english: ""
                        },
                        address: {
                            chinese: "",
                            english: ""
                        },
                        contact: "",
                        contactEmail: "",
                        contactPhone: "",
                    },
                    status: 0x801
                },
                materials: [],
                material: {
                    english: "",
                    chinese: "",
                },
            }
        },
        mounted: function() {
            this.QueryBrands();
            this.QueryManufacturers();
        },
        methods: {
            //品牌
            QueryBrands: async function() {
                const params = {
                    status: this.brands.status,
                };
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryBrands(params, headers) || {total: 0, items: []};
                this.brands.total = data.total;
                this.brands.items = data.items;
            },
            //生产商
            QueryManufacturers: async function() {
                const params = {
                    status: this.manufacturers.status,
                };
                const headers = {
                    "x-language": this.language
                };
                let data = await this.$api.QueryManufacturers(params, headers) || {total: 0, items: []};
                this.manufacturers.total = data.total;
                this.manufacturers.items = data.items;
                this.manufacturers.current = this.manufacturers.items[this.manufacturers.selected];
            },
            CreateMaterial: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.material[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.materials.length <= 4) {
                    this.materials.push(value);
                }
                let len = 0;
                for (let i = 0; i < this.materials.length; i++) {
                    len = len + this.materials[i][this.language].length + 15;
                }
                this.material[this.language] = "";
                this.material[this.language] = this.material[this.language].padStart(len)
            },
            DeleteMaterial: function (index) {
                if (index < 0 || index >= this.materials.length) {
                    return
                }
                this.materials.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.materials.length; i++) {
                    len = len + this.materials[i][this.language].length + 15;
                }
                this.material[this.language] = "";
                this.material[this.language] = this.material[this.language].padStart(len)
            },
        }
    }
</script>

<style scoped>
    .custom_button {
        border: none;
    }
    .custom_button:focus {
        box-shadow: none;
    }
    .material {
        position: absolute;
        left: 110px;
        width: auto;
        top: -1px;
    }
</style>