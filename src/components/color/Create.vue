<template>
    <div>
        <div v-bind:style="{margin: '5% 0'}">
            <Form>
                <!-- 名称-->
                <Form-item :label="languages.Color.name[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="name[language]" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </Form-item>
                <!--色值-->
                <FormItem :label="languages.Color.rgba[language]">
                    <Row>
                        <i-col span="20">
                            <ColorPicker v-model="rgb"/>
                        </i-col>
                    </Row>
                </FormItem>
                <!-- 确定或者重置 -->
                <FormItem>
                    <Row>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="primary" @click="CreateColor" :class="{disabled: confirm}">
                                <span v-if="!confirm">{{this.languages.Actions.confirm[this.language]}}</span>
                                <span v-else>{{this.timeout}}</span>
                            </Button>
                        </i-col>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="default" @click="name[language] = ''">{{this.languages.Actions.reset[this.language]}}</Button>
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
        },
        data() {
            return {
                languages: this.$languages,
                name: {
                    english: "",
                    chinese: "",
                },
                rgb: "#19be6b",
                confirm: false,
                timeout: 20,
            }
        },
        methods: {
            CreateColor: async function() {
                if (this.confirm) {
                    return
                }
                if (this.name[this.language].length <= 0 ) {
                    return
                }
                const headers = {
                    "x-language": this.language
                };
                let body = {};
                body.name = this.name;
                body.rgb  = this.rgb;
                let data = await this.$api.CreateColor(body, headers);
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
                        this.timeout = 20;
                        this.confirm = false;
                    } else {
                        this.timeout--;
                    }
                }, 1000)
            }
        }
    }
</script>

<style scoped>

</style>