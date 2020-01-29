<template>
    <div>
        <div>
            <Form>
                <!-- 名称-->
                <Form-item :label="languages.Category.name[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="name[language]" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </Form-item>
                <Form-item :label="languages.Category.parent[language]">
                    <Row>
                        <i-col span="12">
                            <Cascader :data="categories.items" change-on-select @on-change="handleCategory"></Cascader>
                        </i-col>
                    </Row>
                </Form-item>
                <!-- 确定或者重置 -->
                <FormItem>
                    <Row>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="primary" @click="CreateCategory" :class="{disabled: confirm}">
                                <span v-if="!confirm">{{this.languages.Actions.confirm[this.language]}}</span>
                                <span v-else>{{this.timeout}}</span>
                            </Button>
                        </i-col>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="default" @click="reset">{{this.languages.Actions.reset[this.language]}}</Button>
                        </i-col>
                    </Row>
                </FormItem>
            </Form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Create",
        props: {
            language: {
                type: String,
                required: true,
            },
            categories: {
                type: Object,
                required: true,
            }
        },
        data() {
            return {
                languages: this.$languages,
                name: {
                    english: "",
                    chinese: "",
                },
                parent: [],
                child: [],
                level: 1,
                confirm: false,
                timeout: 5,
            }
        },
        methods: {
            handleCategory(value, selectedData) {
                this.parent = [];
                this.child  = [];
                if (selectedData.length <= 0) {
                    this.level  = 1;
                } else {
                    let index = selectedData.length - 1;
                    let data = selectedData[index];
                    this.parent.push(data.id);
                    this.level  = data.level + 1;
                }
            },
            CreateCategory: async function() {
                const headers = {
                    "x-language": this.language
                };
                if (this.name[this.language].length <= 0 ) {
                    return
                }
                let body = {};
                body.name   = this.name;
                body.level  = this.level;
                body.parent = this.parent;
                body.child  = this.child;
                let data = await this.$api.CreateCategory(body, headers);
                this.interceptor(data);
            },
            interceptor(data) {
                switch (data.code) {
                    case 200:
                        this.$Message.success(data.message);
                        this.confirm = true;
                        this.delay();
                        break;
                    default:
                        this.$Message.error(data.message);
                }
            },
            delay() {
                if (!this.confirm) {
                    return
                }
                let clock = window.setInterval( () => {
                    if (this.timeout < 1) {
                        window.clearInterval(clock);
                        this.timeout = 5;
                        this.confirm = false;
                    } else {
                        this.timeout--;
                    }
                }, 1000)
            },
            reset() {
                this.name[this.language] = "";
                this.parent = [];
                this.child  = [];
                this.level = 1;
            }
        }
    }
</script>

<style scoped>

</style>