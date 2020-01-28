<template>
    <div>
        <div v-bind:style="{margin: '5% 0'}">
            <Form>
                <!-- 名称-->
                <Form-item :label="languages.Manufacturer.name[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="name[language]" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </Form-item>
                <!--地址-->
                <FormItem :label="languages.Manufacturer.address[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="address[language]" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </FormItem>
                <!--联系人-->
                <FormItem :label="languages.Manufacturer.contact[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="contact" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </FormItem>
                <!--手机号-->
                <FormItem :label="languages.Manufacturer.phone[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="phone" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </FormItem>
                <!--邮箱-->
                <FormItem :label="languages.Manufacturer.email[language]">
                    <Row>
                        <i-col span="12">
                            <i-input v-model="email" :placeholder="language"></i-input>
                        </i-col>
                    </Row>
                </FormItem>
                <!-- 确定或者重置 -->
                <FormItem>
                    <Row>
                        <i-col span="3" style="float: right">
                            <Button size="small" type="primary" @click="CreateManufacturer" :class="{disabled: confirm}">
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
        },
        data() {
            return {
                languages: this.$languages,
                name: {
                    english: "",
                    chinese: "",
                },
                address: {
                    english: "",
                    chinese: ""
                },
                contact: "",
                phone: "",
                email: "",
                confirm: false,
                timeout: 20,
            }
        },
        methods: {
            CreateManufacturer: async function() {
                if (this.confirm) {
                    return
                }
                if (this.name[this.language].length <= 0 ) {
                    return
                }
                if (this.address[this.language].length <= 0 ) {
                    return
                }
                if (this.contact.length <= 0 || this.phone <= 0 || this.email <= 0) {
                    return
                }
                const headers = {
                    "x-language": this.language
                };
                let body = {};
                body.name     = this.name;
                body.address  = this.address;
                body.contact  = this.contact;
                body.email    = this.email;
                body.phone    = this.phone;
                let data = await this.$api.CreateManufacturer(body, headers);
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
            },
            reset() {
                this.name[this.language]    = "";
                this.address[this.language] = "";
                this.contact = "";
                this.email   = "";
                this.phone   = "";
            }
        }
    }
</script>

<style scoped>

</style>