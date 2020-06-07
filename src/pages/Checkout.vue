<template>
    <div class="ss_checkout">
        <div class="ss_header">
            <!-- 头部栏 -->
            <Header :width="width" :height="height * 0.13" :opacity=false />
        </div>
        <div class="ss_content">
            <div class="ss_detail">
                <Back :width="width * 0.62" :height="height * 0.05" go="/" :title="languages.OPERATE.BACK[language]"/>
                <Step :items="steps" :width="width * 0.62" :height="height * 0.13" :id="step"/>
                <div class="ss_detail_address" v-bind:style="{width: width * 0.62 + 'px'}">
                    <Address v-for="(item, index) in addresses" :key="index" :item="item" :width="width * 0.15" :language="language" :id="index" :which="address" @which="whichAddress" @clear="deleteAddress" />
                </div>
            </div>
            <div class="ss_summary"></div>
        </div>
    </div>
</template>

<script>
    import Header  from "../components/Business/Header";
    import Back    from "../components/Basic/Back"
    import Step    from "../components/Basic/Step"
    import Address from "../components/Business/Address";


    export default {
        name: "Checkout",
        components: {
            Address,
            Back,
            Header,
            Step,
        },
        data() {
            return {
                languages: this.$languages,
                language: "zh_CN",
                width: window.screen.availWidth,
                height: window.screen.availHeight,
                steps: [],
                step: 0,
                addresses: [
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                    {
                        fullName: "richard.sun",
                        email: "cugriver@qq.com",
                        phone: "11011001110",
                        line1: "111111111111111111111",
                        line2: "",
                        province: "Beijing",
                        city: "Beijing",
                        country: "China",
                        zipCode: 66666,
                        save: (item) => {
                            console.log(item);
                        }
                    },
                ],
                address: -1
            }
        },
        mounted() {
            this.steps.push({icon: "mdi mdi-account", label: this.languages.NOUN.ACCOUNT[this.language]})
            this.steps.push({icon: "mdi mdi-home", label: this.languages.NOUN.ADDRESS[this.language]});
            this.steps.push({icon: "mdi mdi-credit-card", label: this.languages.NOUN.PAY[this.language]});
        },
        methods: {
            whichAddress(index) {
                this.address = index;
            },
            deleteAddress(item, index) {
                this.addresses.splice(index, 1);
            }
        }
    }
</script>

<style scoped>
    .ss_header, .ss_content{
        float: left;
        width: 100%;
    }
    .ss_detail, .ss_summary {
        float: left;
        width: 65%;
        height: 100%;
        padding: 0 5%;
        /*border: 1px solid red;*/
    }
    .ss_detail_address {
        border-top: 1px solid black;
        padding-top: 1%;
    }
    .ss_detail_address > div {
        float: left;
        margin: 2px;
    }
</style>