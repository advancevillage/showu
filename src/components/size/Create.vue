<template>
    <div>
        <div v-bind:style="{margin: '5% 0'}">
            <Form>
                <!--尺码模版-->
                <FormItem :label="languages.Size.template[language]">
                    <Row>
                        <i-col span="8">
                            <Select v-model="template" size="small">
                                <Option v-for="(item,index) in templates" :value="item" :label="languages.Size[item][language]" :key="index"></Option>
                            </Select>
                        </i-col>
                    </Row>
                </FormItem>
                <!-- 尺码值 -->
                <Form-item :label="languages.Size.value[language]">
                    <Row>
                        <i-col span="8">
                            <i-input v-model="value" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </Form-item>
                <!-- 确定或者重置 -->
                <FormItem>
                    <Row>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="primary" @click="CreateSize" :class="{disabled: confirm}">
                                <span v-if="!confirm">{{this.languages.Actions.confirm[this.language]}}</span>
                                <span v-else>{{this.timeout}}</span>
                            </Button>
                        </i-col>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="default" @click="value = ''">{{this.languages.Actions.reset[this.language]}}</Button>
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
                templates: [
                    "digital_size",
                    "letter_size",
                ],
                template: "digital_size",
                value: "",
                confirm: false,
                timeout: 20,
            }
        },
        methods: {
            CreateSize: async function() {
                if (this.confirm) {
                    return
                }
                if (this.value.length <= 0 ) {
                    return
                }
                const headers = {
                    "x-language": this.language
                };
                let body = {};
                body.group = this.languages.Size[this.template];
                body.value = this.value;
                let data = await this.$api.CreateSize(body, headers);
                this.interceptor(data);
            },
            interceptor(data) {
                console.log(data);
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