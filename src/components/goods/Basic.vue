<template>
    <div>
        <Form :label-width="100">
            <!--商品名称-->
            <FormItem :label="languages.Merchandise.name[language]">
                <Row>
                    <i-col span="20">
                        <i-input v-model="name[language]" :placeholder="language" maxlength="50" show-word-limit @on-blur="Emit"></i-input>
                    </i-col>
                </Row>
            </FormItem>
            <!--商品标题-->
            <FormItem :label="languages.Merchandise.title[language]">
                <Row>
                    <i-col span="20">
                        <i-input v-model="title[language]" :placeholder="language" maxlength="100" show-word-limit type="textarea" @on-blur="Emit"></i-input>
                    </i-col>
                </Row>
            </FormItem>
            <!--商品描述-->
            <FormItem :label="languages.Merchandise.description[language]">
                <Row>
                    <i-col span="20">
                        <i-input v-model="description[language]" :placeholder="language" maxlength="300" show-word-limit type="textarea" @on-blur="Emit"></i-input>
                    </i-col>
                </Row>
            </FormItem>
            <!--商品关键字-->
            <FormItem :label="languages.Merchandise.keyword[language]">
                <Row>
                    <i-col span="20">
                        <i-input v-model="keyword[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateKeyword"></i-input>
                    </i-col>
                    <i-col span="4" class="keyword">
                        <Tag v-for="(item,index) in keywords" :key="index">{{item.name[language]}}<Icon type="ios-close" @click="DeleteKeyword(index)"/></Tag>
                    </i-col>
                </Row>
            </FormItem>
            <!--商品标签-->
            <FormItem :label="languages.Merchandise.tag[language]">
                <Row>
                <i-col span="20">
                    <i-input v-model="tag[language]" :placeholder="language" prefix="md-pricetag" @on-enter="CreateTag"></i-input>
                </i-col>
                <i-col span="4" class="tag">
                    <Tag v-for="(item,index) in tags" :key="index">{{item.name[language]}}<Icon type="ios-close" @click="DeleteTag(index)"/></Tag>
                </i-col>
            </Row>
            </FormItem>
            <!--商品排位-->
            <FormItem :label="languages.Merchandise.rank[language]">
                <Row>
                    <i-col span="20">
                        <i-select v-model="rank" @on-change="Emit">
                            <i-option v-for="index in rank" :value="index" :key="index">{{index}}</i-option>
                        </i-select>
                    </i-col>
                </Row>
            </FormItem>
        </Form>
    </div>
</template>

<script>
    export default {
        name: "Basic",
        props: {
            language: {
                type: String,
                required: true,
            },
        },
        data() {
            return {
                languages: this.$languages,
                name: {
                    english: "",
                    chinese: ""
                },
                title: {
                    english: "",
                    chinese: ""
                },
                description: {
                    english: "",
                    chinese: ""
                },
                keyword: {
                    english: "",
                    chinese: ""
                },
                keywords: [],
                tag: {
                    english: "",
                    chinese: ""
                },
                tags: [],
                rank: 10,
                basicInfo: {}
            }
        },
        methods: {
            CreateKeyword: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.keyword[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.keywords.length <= 4) {
                    this.keywords.push({name: value});
                }
                let len = 0;
                for (let i = 0; i < this.keywords.length; i++) {
                    len = len + this.keywords[i].name[this.language].length + 15;
                }
                this.keyword[this.language] = "";
                this.keyword[this.language] = this.keyword[this.language].padStart(len)
            },
            DeleteKeyword: function (index) {
                if (index < 0 || index >= this.keywords.length) {
                    return
                }
                this.keywords.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.keywords.length; i++) {
                    len = len + this.keywords[i].name[this.language].length + 15;
                }
                this.keyword[this.language] = "";
                this.keyword[this.language] = this.keyword[this.language].padStart(len)
            },
            CreateTag: function () {
                let value = {
                    english: "",
                    chinese: ""
                };
                value[this.language] = this.tag[this.language].trim();
                if ( value[this.language].length <= 0 ) {
                    return
                }
                if ( this.tags.length <= 4) {
                    this.tags.push({name: value});
                }
                let len = 0;
                for (let i = 0; i < this.tags.length; i++) {
                    len = len + this.tags[i].name[this.language].length + 15;
                }
                this.tag[this.language] = "";
                this.tag[this.language] = this.tag[this.language].padStart(len)
            },
            DeleteTag: function (index) {
                if (index < 0 || index >= this.tags.length) {
                    return
                }
                this.tags.splice(index, 1);
                let len = 0;
                for (let i = 0; i < this.tags.length; i++) {
                    len = len + this.tags[i].name[this.language].length + 15;
                }
                this.tag[this.language] = "";
                this.tag[this.language] = this.tag[this.language].padStart(len)
            },
            Emit: function () {
                this.basicInfo.name  = this.name;
                this.basicInfo.title = this.title;
                this.basicInfo.rank  = this.rank;
                this.basicInfo.tags  = this.tags;
                this.basicInfo.keywords  = this.keywords;
                this.basicInfo.description = this.description;
                this.$emit("basicInfo", this.basicInfo);
            }
        }
    }
</script>

<style scoped>
    .keyword, .tag {
        position: absolute;
        left: 30px;
        width: auto;
    }
</style>